# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3
class TaobaospiserPipeline(object):
    def __init__(self):
        self.connect = sqlite3.connect('diannaoDB')
        self.cursor = self.connect.cursor()
        self.cursor.execute('create table if not exists diannaoTable(title text, price int)')

    def process_item(self, item, spider):
        self.cursor.execute('insert into diannaoTable (title , price) VALUES ("{}","{}")'.format(item['title'],item['price']))
        self.connect.commit()

        return item

    def close_spide(self,spider):
        self.cursor.close()
        self.connect.close()