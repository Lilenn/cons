# -*- coding: utf-8 -*-
import scrapy

from scrapy_redis.spiders import RedisCrawlSpider
class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['zhaopin.com']
    start_urls = ['http://zhaopin.com/']

    def parse(self, response):
        pass
