# -*- coding: utf-8 -*-
from odoo import http

# class MethodLinkPickingInvoice(http.Controller):
#     @http.route('/method_link_picking_invoice/method_link_picking_invoice/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_link_picking_invoice/method_link_picking_invoice/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_link_picking_invoice.listing', {
#             'root': '/method_link_picking_invoice/method_link_picking_invoice',
#             'objects': http.request.env['method_link_picking_invoice.method_link_picking_invoice'].search([]),
#         })

#     @http.route('/method_link_picking_invoice/method_link_picking_invoice/objects/<model("method_link_picking_invoice.method_link_picking_invoice"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_link_picking_invoice.object', {
#             'object': obj
#         })