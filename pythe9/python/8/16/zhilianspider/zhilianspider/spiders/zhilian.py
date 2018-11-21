# -*- coding: utf-8 -*-
import scrapy
from ..items import ZhilianspiderItem
from selenium import webdriver
from ..items import AticDataItem
from scrapy_redis.spiders import RedisCrawlSpider
class ZhilianSpider(RedisCrawlSpider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    # start_urls = ['https://sou.zhaopin.com/?jl=719']
    redis_key = 'zhilianspider:start_urls'
    # lpush zhilianspider:start_urls https://sou.zhaopin.com/?jl=719

    def __init__(self):
        self.driver = webdriver.PhantomJS()
        self.page_num = 1
    def parse(self, response):
        # print(response.text)
        div_list = response.xpath('//div[@class="listItemBox clearfix"]//a/@href').extract()
        for url in div_list:
            # print(url)

            yield scrapy.Request(url=url,callback=self.get_detail)

        # next_page = 'https://sou.zhaopin.com/?p='+ str(self.page_num + 1) +'&jl=719'
        # print(next_page)
        # if next_page:
            # yield scrapy.Request(url= next_page,callback=self.parse)

    def get_detail(self,response):

        # print(response.url)
        # name = response.xpath('//div[@class="new-info"]//h1/text()').extract_first('')
        # print(name)
        item_loader = AticDataItem(item=ZhilianspiderItem(),response=response)

        item_loader.add_xpath('name','//div[@class="new-info"]//h1/text()')

        item_loader.add_xpath('company','//div[@class="company l"]//a/text()')

        item_loader.add_xpath('salary','//div[@class="l info-money"]//strong/text()')

        item_loader.add_xpath('site','//div[@class="info-three l"]//a/text()')

        item = item_loader.load_item()

        yield item




