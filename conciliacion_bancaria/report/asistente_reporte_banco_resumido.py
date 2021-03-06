# -*- encoding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError
import time

class AsistenteReporteBancoResumido(models.TransientModel):
    _name = 'conciliacion_bancaria.asistente_reporte_banco_resumido'
    
    def _default_cuenta(self):
        if len(self.env.context.get('active_ids', [])) > 0:
            return self.env.context.get('active_ids')[0]
        else:
            return None

    cuenta_bancaria_id = fields.Many2one('account.account', string='Cuenta', required=True, default=_default_cuenta)
    fecha_desde = fields.Date(string='Fecha Inicial', required=True, default=lambda self: time.strftime('%Y-%m-01'))
    fecha_hasta = fields.Date(string='Fecha Final', required=True, default=lambda self: time.strftime('%Y-%m-%d'))
    saldo_banco = fields.Float('Saldo Banco')

    def print_report(self):
        data = {
             'ids': [],
             'model': 'conciliacion_bancaria.asistente_reporte_banco_resumido',
             'form': self.read()[0]
        }
        return self.env.ref('conciliacion_bancaria.conciliacion_bancaria_action_reporte_banco_resumido').report_action(self, data=data)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
