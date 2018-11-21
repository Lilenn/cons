# -*- coding: utf-8 -*-
import scrapy

from selenium import webdriver
from ..items import TaobaospiserItem
class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['https://s.taobao.com/search?initiative_id=tbindexz_20170306&ie=utf8&spm=a21bo.2017.201856-taobao-item.1&sourceId=tb.index&search_type=item&ssid=s5-e&commend=all&imgfile=&q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&suggest=history_1&_input_charset=utf-8&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&suggest_query=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&source=suggest']

    def __init__(self):
        self.driver =webdriver.PhantomJS()
    def parse(self, response):
        com_list = response.xpath('//div[@class="info-cont"]')
        # print(len(com_list))
        for com in com_list:
            title = com .xpath('.//div[@class="title-row "]/a/@title').extract_first('')
            print(title)
            price = com.xpath('.//div[@class="sale-row row"]/div/span/strong/text()').extract_first('')
            print(price)

            item = TaobaospiserItem()
            item['title'] = title
            item['price'] = price

            yield item



