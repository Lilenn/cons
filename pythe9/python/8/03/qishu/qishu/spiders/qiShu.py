# -*- coding: utf-8 -*-
import scrapy

from  ..items import QishuItem
class QishuSpider(scrapy.Spider):
    name = 'qiShu'
    allowed_domains = ['qisuu.la']
    start_urls = ['https://www.qisuu.la/']

    def parse(self, response):
    # 获取导航页所有小说的类型
        type_list = response.xpath('//div[@class="nav"]/a/@href').extract()
        # 列表里面第一个是首页 将其去掉
        del type_list[0]

        for type in type_list:
            # 拼接每一个类型的url地址
            url = response.url + type[1:]
            # 在这个方法里面 response.url 为start_url
            yield scrapy.Request(url = url,callback=self.get_next_page_url)

    def get_next_page_url(self,response):
        # 获取下一页的网址
        # print(next_url)
        # print(response.text)
        # print(response.text)
        next_url = response.xpath('//div[@class="tspage"]/a[text()="下一页"]/@href').extract()
        if len(next_url) !=0:
            url = 'https://www.qisuu.la' + next_url[0]
            # print(url)
            yield scrapy.Request(url=url,callback=self.get_content_with_type_url)
    # 用来找到每一种类型对应的内容
    def get_content_with_type_url(self,response):
        # 找到类型中第一页所有小说的详情页地址
        # print(response.url)
        book_list = response.xpath('//div[@class="listBox"]/ul/li/a/@href').extract()
        for book in book_list:
            # 在这个方法里面，response.url为 https://www.qisuu.la/soft/sort02/
            # 到了下一页，response.url 为https://www.qishu.la/soft/sort02/index_2.html
            url ='https://www.qisuu.la' + book
    #         print(url)
            yield scrapy.Request(url= url,callback=self.get_datail_with_book_url)
            # 获取每一本书的内容详情
    def get_datail_with_book_url(self,response):
        item = QishuItem()
        # 获取小说标题
        name = response.xpath('//div[@class="detail_right"]/h1/text()').extract_first('')
    #     print('---------')
        info_list = response.xpath('//div[@class="detail_right"]/ul/li/text()').extract()

        # 获取小说点击量
        clickNum = info_list[0]
        # 获取小说大小
        fileSize = info_list[1]
        # 获取小说类型
        bookType = info_list[2]
        # 获取小说更新时间
        updateTime = info_list[3]
        # 获取小说更新状态
        bookStatue = info_list[4]
        # 获取小说作者
        bookAuthor = info_list[5]

        # 获取需要下载的小说图片地址
        imgUrl = response.xpath('//div[@class="detail_pic"]/img/@src').extract_first('')
        imgUrl = 'https://www.qisuu.la' + imgUrl
        # 获取小说的下载地址、
        downloadUrl = response.xpath('//div[@class="showDown"]/ul/li[3]/script').extract_first('').split(',')[1].strip("'")
        # print(downloadUrl)

        item['name'] = name
        item['clickNum'] = clickNum
        item['fileSize'] = fileSize
        item['bookType'] = bookType
        item['updateTime'] = updateTime
        item['bookStatue'] = bookStatue
        item['bookAuthor'] = bookAuthor
        item['imgUrl'] = [imgUrl]
        item['downloadUrl'] = [downloadUrl]
        yield item




