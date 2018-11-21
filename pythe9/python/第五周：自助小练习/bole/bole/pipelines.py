# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymysql
from scrapy.pipelines.images import ImagesPipeline
class BolePipeline(object):
    # def __init__(self):
    #     self.connect = pymysql.connect(host='localhost',
    #                                    password='123456',
    #                                    port=3306,
    #                                    user='root',
    #                                    db ='bole' )
    #     self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
        #
        # self.cursor.execute('insert into mytable(title,data,detail_url,zan,cang,lun)VALUES ("{}","{}","{}","{}","{}","{}")'
        #                     .format(item['title'],item['data'],item['detail_url'],item['zan'],item['cang'],item['lun']))
        # self.connect.commit()
        return item
class ImgPipelines(ImagesPipeline) :
    def get_media_requests(self, item, info):
        name = item['title']
        print(name)
        yield scrapy.Request(url=item['img'],meta={'item': item})
    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        print(item['title'])
        print(item['img'])
        print("+++++++++++++++++++")
        name = item['title']
        path = name + '.jpg'
        return path