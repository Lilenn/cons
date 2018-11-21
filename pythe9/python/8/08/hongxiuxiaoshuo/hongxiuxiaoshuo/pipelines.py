# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.conf import settings

class GenspiderPipeline(object):
    def process_item(self, item, spider):
        host = settings['MY_HOST']
        user = settings['MY_USER']
        pwd = settings['MY_PASSWORD']
        db = settings['MY_DB']
        port = settings['MY_PORT']
        cat = settings['CHARSET']
        # 创建数据库
        db = pymysql.connect(host = host,user = user,password = pwd, db = db,charset= cat,port = port)

        cursor = db.cursor()

        cursor.execute('insert into hongxiuTable (zishu,name,author,intro) VALUES ("{}","{}","{}","{}")'.format(item['zishu'],item['name'],item['author'],item['intro']))
        db.commit()
        db.close()

        return item
