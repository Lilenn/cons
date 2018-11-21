# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuItem

class YuSpider(scrapy.Spider):
    name = 'yu'
    allowed_domains = ['api.douyucdn.cn']
    base_url = 'http://api.douyucdn.cn/api/v1/getverticalRoom?limit=20&offset='
    offset  =0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        # print(response.text)
        jsonData =json.loads(response.text)
        # print(jsonData)
        if len(jsonData['data']) !=0:
           for data in jsonData['data']:
               item  =DouyuItem()
               room_src = data['room_src']
            # print(room_src)
            # 使用系统管道文件下载图片的话 需要将内容包裹进列表中
               item['src'] = [room_src]
            # 传递item到管道文件中
               yield item
           self.offset +=20
           url = self.base_url + str(self.offset)
           yield scrapy.Request(url=url,callback=self.parse)





