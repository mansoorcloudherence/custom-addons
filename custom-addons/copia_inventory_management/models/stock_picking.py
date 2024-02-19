from odoo import _, api, fields, models

class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    order_id = fields.Many2one('sale.order', string="Sale Oder")

    @api.onchange('order_id')
    def _onchange_order_id(self):
        if self.order_id:
            for rec in self.order_id.order_line:
                self.env['stock.move'].create({
                    'product_id': rec.product_id.id,
                    'name': rec.product_id.name,
                    'product_uom_qty': rec.qty_delivered,
                    'location_id': self.location_id.id,
                    'location_dest_id': self.order_id.picking_ids.location_id.id,
                    'lot_ids': [self.order_id.picking_ids.move_ids.lot_ids.id],
                    'picking_id': self.id,
                    'state': 'done'
                })
            self.state = 'done'





