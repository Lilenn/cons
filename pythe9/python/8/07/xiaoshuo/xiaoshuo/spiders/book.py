# -*- coding: utf-8 -*-
import scrapy

from ..items import XiaoshuoItem
class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['readnovel.com']
    start_urls = ['https://www.readnovel.com/']

    def parse(self, response):
        # book_list = response.xpath('//div[@class="book-info"]')
        book_list = response.css('.book-info')
        # print(book_list)
        for book in book_list:
            # 获取小说名称
            name = book.xpath('.//h4/a/@title').extract_first('')
            if len(name) ==0:
                name = book.xpath('.//h3/a/@title').extract_first('')
            # print(name)

            des = book.xpath('.//p/text()').extract_first('')
            # print(des)
            author = book.xpath('.//div[@class="state-box cf"]/a/text()').extract_first('')
            # print(author)
            type = book.xpath('.//div[@class="state-box cf"]/i/text()').extract_first('')
            # print(type)

            item = XiaoshuoItem()
            item['name'] = name
            item['des'] = des
            item['author'] = author
            item['type'] = type

            yield item
