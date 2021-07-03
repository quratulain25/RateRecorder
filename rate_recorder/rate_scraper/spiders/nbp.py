import re
import scrapy
from scrapy import Request
from datetime import date
from pathlib import Path
import requests
import PyPDF2

from items import RateRecorderItem, BankItem


class NBPSpider(scrapy.Spider):
    name = 'nbp'
    bank_id = 1
    bank_name = 'NBP'
    dummy_url = 'https://www.google.com/'

    def start_requests(self):
        # send dummy request
        yield Request(self.dummy_url, self.parse_response)

    def parse_response(self, response):
        today = date.today()
        date_today = today.strftime('%d-%m-%Y')
        pdf_link = f'https://www.nbp.com.pk/RateSheetFiles/NBP-RateSheet-{date_today}.pdf'
        # pdf_link = f'https://www.nbp.com.pk/RateSheetFiles/NBP-RateSheet-18-06-2021.pdf'

        pdf_resp = requests.get(pdf_link)

        filename = Path('nbp_rates.pdf')
        filename.write_bytes(pdf_resp.content)

        pdfFileObj = open('nbp_rates.pdf', 'rb')

        try:
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
        except PyPDF2.utils.PdfReadError:
            # rate sheet doesnt exists
            return

        pageObj = pdfReader.getPage(0)
        pdf_text = pageObj.extractText()
        usa_import_rate, usa_export_rate = self.extract_rates('US DOLLAR\nUSD\n(.*?)\n(.*?)\n', pdf_text)
        eur_import_rate, eur_export_rate = self.extract_rates('EURO\nEUR\n(.*?)\n(.*?)\n', pdf_text)

        item = RateRecorderItem(
            bank=BankItem.bank.objects.get(name=self.bank_name),
            usa_import_rate=usa_import_rate,
            eur_import_rate=eur_import_rate,
            usa_export_rate=usa_export_rate,
            eur_export_rate=eur_export_rate,
        )

        yield item

    def extract_rates(self, re_string, pdf_text):
        return re.search(re_string, pdf_text, re.DOTALL).groups()
