# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BizhiSpider(CrawlSpider):
    name = 'bizhi'
    allowed_domains = ['netbian.com']
    start_urls = ['http://pic.netbian.com/4kfengjing/']

    page_link = LinkExtractor(allow='http://pic.netbian.com/4kfengjing/index_2.html')
    rules = (
        Rule(page_link, callback='get_detail', follow=True),
    )

    def get_detail(self,response):
        print('--------------------')
        li_list = response.xpath('//div[@class="slist"]/ul/li')
        # print(li_list)
        for li in li_list:

            img = li.xpath('.//a/img/@src').extract_first('')
            print(img)

            title =li.xpath('.//a/b/text()').extract_first('')
            print(title)







