# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import re
import scrapy
from scrapy.loader import ItemLoader

from scrapy.loader.processors import MapCompose,TakeFirst
def newtime(value) :
    time = value.split('·')[0].strip()
    return time
def newzan(value) :
    pattern = re.compile(r'\d+')
    result = re.findall(pattern,value)
    if result :
        return int(result[0])
    else :
        return 0



class ArticleItemLoad(ItemLoader) :
    # default_output_processor = ItemLoader.default_output_processor
    default_output_processor = TakeFirst()
class BoleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    img = scrapy.Field()
    title = scrapy.Field()
    data = scrapy.Field(
        input_processor = MapCompose(newtime)
    )
    detail_url = scrapy.Field()
    zan = scrapy.Field(
        input_process = MapCompose(newzan)
    )
    cang = scrapy.Field(
        input_processor = MapCompose(newzan)
    )
    lun = scrapy.Field(
        input_processor = MapCompose(newzan)
    )
