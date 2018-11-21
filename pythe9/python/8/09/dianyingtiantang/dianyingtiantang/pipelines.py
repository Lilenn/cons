# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class DianyingtiantangPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(host = 'localhost',user = 'root',password = '123456',db = 'Movie',port = 3306)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        self.cursor.execute('insert into movieTable (name,href) VALUES ("{}","{}")'.format(item['title'],item['href']))
        self.connect.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()