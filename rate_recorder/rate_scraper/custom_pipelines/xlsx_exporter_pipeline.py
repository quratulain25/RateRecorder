from openpyxl import Workbook

class XlxsExporterPipeline(object):
    wb = Workbook()
    ws = wb.active
    # Set Header
    ws.append(['bank_name',
               'usa_import_rate',
               'usa_export_rate',
               'ca_import_rate',
               'ca_export_rate'])

    def process_item(self, item, spider):
                 # adding data
        line = [
            spider.__class__.name,
            item['usa_import_rate'],
            item['usa_export_rate'],
            item['ca_import_rate'],
            item['ca_export_rate']
        ]
        self.ws.append (line) # add rows
        self.wb.save('current_rates.xlsx')
        return item
