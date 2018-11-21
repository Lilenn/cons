# -*- coding: utf-8 -*-
import scrapy

from ..items import HongxiutianxiangItem
class HongxiuSpider(scrapy.Spider):
    name = 'hongxiu'
    allowed_domains = ['hongxiu.com']
    start_urls = ['https://www.hongxiu.com/finish?gender=2&catId=-1']

    def parse(self, response):
        li_list = response.xpath('//div[@class="right-book-list"]/ul/li')
        for li in li_list:
            img = 'https:'+li.xpath('.//div[@class="book-img"]/a/img/@src').extract_first('')
            print(img)
            name = li.xpath('.//div[@class="book-info"]/h3/a/text()').extract_first('')
            print(name)
            author = li.xpath('.//div[@class="book-info"]/h4/a/text()').extract_first('')
            print(author)
            intro = li.xpath('.//p[@class="intro"]/text()').extract_first('')
            print(intro)

            item = HongxiutianxiangItem()
            item['img'] = img
            item['name'] = name
            item['author'] = author
            item['intro'] = intro

            yield item
