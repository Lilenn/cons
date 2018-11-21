# -*- coding: utf-8 -*-
import scrapy

from ..items import ZhanzhangItem
class SucaiSpider(scrapy.Spider):
    name = 'sucai'
    allowed_domains = ['sc.chinaz.com']
    start_urls = ['http://sc.chinaz.com/tubiao/xiaotubiao.html']

    def parse(self, response):
        # print(response.text)
        tu_url = response.xpath('//div[@class="text"]/ul/li/p/a/@href').extract()
        # print(tu_url)
        for url in tu_url:
            yield scrapy.Request(url=url,callback=self.get_tubiao_type_info)
    def get_tubiao_type_info(self,response):
        # print(response.text)
        item = ZhanzhangItem()
        img = response.xpath('//div[@class="png_pic"]/img/@src').extract()
        for src in img:

        # print(img)
           item['src'] = [src]
           yield item

