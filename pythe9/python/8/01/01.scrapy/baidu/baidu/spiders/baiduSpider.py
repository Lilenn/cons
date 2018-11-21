# -*- coding: utf-8 -*-
import scrapy


class BaiduspiderSpider(scrapy.Spider):
    # 爬虫名
    name = 'baiduSpider'  #一定要存在
    # 允许爬虫的范围
    allowed_domains = ['baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # body 为响应体 而不是html中的body标签
        print(response.body)
        # 获取响应头
        print(response.headers)
        # 获取当前状态
        print(response.status)