# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import HongxiuItem
class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['hongxiu.com']
    start_urls = ['https://www.hongxiu.com/all']

    def parse(self, response):
        type_list = response.xpath('//div[@class="range-sidebar fl"]/div/div/a/@href').extract()
        for type in type_list:
            url = 'https://www.hongxiu.com'+type
            # print(url)
            yield scrapy.Request(url=url,callback=self.get_type_with_url)
    def get_type_with_url(self,response):
        # 获取所有分类
        div_list = response.xpath('//div[@class="work-filter type-filter"]/ul/li/a/@href').extract()
        del div_list[0]
        for div in div_list:
            url = 'https://www.hongxiu.com/'+ div[1:]
            yield scrapy.Request(url=url,callback=self.get_book_with_type_url)
    def get_book_with_type_url(self,response):
        book_list = response.xpath('//div[@class="book-img"]/a/@href').extract()
        for book in book_list:
            url = 'https://www.hongxiu.com' +book
            yield scrapy.Request(url=url,callback=self.get_content_with_url)
    def get_content_with_url(self,response):
        item = HongxiuItem()
        kong = re.compile(r'\r')
        img ='http:'+ response.xpath('//div[@class="book-img"]/a/img/@src').extract()[0]
        img = re.sub(kong,'',img)
        book_name = response.xpath('//div[@class="book-info"]/h1/em/text()').extract()
        author = response.xpath('//div[@class="book-info"]/h1/a/text()').extract()
        span_list = response.xpath('//div[@class="book-info"]/p[@class="total"]/span/text()').extract()
        em_list = response.xpath('//div[@class="book-info"]/p[@class="total"]/em/text()').extract()
        zishu = span_list[0] +em_list[0]
        shoucang =span_list[1]+em_list[1]
        dianji = span_list[2] +em_list[2]
        jianjie = response.xpath('//div[@class="book-info"]/p[@class="intro"]/text()').extract()

        item['book_name'] = book_name
        item['author'] = author
        item['zishu'] = zishu
        item['shoucang'] = shoucang
        item['dianji'] = dianji
        item['jianjie'] = jianjie
        item['img'] = [img]

        yield item








