# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv
import scrapy
# from scrapy.pipelines.images import ImagesPipeline

# class ImagesDownLoadPipeline(ImagesPipeline):
#     def get_media_requests(self, item, info):
#         yield scrapy.Request(url=item['img'][0], meta={'item': item})
#
#     def file_path(self, request, response=None, info=None):
#         item = request.meta['item']
#         print('-----------------------')
#         print(item['title'])
#         print(item['img'])
#         name = '图片'
#
#         path = name + '.png'
#
#         return path

class TaobaospiderPipeline(object):
    def __init__(self):
        self.writer = csv.writer(open('taobao.csv','w+',newline=''))
        # 设置标题
        self.writer.writerow(['name','price','shopper'])
    def process_item(self, item, spider):
        rows = zip(item['title'],item['price'],item['shopper'])
        for row in rows:
            self.writer.writerow(row)

        return item

