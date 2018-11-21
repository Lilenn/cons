# -*- coding: utf-8 -*-
import scrapy
import re

class TiebaSpider(scrapy.Spider):
    name = 'tieBa'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/5927469611']
    f = open('tieba.txt','a',encoding='utf-8')
    def parse(self, response):
        div_list = response.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
        # print(div_list)
        for div in div_list:
            author = div.xpath('.//div[@class="louzhubiaoshi_wrap"]').extract()
            # print(author)
            if len(author) !=0:
                content_list = div.xpath('.//cc//text()').extract()
                # print(content_list)
                remove = re.compile('\s')
                douhao = re.compile(',')
                content = ''
                for string in content_list:
                    string = re.sub(remove,'',string)
                    string = re.sub(douhao,'',string)
                    # print(string)
                    content +=string + ' '
                print(content)
                self.f.write(content)
                self.f.write('\n')
