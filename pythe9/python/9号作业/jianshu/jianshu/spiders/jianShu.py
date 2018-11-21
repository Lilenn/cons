# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
import re


class JianshuSpider(scrapy.Spider):
    name = 'jianShu'
    allowed_domains = ['jianshu.com']
    start_urls = ['https://www.jianshu.com/search?q=python&page=1&type=note']

    def __init__(self):
        self.driver = webdriver.PhantomJS()

    def parse(self, response):
        # print(response.text)
        # re_comment = re.compile('<!--[^>]*-->')
        # resp = []
        # resp.append(re.sub(re_comment," ",response.text))
        # print(response)
        author_list = response.xpath('//div[@class="content"]/a/@href').extract()
        print(author_list)

        # print(author_list)
        # for author in author_list:
        #     print('-------')
        #     # print(author)
        #     url = 'https://www.jianshu.com' + author
    #         yield scrapy.Request(url=url,callback=self.get_all)
    #
    # def get_all(self,response):
    #     id_list = response.xpath('//div[@id="list-container"]/ul/li/@id').extract()
    #     id = ''
    #     for ids in id_list:
    #         id += ids+"\n"
    #     print(id)
    #
    #     url_list = response.xpath('//div[@id="list-container"]/ul/li/div/a/@href').extract()
    #     # print(url_list)
    #     for url in url_list:
    #         url = 'https://www.jianshu.com' + url
    #         yield scrapy.Request(url=url,callback=self.get_del_content)
    # def get_del_content(self,response):
    #     title = response.xpath('//div[@class="article"]/h1/text()').extract()
    #     # print(title)
    #     content_list = response.xpath('//div[@class="show-content-free"]/p/text()').extract()
    #     print("=====")
    #     remove = re.compile('\n')
    #     douhao = re.compile(',')
    #     content = ''
    #     for string in content_list:
    #         string = re.sub(remove, '', string)
    #         string = re.sub(douhao, '', string)
    #         content += string + ' '
    #     print(content)



