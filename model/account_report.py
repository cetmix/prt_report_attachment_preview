# -*- coding: utf-8 -*-

import time
from odoo import api, models, _
from odoo.exceptions import UserError

class ReportFinancialInherit(models.AbstractModel):
    _inherit = 'report.account.report_financial'

    @api.model
    def render_html(self, docids, data=None):
        if not data.get('form') or not data['context'].get('active_model') or not data['context'].get('active_id'):
            raise UserError(_("Form content is missing, this report cannot be printed."))

        self.model = data['context'].get('active_model')
        docs = self.env[data['model']].browse(data['context'].get('active_id'))
        report_lines = self.get_account_lines(data.get('form'))
        docargs = {
            'doc_ids': data['ids'],
            'doc_model': data['model'],
            'data': data['form'],
            'docs': docs,
            'time': time,
            'get_account_lines': report_lines,
        }
        return self.env['report'].render('account.report_financial', docargs)