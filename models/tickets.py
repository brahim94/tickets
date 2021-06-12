# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from odoo import models, fields, api, _
from odoo.exceptions import Warning, UserError, ValidationError
from odoo.tools.misc import formatLang
from odoo.osv import expression
from odoo.tools import float_is_zero, float_compare
# from odoo.addons import decimal_precision as dp
from dateutil.relativedelta import relativedelta
from odoo.http import request
import qrcode
import base64
from io import BytesIO
from odoo.http import request

# def generate_qr_code(url):
#     qr = qrcode.QRCode(
#              version=1,
#              error_correction=qrcode.constants.ERROR_CORRECT_L,
#              box_size=20,
#              border=4,
#              )
#     qr.add_data(url)
#     qr.make(fit=True)
#     img = qr.make_image()
#     temp = BytesIO()
#     img.save(temp, format="PNG")
#     qr_img = base64.b64encode(temp.getvalue())
#     return qr_img


class StockMove(models.Model):
    _inherit = 'stock.move'
    _description = 'Tickets'

    value = fields.Char(strign='value')
    show_mark_as_todo = fields.Boolean(string="Show Mark As Todo")
    show_check_availability = fields.Boolean(string="Show Check Availability")
    show_validate = fields.Boolean(string="Show Validate")
    show_lots_text = fields.Boolean(string="Show lots text")
    immediate_transfer = fields.Boolean(string="Immediate Transfer")
    picking_type_code = fields.Selection(
        related='picking_type_id.code',
        readonly=True)
    hide_picking_type = fields.Boolean(compute='_compute_hide_pickign_type')
    show_reserved = fields.Boolean(
        'Pre-fill Detailed Operations', default=True,
        help="If this checkbox is ticked, Odoo will automatically pre-fill the detailed "
        "operations with the corresponding products, locations and lot/serial numbers.")
    move_line_exist = fields.Boolean(
        'Has Pack Operations', compute='_compute_move_line_exist',
        help='Check the existence of pack operation on the picking')
    has_packages = fields.Boolean(
        'Has Packages', compute='_compute_has_packages',
        help='Check the existence of destination packages on move lines')
    use_create_lots = fields.Boolean(
        'Create New Lots/Serial Numbers', default=True,
        help="If this is checked only, it will suppose you want to create new Lots/Serial Numbers, so you can provide them in a text field. ")

    # def _generate_qr_code(self):
    #     base_url = request.env['ir.config_parameter'].get_param('web.bsase.url')
    #     base_url += '/web#id=%d&view_type=form&model=%s' % (self.id, self._name)
    #     self.qr_image = generate_qr_code(base_url)
    
    # qr_image = fields.Binary("QR Code", compute='_generate_qr_code')


