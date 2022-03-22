from datetime import datetime

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError
import logging

_logger = logging.getLogger(__name__)

from odoo.addons.report_xlsx.report.report_xlsx import ReportXlsx


class SweepReportXls(ReportXlsx):

    def generate_xlsx_report(self, workbook, data, lines):
        q = """SELECT *,
                AAA.NAME ANALYTIC_ACCOUNT,
                AM.NAME JOURNAL_ENTRY_NUMBER,
                DATE(AM.CREATE_DATE) SWEPT_DATE,
                AM.REF SWEEP_ITEM_JOURNAL_ENTRY_NUMBER,
                AML.NAME SWEPT_ITEMS
            FROM ACCOUNT_MOVE AM
            INNER JOIN ACCOUNT_MOVE_LINE AML ON AM.ID = AML.MOVE_ID
            LEFT OUTER JOIN ACCOUNT_ANALYTIC_ACCOUNT AAA ON AAA.ID = AML.ANALYTIC_ACCOUNT_ID
            WHERE AM.IS_A_SWEEP_JE = TRUE
                AND AM.DATE BETWEEN '{0}' AND '{1}'
            ORDER BY 1; """.format(
            datetime.strptime(data['start_date'], '%Y-%m-%d').date(),
            datetime.strptime(data['end_date'], '%Y-%m-%d').date())
        # print(q)
        self.env.cr.execute(q)
        sheet = workbook.add_worksheet('Sweep Report')
        bold = workbook.add_format({'bold': True})
        format = workbook.add_format({'font_size': 12, 'align': 'vcenter', 'bold': True})
        sheet.set_column(1, 0, 15)
        sheet.write(1, 0, 'Date Range', format)
        sheet.set_column(1, 1, 25)
        sheet.write(1, 1, 'Analytic Account', format)
        sheet.set_column(1, 2, 30)
        sheet.write(1, 2, 'Sweep Journal Entry Number', format)
        sheet.set_column(1, 3, 30)
        sheet.write(1, 3, 'Swept Item Journal Entry Number', format)
        sheet.set_column(1, 4, 25)
        sheet.write(1, 4, 'Swept Items', format)
        sheet.set_column(1, 5, 25)
        sheet.write(1, 5, 'Date Swept', format)
        res = self.env.cr.dictfetchall()
        col = 0
        row = 2
        for i in res:
            sheet.write(row, col, str(i.get('date')))
            sheet.write(row, col + 1, str(i.get('analytic_account')))
            sheet.write(row, col + 2, str(i.get('journal_entry_number')))
            sheet.write(row, col + 3, str(i.get('sweep_item_journal_entry_number')))
            sheet.write(row, col + 4, str(i.get('swept_items')))
            sheet.write(row, col + 5, str(i.get('swept_date')))
            row += 1


SweepReportXls('report.sweep_report.report_sweep_report.xlsx', 'sweep.report')
