from urllib.request import urlopen
from urllib.parse import quote
import string
import json
from prettyprinter import pprint

from xpinyin import Pinyin
p = Pinyin()
import sqlite3
class DaoYan(object):
    def __init__(self,dbname = '', citylist =[]):
        self.dbname = dbname
        self.citylist = citylist
        self.tablename = ''
        self.connect = None
        self.cursor = None

    def getAllCityInfo(self):

        self.connect = sqlite3.connect('{}'.format(self.dbname))
        self.cursor = self.connect.cursor()

        for city in self.citylist:
            self.tablename = p.get_pinyin(city)
            self.tablename = self.tablename.replace('-','')
            self.cursor.execute('create table if not exists "{}" (name text,description text, areaName list)'.format(self.tablename))
            self.connect.commit()

            url = 'http://api.map.baidu.com/telematics/v3/travel_city?location={}&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'.format(city)
            response = urlopen(quote(url,safe= string.printable))
            responseStr = response.read()
            responseJson = json.loads(responseStr)

            for day in responseJson['result']['itineraries']:
                name = day['name']
                des = day['description']
                areaName = []

                for time in day['itineraries']:
                    for value in time['path']:
                        areaName.append(value['name'])
                self.cursor.execute('INSERT INTO "{}" (name ,description ,areaName) VALUES ("{}","{}","{}")'.format(self.tablename,name ,des ,areaName))
                self.connect.commit()

    def getInfoWith(self,info):
        daylist = ['一','二','三','四','五','六','七']
        info.time = daylist[int(info.time)-1] + '日游'
        info.city = (p.get_pinyin(info.city)).replace('-','')

        self.connect = sqlite3.connect('{}'.format(self.dbname))
        self.cursor = self.connect.cursor()

        self.cursor.execute('select * from "{}" WHERE name = "{}"'.format(info.city,info.time))
        self.connect.commit()
        result = self.cursor.fetchall()
        if len(result) == 0 :
            print('对不起，该城市没有{}项目'.format(info.time))
        else:
            print(result)

class YouKe(object):
    def __init__(self,time = '',city = ''):
        self.time = time
        self.city = city

dao = DaoYan('lvyouDB',['郑州','上海','北京','杭州','苏州'])
print(dao.citylist)
dao.getAllCityInfo()


youke = YouKe()
youke.city = input('请输入地点')
youke.time = input('请输入时间')

dao.getInfoWith(youke)
