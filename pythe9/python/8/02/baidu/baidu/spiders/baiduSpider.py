# -*- coding: utf-8 -*-
import scrapy


class BaiduspiderSpider(scrapy.Spider):
    name = 'baiduSpider'
    # 允许爬虫的域名
    # allowed_domains = ['baidu.com']
    # 开始的网址
    start_urls = ['http://www.baidu.com/']
# 请求以后会自动执行的方法、
    def parse(self, response):
        # 获取请求的响应
        print(response.text)
