# -*- coding: utf-8 -*-
import scrapy
import re
from  ..items import QuibaiItem
class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/imgrank/']

    def parse(self, response):
        item = QuibaiItem()
        div_list = response.xpath('//div[@class="col1"]')
        for div in div_list:
            content_list = div.xpath('.//div[@class="content"]/span/text()').extract()
            konghang = re.compile('\n')
            content = ''
            for content1 in content_list:
                content1 = re.sub(konghang , '',content1)
                content +=content1

            src_list = div.xpath('//div[@class="thumb"]/a/img/@src').extract()
            img = ''
            for src in src_list:
                src = 'https:' + src
                img +=src

            item['content'] = content
            item['img'] = [img]
            yield item

        next_url =response.xpath('//div[@class="pagination"]/li[last()]/a/@href').extract()
        if len(next_url) !=0:
            url = 'https://www.qiushibaike.com' + next_url
            yield scrapy.Request(url=url,callback=self.parse)





