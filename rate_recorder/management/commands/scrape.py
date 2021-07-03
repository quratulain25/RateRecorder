from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from rate_recorder.rate_scraper import settings as project_settings
from rate_recorder.rate_scraper.spiders.habib_metro import HabibMetroSpider
from rate_recorder.rate_scraper.spiders.nbp import NBPSpider
from rate_recorder.rate_scraper.spiders.jsbl import JSBLSpider


class Command(BaseCommand):
    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(project_settings)

        process = CrawlerProcess(settings=crawler_settings)
        process.crawl(HabibMetroSpider)
        process.crawl(JSBLSpider)
        process.crawl(NBPSpider)
        process.start()
