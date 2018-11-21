# 天气类接口
import sqlite3
from urllib.request import urlopen
from urllib.parse import quote
import string
import json
from xpinyin import Pinyin

p = Pinyin()

class Weather(object):
    def __init__(self,citylist = []):

        self.citylist = citylist
        self.connect = None
        self.cursor = None

    def getAllInfo(self):
        # 创建/打开数据库
        self.openDB()

        for city in self.citylist:
            cityName = p.get_pinyin(city).replace('-','')

            self.cursor.execute('create table if not exists "{}" (day text ,high text , low text)'.format(cityName))
            self.connect.commit()

            url = 'https://www.apiopen.top/weatherApi?city={}'.format(city)
            # 获取的是响应对象
            response = urlopen(quote(url , safe= string.printable))
            # 获取相应对象的文本内容
            responseStr = response.read()
            # 将文本转化成字典
            responseDic =json.loads(responseStr)
            # 添加昨天数据
            self.cursor.execute('insert into "{}" (day ,high ,low) VALUES ("{}","{}","{}")'.format(cityName,responseDic['data']['yesterday']['date'],responseDic['data']['yesterday']['high'],responseDic['data']['yesterday']['low']))
            # 添加今天及以后的数据
            for otherDate in responseDic['data']['forecast']:
                self.cursor.execute('insert into "{}" (day , high ,low ) VALUES ("{}","{}","{}")'.format(cityName,otherDate['date'],otherDate['high'],otherDate['low']))
                self.connect.commit()


    def getInfoWith(self,info):
        info['city'] = p.get_pinyin(info['city']).replace('-','')
        self.openDB()

        # 模糊查询
        self.cursor.execute('select * from "{}" WHERE  DAY LIKE "%{}%"'.format(info['city'],info['time']))
        self.connect.commit()
        result = self.cursor.fetchall()
        if result:
            print(result)
        else:
            print('暂无相关信息')

    def openDB(self):
        self.connect = sqlite3.connect('weatherDB')
        self.cursor = self.connect.cursor()
    def closeDB(self):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()


w = Weather( ['郑州','洛阳','开封','南阳','商丘','驻马店','周口','平顶山'])
w.getAllInfo()

dic = {}
dic['city'] =input('你想查询哪个城市')
dic ['time'] = input('你想查询哪一天')

w.getInfoWith(dic)