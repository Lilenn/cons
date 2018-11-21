# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# codecs是用来打开指定文件并且对文件进行转码，防止出现乱码问题
import codecs
import json
import os
class XiaoshuoPipeline(object):
    def __init__(self):
        # w 写文件
        # w+ 读写文件 r 读  r+ 读写文件
        # 前者读写文件，如果文件不存建，则创建
        # 后者读写文件，如果不存在，则抛出异常
        self.file = codecs.open(filename='book.json',mode='w+',encoding='utf-8')
        self.file.write('"list":[')
    # 如果想要将数据写入本地 或者想将数据写入数据库的时候，这个方法保留
    def process_item(self, item, spider):

        # 将item对象转化为字典对象
        res = dict(item)

        # dumps 将字段对象转化为字符串， ascii编码是否可用
        # 如果直接将字典形式的数据写入到文件当中，会发生错误，所以讲字典形式的值，转化为字符串形式，写入到文件中
        str = json.dumps(res,ensure_ascii=False)
        # 将数据写入到文件当中
        self.file.write(str)
        self.file.write(',\n')

    def open_spider(self,spider):
        print('爬虫开始了')

    def close_spider(self,spider):

        print('爬虫结束了')
        # 删除文件当中最后一个字符
        # -1 表示偏移量
        # SEEK_END 定位到文件的最后一个字符
        self.file.seek(-1,os.SEEK_END)
        # 开始执行
        self.file.truncate()

        self.file.seek(-1,os.SEEK_END)
        self.file.truncate()

        self.file.write(']')
        self.file.close()

