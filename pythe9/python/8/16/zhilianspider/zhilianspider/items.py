# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst

class AticDataItem(ItemLoader):

    default_output_processor = TakeFirst()

class ZhilianspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    company = scrapy.Field()
    salary = scrapy.Field()
    site = scrapy.Field()
    pass
