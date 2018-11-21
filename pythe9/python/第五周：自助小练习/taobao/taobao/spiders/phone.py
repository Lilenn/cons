# -*- coding: utf-8 -*-

# 项目要求：
    # 1.获取淘宝任意一个类别的商品信息
    # 2.将商品名称，价格 ，店铺 三个信息存储到excel中
    # 3.爬虫结束时，将excel以及获取的商品中任意一个商品的
    #   图片一起发送到自己的邮箱


import scrapy
from selenium import webdriver
from ..items import TaobaoItem
from ..sendemail import SendEmail
class PhoneSpider(scrapy.Spider):
    name = 'phone'
    allowed_domains = ['s.taobao.com']
    start_urls = ['https://s.taobao.com/search?q=%E4%B8%80%E5%8A%A0%E6%89%8B%E6%9C%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306']

    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def parse(self, response):

        data_list = response.xpath('//div[@class="item J_MouserOnverReq  "]')

        for data in data_list:

            info = ''.join(data.xpath('.//div[@class="row row-2 title"]/a/text()').extract()).strip().replace('/','')
            price = data.xpath('.//div[@class="price g_price g_price-highlight"]/strong/text()').extract_first()
            shop = data.xpath('.//a[@class="shopname J_MouseEneterLeave J_ShopInfo"]/span[2]/text()').extract_first()
            img_src = "https:" + data.xpath('.//a[@class="pic-link J_ClickStat J_ItemPicA"]/img/@data-src').extract_first()

            # print(img_src)
            item = TaobaoItem()

            item['info'] = info

            item['price'] = price
            item['shop'] = shop
            item['img_src'] = [img_src]

            yield item
    @staticmethod
    def close(spider, reason):
        print("11111111111111")
        email = SendEmail()
        subject = "淘宝手机信息"
        email.send_data(subject)
        return


