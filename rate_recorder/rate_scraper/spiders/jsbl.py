import scrapy

from rate_recorder.rate_scraper.items import RateRecorderItem, BankItem


class JSBLSpider(scrapy.Spider):
    name = 'jsbl'
    bank_id = 3
    bank_name = 'JS'

    def start_requests(self):
        urls = ['https://jsbl.com/business/treasury/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.css('.table')
        usa_rates = table.css('tr:contains("USD") ::text').getall()
        usa_import_rate = usa_rates[7]
        usa_export_rate = usa_rates[5]

        eur_rates = table.css('tr:contains("EUR") ::text').getall()
        eur_import_rate = eur_rates[7]
        eur_export_rate = eur_rates[5]

        item = RateRecorderItem(
            bank=BankItem.bank.objects.get(name=self.bank_name),
            usa_import_rate=usa_import_rate,
            usa_export_rate=usa_export_rate,
            eur_export_rate=eur_export_rate,
            eur_import_rate=eur_import_rate
        )

        yield item
