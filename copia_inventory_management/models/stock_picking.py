from odoo import _, api, fields, models

class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    order_id = fields.Many2one('sale.order', string="Sale Oder")

    @api.onchange('order_id')
    def _onchange_order_id(self):
        if self.order_id:
            print("ok")
            # self.location_id = self.workorder_id.production_id.location_src_id.id




