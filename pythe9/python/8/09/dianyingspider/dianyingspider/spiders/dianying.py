# -*- coding: utf-8 -*-
import scrapy

from ..items import DianyingspiderItem
class DianyingSpider(scrapy.Spider):
    name = 'dianying'
    allowed_domains = ['ygdy8.net']
    start_urls = ['http://www.ygdy8.net/html/gndy/index.html']

    def parse(self, response):
        more_list = response.xpath('//div[@class="co_area2"]//em/a/@href').extract()
        for more in more_list:
            more_uel = 'http://www.ygdy8.net' + more
            # print(more_uel)
            yield scrapy.Request(url= more_uel,callback=self.more_with_url)
    def more_with_url(self,response):
        detail_list =response.xpath('//div[@class="co_area2"]//td[@height="26"]/b/a[2]/@href').extract()
        # print(detail_list)
        for detail in detail_list:
            detail_url = 'http://www.ygdy8.net' + detail
            # print(detail_url)
            yield scrapy.Request(url= detail_url,callback=self.detail_with_url)
        next_url = response.xpath('//a[text()="下一页"]/@href').extract()
        # print(next_url)
        if len(next_url) !=0:
            url = response.url
            if 'china'in url:
                url = 'http://www.ygdy8.net/html/gndy/china/' + next_url[0]
                yield scrapy.Request(url = url ,callback=self.more_with_url)
            elif 'rihan' in url:
                url = 'http://www.ygdy8.net/html/gndy/rihan/' + next_url[0]
                yield scrapy.Request(url=url, callback=self.more_with_url)
            elif 'dyzz' in url:
                url = 'http://www.ygdy8.net/html/gndy/dyzz/' + next_url[0]
                yield scrapy.Request(url=url, callback=self.more_with_url)
            else:
                url = 'http://www.ygdy8.net/html/gndy/oumei/' + next_url[0]
                yield scrapy.Request(url=url, callback=self.more_with_url)

    def detail_with_url(self,response):
        title = response.xpath('//div[@class="co_area2"]//font/text()').extract_first('')
        print(title)
        href = response.xpath('//td[@style="WORD-WRAP: break-word"]/a/@href').extract_first('')
        print(href)

        item = DianyingspiderItem()
        item['name'] = title
        item['href'] = href
        yield item


