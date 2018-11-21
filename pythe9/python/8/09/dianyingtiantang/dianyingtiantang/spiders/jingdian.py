# -*- coding: utf-8 -*-
import scrapy

from ..items import DianyingtiantangItem
class JingdianSpider(scrapy.Spider):
    name = 'jingdian'
    allowed_domains = ['ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/index.html']

    def parse(self, response):
        detail_list = response.xpath('//div[@class="co_area2"]//tr')
        # print(detail_list)
        for detail in detail_list:
            url ='http://www.ygdy8.net'+ detail.xpath('.//td[1]/a[2]/@href').extract_first('')

            yield scrapy.Request(url = url,callback=self.detail_info)
    def detail_info(self,response):
        title = response.xpath('//div[@class="title_all"]//font/text()').extract_first('')
        print(title)
        href = response.xpath('//td[@style="WORD-WRAP: break-word"]/a/@href').extract_first('')
        print(href)

        item = DianyingtiantangItem()
        item['title'] = title
        item['href'] = href

        yield item
