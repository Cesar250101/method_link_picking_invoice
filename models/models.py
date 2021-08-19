# -*- coding: utf-8 -*-

from odoo import models, fields, api



class Picking(models.Model):
    _inherit = 'stock.picking'

    invoice_id = fields.Integer(string="N° Factura", required=False,compute='_compute_invoice_id' )
    invoice_count=fields.Integer(string="Conteo Facturas",compute='_compute_invoice_id')

    @api.one
    @api.depends('origin')
    def _compute_invoice_id(self):
        factura_id=self.env['account.invoice'].search([('origin','=',self.origin)],limit=1).id
        self.invoice_id=factura_id
        self.invoice_count=1
        return True
    
    
    def action_view_invoice(self):
        action = self.env.ref('account.action_invoice_tree1').read()[0]
        action['views'] = [(self.env.ref('account.invoice_form').id, 'form')]
        action['res_id'] = self.invoice_id and self.invoice_id or False 
        action['context']=self.id
        return action 
