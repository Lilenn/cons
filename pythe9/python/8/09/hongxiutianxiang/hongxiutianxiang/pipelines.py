# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 引入系统的下载管道模块
import scrapy
import json
import codecs
from scrapy.pipelines.images import ImagesPipeline
class HongxiutianxiangPipeline(object):
    def __init__(self):
        self.file  =codecs.open(filename='hongxiu.json',mode = 'w+',encoding='utf-8')

    def process_item(self, item, spider):

        res = dict(item)
        str = json.dumps(res,ensure_ascii=False)
        self.file.write(str)
        self.file.write(',\n')

        return item

class HongXiuDownLoadPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 取出图片的下载链接
        url = item['img'][0]
        # 请求下载链接 并且传给后续的方法
        yield scrapy.Request(url = url,meta={'item':item})

    # 设置文件路径以及文件名字
    def file_path(self, request, response=None, info=None):
        item = response.meta['item']
        bookName = item['title']
        path = bookName + '.jpg'
        return path

