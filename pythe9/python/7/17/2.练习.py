import sqlite3
from urllib.request import urlopen

from urllib.parse import quote

import string
import json
from prettyprinter import pprint
from xpinyin import Pinyin
p = Pinyin()

class tianQi(object):
    def __init__(self,dbname ='' , citylist = []):
        self.dbname = dbname
        self.citylist = citylist
        self.tablename = ''
        self.connect = None
        self.cursor = None

    def getAllCityInfo(self):

        self.connect = sqlite3.connect('{}'.format(self.dbname))
        self.cursor = self.connect.cursor()

        for city in self.citylist:
            self.tablename= p.get_pinyin(city)
            self.tablename = self.tablename.replace('-','')
            self.cursor.execute('CREATE TABLE IF NOT EXISTS "{}" (high text , low text , date text)'.format(self.tablename))
            self.connect.commit()

            url = 'https://www.apiopen.top/weatherApi?city="{}"'.format(city)
            response = urlopen(quote(url,safe=string.printable))
            responseDate = response.read()

            responseJson = json.loads(responseDate)

            for dict in responseJson['data']['forecast']:
                 day = dict['date']
                 high = dict['high']
                 low = dict['low']

            self.cursor.execute('INSERT INTO "{}" (high, low , date) VALUES ("{}","{}","{}")'.format(self.tablename,high , low , day))
            self.connect.commit()

yuan = tianQi('tianqiDB',['洛阳','周口','信阳','驻马店','开封','商丘','南阳'])
print(yuan.citylist)
yuan .getAllCityInfo()







