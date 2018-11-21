# -*- coding: utf-8 -*-
import scrapy
import re

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['51job.com']
    start_urls = ['https://search.51job.com/list/170200%252C00,000000,0000,00,9,99,python,2,1.html','https://search.51job.com/list/170200,000000,0000,00,9,99,java,2,1.html']

    def parse(self, response):
        # 获取总页码
        total_page = response.xpath('//div[@class="p_in"]/span[1]/text()').extract_first('')
        # print(total_page)
        # 使用正则表达式取出页码里面的所有数字
        res = re.compile(r'\d+')
        result = re.search(res,total_page)
        # 得到的结果是一个对象，从对象中取出匹配的结果
        page_num = int(result.group())
        # 获取请求的网页
        url = response.url
        print(url)
        if 'java' in url:
            for page in range(1,page_num+1):
                java_url = 'https://search.51job.com/list/170200,000000,0000,00,9,99,java,2,{}.html'.format(page)

                yield scrapy.Request(
                    url = java_url,
                    callback=self.get_detail_with_page
                )
        else:
            for page in range(1,page_num+1):
                python_url = 'https://search.51job.com/list/170200%252C00,000000,0000,00,9,99,python,2,{}.html'.format(page)

                yield scrapy.Request(
                    url = python_url,
                    callback=self.get_detail_with_page
                )
    def get_detail_with_page(self,response):
        pass
