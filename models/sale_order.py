# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

logger = logging.getLogger(__name__)
class SaleOrder(models.AbstractModel):
    _inherit = "sale.order"

    def change_invoices_state(self):
        if len(self.invoice_ids) > 0:
            self.invoice_status = "invoiced"
        else:
            raise ValidationError('La Orden de Venta debe tener al menos una factura asociada para cambiar su estado a Facturado')