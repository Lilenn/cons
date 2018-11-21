# -*- coding: utf-8 -*-
import scrapy

from ..items import BizhiItem
class FengjingSpider(scrapy.Spider):
    name = 'fengjing'
    allowed_domains = ['pic.netbian.com']
    start_urls = ['http://pic.netbian.com/4kfengjing/']

    def parse(self, response):
        img_list =response.xpath('//ul[@class="clearfix"]/li/a/img/@src').extract()
        # print(img_list)
        for img in img_list:
            item = BizhiItem()
            src = 'http://pic.netbian.com' + img
            # print(url)
            item['src'] = [src]
            yield item

        netx_url = response.xpath('//div[@class="page"]/a[text()="下一页"]/@href').extract_first('')
        print('------------')
        # print(netx_url)
        if len(netx_url) !=0:
            url = 'http://pic.netbian.com' + netx_url
            # print(url)
            yield scrapy.Request(url=url,callback=self.parse)

