from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)

from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx


class SweepReportXls(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, lines):
        #We can recieve the data entered in the wizard here as data
        print("data")
        print(data)
        print("lines")
        print(lines)
        sheet = workbook.add_worksheet('Sweep Report')
        sheet.write(2, 2, 'Name')


SweepReportXls('report.sweep_report.report_sweep_report.xlsx', 'sweep.report')
