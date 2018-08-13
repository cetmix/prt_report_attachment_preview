from odoo import http
from odoo.http import request, Response
from odoo.addons.web.controllers.main import ReportController


#####################
# Report Controller #
#####################
class PrtReportController(ReportController):

    @http.route(['/report/download'], type='http', auth="user")
    def report_download(self, data, token):
        res = super(PrtReportController, self).report_download(data, token)
        res.headers['Content-Disposition'] = res.headers['Content-Disposition'].replace('attachment', 'inline')
        return res
