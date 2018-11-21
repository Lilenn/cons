# -*- coding: utf-8 -*-
import scrapy

from ..items import DongmanItem
class DongmanSpider(scrapy.Spider):
    name = 'dongman'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kdongman/']

    def parse(self, response):
        pic = response.xpath('//div[@class="slist"]/ul/li/a/img/@src').extract()
        # print(pic)
        for img in pic:
            item = DongmanItem()
            src = 'http://pic.netbian.com' + img
            # print(src)
            item['src'] = [src]
            yield item

        netx_url = response.xpath('//div[@class="page"]/a[text()="下一页"]/@href').extract()
        if len(netx_url) != 0:
            url = 'http://pic.netbian.com' + netx_url[0]
            yield scrapy.Request(url = url,callback=self.parse)


