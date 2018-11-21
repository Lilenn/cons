# -*- coding: utf-8 -*-
import scrapy
from ..items import ImagenetItem

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['pic.netbian.com']
    # 请求最开始的url
    start_urls = ['http://pic.netbian.com/4kmeishi/']

    def parse(self, response):
        # 根据相应来找到指定的内容，现在找的是src属性
        img_list = response.xpath('//ul[@class="clearfix"]/li/a/img/@src')
        # print(img_list)
        # 找到了很多src属性值 现在进行遍历 分别使用每一个
        for img in img_list:
            # 使用在items.py中创建的数据模型item
            item = ImagenetItem()
            # 拼接url 得到完整的图片地址
            src = 'http://pic.netbian.com' + img.extract()
            # 经得到的下载地址 放入到数据模型 中

            # item['src'] = src
            # 下载地址要包在列表当中
            item['src'] = [src]
            # 将数据模型传输给管道
            yield item

        next_url = response.xpath('//div[@class="page"]/a[text()="下一页"]/@href').extract()
        # print(next_url)
        if len(next_url) !=0:
            url = 'http://pic.netbian.com' + next_url[0]
            # 将url传给scrapy。Request  得到的结果继续用self.parse进行处理
            # callback 回调
            yield scrapy.Request(url=url,callback=self.parse)



