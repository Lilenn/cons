# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class DouguomeishiPipeline(object):
    def __init__(self):
        self.connect = sqlite3.connect('meishiDB')
        self.cursor = self.connect.cursor()
        self.cursor.execute('create table if not exists meishiTable(title text , author text, href text,skip text,img text)')


    def process_item(self, item, spider):

        self.cursor.execute('insert into meishiTable (title,author,img,href,skip) VALUES ("{}","{}","{}","{}","{}")'.format(item['title'],item['author'],item['img'],item['href'],item['skip']))
        self.connect.commit()

        return item
    def close_spider(self,spider):

        self.cursor.close()
        self.connect.close()

