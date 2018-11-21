# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
# ImagesPipeline 系统中下载图片的管道
from scrapy.pipelines.images import ImagesPipeline
# 系统管道有下载图片的功能，我们的管道继承了系统的管道，也有了下载图片的功能
class ZhanzhangPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        print('管道方法执行了')
        # print(item['title'])
        # print(item['img'])
        # 这个方法会循环执行
        # 前边每次会传入一个个item，这个item会被交给了引擎，
        # 引擎又交给了管道来运行，管道里面有很多方法
        # 这些方法会依次执行
        yield scrapy.Request(url=item['img'][0],meta={'item':item})
        # 管道里面提供了一系列的内置方法，这下方法会自动从第一个执行到最后一个
    def file_path(self, request, response=None, info=None):
        print('====================')
        item = request.meta['item']
        print(item['title'])
        print(item['img'])
        # 设置图片的路径为，类型名称/url地址
        image_name  = item['img'][0].split('/')[-1]
        # 在拼接图片名字的时候，注意/和\
        path ='%s/%s' % (item['title'],image_name)
        return path

