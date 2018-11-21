# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JodspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    companyName =scrapy.Field()
    cityName =scrapy.Field()
    min_salary = scrapy.Field()
    max_salary = scrapy.Field()
    date = scrapy.Field()

    pass
