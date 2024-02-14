from odoo import _, api, fields, models

class StockLocation(models.Model):
    _inherit = 'stock.location'


    active = fields.Boolean('Enabled', default=True)
    iscoldstorage = fields.Boolean('isColdStorage', default=False)
    issecure = fields.Boolean('isSecure', default=False)
    issegregated = fields.Boolean('isSegregated', default=False)



    usage = fields.Selection([
        ('supplier', 'Vendor Location'),
        ('view', 'View'),
        ('internal', 'Internal Location'),
        ('customer', 'Customer Location'),
        ('inventory', 'Inventory Loss'),
        ('production', 'Production'),
        ('transit', 'Transit Location')], string='Aisle Type',
        default='internal', index=True, required=True,
        help="* Vendor Location: Virtual location representing the source location for products coming from your vendors"
             "\n* View: Virtual location used to create a hierarchical structures for your warehouse, aggregating its child locations ; can't directly contain products"
             "\n* Internal Location: Physical locations inside your own warehouses,"
             "\n* Customer Location: Virtual location representing the destination location for products sent to your customers"
             "\n* Inventory Loss: Virtual location serving as counterpart for inventory operations used to correct stock levels (Physical inventories)"
             "\n* Production: Virtual counterpart location for production operations: this location consumes the components and produces finished products"
             "\n* Transit Location: Counterpart location that should be used in inter-company or inter-warehouses operations")
    scrap_location = fields.Boolean('Is a Scrap Aisle?', default=False,
                                    help='Check this box to allow using this location to put scrapped/damaged goods.')
    return_location = fields.Boolean('Is a Return Aisle?',
                                     help='Check this box to allow using this location as a return location.')
    replenish_location = fields.Boolean('Replenish Aisle', copy=False, compute="_compute_replenish_location",
                                        readonly=False, store=True,
                                        help='Activate this function to get all quantities to replenish at this particular location')
