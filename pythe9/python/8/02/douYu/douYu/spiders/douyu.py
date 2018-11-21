# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuItem
class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['api.douyucdn.cn']
    start_urls = [ 'http://api.douyucdn.cn/api/v1/getverticalRoom?limit=20&offset=1']

    def parse(self, response):
        item = DouyuItem()
        x = json.loads(response.text)
        for img in x['data']:
            src = img['room_src']

            item['src'] = [src]

            yield item
        for y in range(2, 501):
            url = 'http://api.douyucdn.cn/api/v1/getverticalRoom?limit=20&offset=' + str(y)

            yield scrapy.Request(url=url, callback=self.parse)

