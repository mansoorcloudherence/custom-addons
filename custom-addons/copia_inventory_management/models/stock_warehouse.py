from odoo import _, api, fields, models

class StockWarehouse(models.Model):
    _inherit = 'stock.warehouse'

    active = fields.Boolean('Enabled', default=True)