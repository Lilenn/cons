# -*- coding: utf-8 -*-
import scrapy
from ..items import TaobaospiderItem
from selenium import webdriver
from ..emailSender import SenderEmail
class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['https://s.taobao.com/search?q=%E6%B8%B8%E6%88%8F%E9%85%8D%E4%BB%B6&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306']
    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def parse(self, response):
        # print(response.text)
        div_list = response.xpath('//div[@class="item J_MouserOnverReq  "]')
        # print(div_list)
        for div in div_list:
            title = div.xpath('.//a/img/@alt').extract_first('')
            print(title)
            price = div.xpath('.//div[@class="price g_price g_price-highlight"]/strong/text()').extract_first('')
            print(price)
            shopper = div.xpath('.//div[@class="shop"]/a/span[2]/text()').extract_first('')
            print(shopper)
            # img = div.xpath('.//a/img/@src').extract_first('')
            # if len(img) !=0:
            #     src ='https:' + img

            # print(src)
            item = TaobaospiderItem()
            # item['img'] = [src]
            item['title'] = [title]
            item['price'] = [price]
            item['shopper'] = [shopper]

            yield item

    @staticmethod
    def close(spider, reason):
        print('11111111111111111111')
        email = SenderEmail()
        subject = '淘宝信息'
        email.send_data(subject)
        return