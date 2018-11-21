# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import pymysql
from scrapy.pipelines.images import ImagesPipeline

# class jobboleDownImage(ImagesPipeline):
#     def get_media_requests(self, item, info):
#
#         yield scrapy.Request(url = item['img'],meta = {'item':item})
#     def file_path(self, request, response=None, info=None):
#         item = request.meta['item']
#         print('-----------------------')
#         print(item['title'])
#         print(item['img'])
#         name = item['title']
#
#         path = name + '.jpg'
#
#         return path


class JobbolePipeline(object):
    # def __init__(self):
    #     # localhost
    #     self.connect = pymysql.connect(host='localhost',
    #                                    user='root',
    #                                    password='123456',
    #                                    db='jobbole',
    #                                    port=3306)
    #     self.cursor = self.connect.cursor()
    def process_item(self, item, spider):
#
        # self.cursor.execute('insert into blog (img , title  ,time ,detail_url,dianzan,comment_num,book_mark_num) VALUES ("{}","{}","{}","{}","{}","{}","{}")'.
        #                     format(item['img'],item['title'],item['time'],item['detail_url'],item['dianzan'],item['comment_num'],item['book_mark_num']))
        #
        # self.connect.commit()
#
        return item
    # def close_spider(self ,spider):
    #     self.cursor.close()
    #     self.connect.close()



# def test(a=1,b=2):
#
#     print('123')
# test(1,2)
# test(b=2 ,a = 1)
