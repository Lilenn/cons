# -*- coding: utf-8 -*-
import scrapy

from ..items import HongxiuxiaoshuoItem
class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['hongxiu.com']
    start_urls = ['https://www.hongxiu.com/finish?gender=1&catId=-1']

    def parse(self, response):
        li_list = response.xpath('//div[@class="right-book-list"]/ul/li')
        # print(li_list)
        for li in li_list:
            name = li.xpath('.//div[@class="book-info"]/h3/a/@title').extract_first('')
            print(name)
            author = li.xpath('.//div[@class="book-info"]/h4/a/text()').extract_first('')
            print(author)
            intro = li.xpath('.//p[@class="intro"]/text()').extract_first('')
            print(intro)
            zishu = li.xpath('.//p[@class="tag"]/span[last()]/text()').extract_first('').replace('万','')
            print(zishu)

            item = HongxiuxiaoshuoItem()
            item['name'] = name
            item['author'] = author
            item['intro'] = intro
            item['zishu'] = zishu

            yield item


