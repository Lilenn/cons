# -*- coding: utf-8 -*-
import scrapy
import datetime
from ..emailSender import SendEmail
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def start_requests(self):
        email = SendEmail()
        # 获取现在时间
        body = '爬虫开始时间为:{}'.format(datetime.datetime.now())

        subject = '重要通知，明天放假'

        receiver = '846077763@qq.com'

        email.send_text_email(body,receiver,subject)

        yield scrapy.Request(url = 'https://www.baidu.com')

    def parse(self, response):
        pass


    # 项目要求：
    # 1.获取淘宝任意一个类别的商品信息
    # 2.将商品名称、价格、店铺 三个信息存储到excel中
    # 3.爬虫结束时，将excel以及获取的商品中任意一个商品的图片一起发送到自己的邮箱。。。
