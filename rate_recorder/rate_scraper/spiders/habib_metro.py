import scrapy

from rate_recorder.rate_scraper.items import RateRecorderItem, BankItem


class HabibMetroSpider(scrapy.Spider):
    name = 'habib_metro'
    bank_id = 2
    bank_name = 'Habib Metro'

    def start_requests(self):
        urls = ['https://www.habibmetro.com/exchange-rates/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        table = response.css('h4:contains(RATES)+table')
        usa_rates = table.css('tr:contains("U.S.A.") ::text').getall()[2:4]
        usa_import_rate, usa_export_rate = usa_rates

        eur_rates = table.css('tr:contains("EURO") ::text').getall()[2:4]
        eur_import_rate, eur_export_rate = eur_rates

        item = RateRecorderItem(
            bank=BankItem.bank.objects.get(name=self.bank_name),
            usa_import_rate=usa_import_rate,
            eur_import_rate=eur_import_rate,
            usa_export_rate=usa_export_rate,
            eur_export_rate=eur_export_rate,
        )

        yield item
