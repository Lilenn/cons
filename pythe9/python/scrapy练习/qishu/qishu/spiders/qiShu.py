# -*- coding: utf-8 -*-
import scrapy

from ..items import QishuItem

class QishuSpider(scrapy.Spider):
    name = 'qiShu'
    allowed_domains = ['qisuu.la']
    start_urls = ['https://www.qisuu.la/']

    def parse(self, response):
        # print(response.text)
        type_list = response.xpath('//div[@class="nav"]/a/@href').extract()
        # print(type_list)
        del type_list[0]
        for type in type_list:
            url = response.url + type[1:]
            # print(url)
            yield scrapy.Request(url=url,callback=self.get_next_page_url)

    def get_next_page_url(self,response):
        # 获取下一页的网址
        next_url = response.xpath('//div[@class="tspage"]/a[text()="下一页"]/@href').extract()
        if len(next_url) != 0:
            url = 'https://www.qisuu.la/' + next_url[0]
            # print(url)
            yield scrapy.Request(url=url,callback=self.get_content_with_type_url)

    def get_content_with_type_url(self,response):
        # 找到类型中第一页所有小说的详情页地址
        book_list = response.xpath('//div[@class="listBox"]/ul/li/a/@href').extract()
        # print(book_list)
        for book in book_list:
            url =  'https://www.qisuu.la' + book
            # print(url)
            yield scrapy.Request(url=url,callback=self.get_detail_with_book_url)

    def get_detail_with_book_url(self,response):
        item = QishuItem()
        # 获取小说名字
        name = response.xpath('//div[@class="detail_right"]/h1').extract()
        # 获取小说各方面指标
        info_list = response.xpath('//div[@class="detail_right"]/ul/li/text()').extract()
        # print(info_list)
        # 获取小说点击量
        clickNum = info_list[0]
        # 获取小说大小
        fileSize = info_list[1]
        # 获取小说类型
        bookType = info_list[2]
        # 获取小说更新日期
        updateTime = info_list[3]
        # 是否连载
        bookStatus = info_list[4]
        # 获取小说作者
        bookAuthor = info_list[5]
        # 获取小说封面
        imgUrl = response.xpath('//div[@class="detail_pic"]/img/@src').extract_first()
        imgUrl = 'https://www.qisuu.la' + imgUrl

        # 获取小说下载地址
        downLoadUrl = response.xpath('//div[@class="showDown"]/ul/li[3]/script').extract_first('').split(',')[1].strip("'")
        print('============')
        print(downLoadUrl)
        print('=============')

        item['name'] = name
        item['clickNum'] = clickNum
        item['fileSize'] = fileSize
        item['bookType'] = bookType
        item['updateTime'] = updateTime
        item['bookStatus'] = bookStatus
        item['bookAuthor'] = bookAuthor
        item['imgUrl'] = [imgUrl]
        item['downLoadUrl'] = [downLoadUrl]
        yield item