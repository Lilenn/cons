# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class HongxiutianxiangPipeline(object):
    def process_item(self, item, spider):
        return item
class HongXiuDBPipeline(object):
    def open_spider(self,spider):
        self.connect = sqlite3.connect('hongxiuDB')
        self.cursor = self.connect.cursor()
        self.cursor.execute('create table if not exists bookTable(name text ,author text,img text,intro text)')
        self.connect.commit()

    def process_item(self,item,spider):

        self.cursor.execute('insert into bookTable (name,author,img,intro) VALUES ("{}","{}","{}","{}")'
                            .format(item['name'],item['author'],item['img'],item['intro']))
        self.connect.commit()

    def close_spider(self,spider):
        self.cursor.close()
        self.connect.close()