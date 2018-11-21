# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
import scrapy
import xlwt

class TaobaoPipeline(object):
    def __init__(self):
        self.workbook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workbook.add_sheet('一加手机')
        self.info_list = ['info','price','shop','img_src']
        self.row = 1
    def open_spider(self,spider):

        for index,info in enumerate(self.info_list):
            self.sheet.write(0,index,info)

    def close_spider(self,spider):

        self.workbook.save("Taobao.xlsx")

    def process_item(self, item, spider):

        data_list = [item["info"],item["price"],item["shop"],item["img_src"]]

        for index,data in enumerate(data_list):
            self.sheet.write(self.row,index,data)
        self.row += 1
        return item

"""
class DownloadImagePipeline(ImagesPipeline):


    def get_media_requests(self, item, info):
        print("-----------------")
        print(item['img_src'][0])
        yield scrapy.Request(url=item['img_src'][0],meta={"item":item})

    def file_path(self, request, response=None, info=None):

        name = request.meta["item"]["info"]

        return name+".jpg"
"""