# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy_djangoitem import DjangoItem
from rate_recorder.models import Rates, Bank

class RateRecorderItem(DjangoItem):
    # define the fields for your item here like:
    django_model = Rates

class BankItem(DjangoItem):
    # define the fields for your item here like:
    bank = Bank
