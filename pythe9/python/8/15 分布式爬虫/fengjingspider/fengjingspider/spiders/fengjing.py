# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisCrawlSpider

class FengjingSpider(RedisCrawlSpider):
    name = 'fengjing'
    allowed_domains = ['netbian.com']
    # start_urls = ['http://pic.netbian.com/4kfengjing/index_3.html']
    redis_key = 'fengjingspider:start_urls'

    def parse(self, response):
        print('--------------------')
        li_list = response.xpath('//div[@class="slist"]/ul/li')
        # print(li_list)
        for li in li_list:
            img = li.xpath('.//a/img/@src').extract_first('')
            print(img)

            title = li.xpath('.//a/b/text()').extract_first('')
            print(title)
