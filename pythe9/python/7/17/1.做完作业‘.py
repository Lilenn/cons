from urllib.request import urlopen

from urllib.parse import quote

import string

import json
import sqlite3

from prettyprinter import pprint
# 汉子转拼音
from xpinyin import Pinyin
p = Pinyin()
# result = p.get_pinyin('北京')
# print(result)
# url = 'http://api.map.baidu.com/telematics/v3/travel_city?location=北京&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'

class DaoYou(object):
    def __init__(self, dbName = '', citylist = []):
        self.citylist= citylist
        self.dbName = dbName
    # 不知道值是什么但知道值是什么类型
        self.tableName = ''
    # 不知道值是什么 也不知道值得类型
        self.connect = None
        self.cursor = None

    def getAllCityinfo(self):

        self.connect = sqlite3.connect('{}'.format(self.dbName))
        self.cursor = self.connect.cursor()

        for city in self.citylist:
            # 将['北京','上海','郑州','杭州','洛阳'] 转化为 bei-jing。。。。。。等拼音形式
            self.tableName = p.get_pinyin(city)
            # bei-jing  转化为 beijing
            self.tableName = self.tableName.replace('-','')
            self.cursor.execute('create table if not exists "{}" (name tsxt,description text , areaName list)'.format(self.tableName))
            self.connect.commit()
            url = 'http://api.map.baidu.com/telematics/v3/travel_city?location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(city)

            # print(url)
# UnicodeEncodeError: 'ascii'codec can't encode characters in position 40-41: ordinal not in range(128)
#            response = urlopen(url)  地址没有中文时
#             response = urlopen(quote(url)) 地址有中文时 引入quote 将中文转码 但是地址里的特殊字符也会被转码

#         因此 引入 afe = string.printable 进行安全转码 --  response = urlopen(quote(url,safe = string.printable))
# urlopen 不支持中文 uote会将中文进行转码 使url地址合法 但是在转码的过程中也会将特殊字符进行转码 所以报错
# safe = string.printable使用安全转码
# 只让中文进行转码 但是特殊符号进行保留
            response = urlopen(quote(url,safe = string.printable))
        # 读取里面的信息  返回的永远是一个字符串
            responseStr = response.read()
            print(responseStr)
          # 将字符串转化成字典
            responseJson = json.loads(responseStr)

            for day in responseJson['result']['itineraries']:
               name = day['name']
               des = day['description']
               areaName = []

               for time in day['itineraries']:
                    for value in time['path']:
                        areaName.append(value['name'])
               self.cursor.execute('INSERT INTO "{}" (name , description ,areaName) VALUES ("{}","{}","{}")'.format(self.tableName,name , des, areaName))
               self.connect.commit()

    def getInfoWith(self,info):
        daylist = ['一','二','三','四','五','六','七']

        info.time = daylist[int(info.time)-1]+'日游'

        info.city = (p.get_pinyin(info.city)).replace('-','')

        self.connect = sqlite3.connect('{}'.format(self.dbName))

        self.cursor = self.connect.cursor()

        self.cursor.execute('select * from "{}" WHERE  name = "{}"'.format(info.city,info.time))
        self.connect.commit()
        result = self.cursor.fetchall()
        if len(result) == 0:
            print('抱歉，目前该城市暂无{}计划'.format(info.time))
        else:
            print(result)

class YouKe(object):
    def __init__(self,city = '', time = ''):
        self.city = city
        self.time = time

dao = DaoYou('cityDB',['北京','上海','郑州','杭州','洛阳','厦门'])
print(dao.citylist)
dao.getAllCityinfo()

youKe = YouKe()
youKe.city = input('你想去哪里旅游')
youKe.time = input('你有几天时间')

dao.getInfoWith(youKe)