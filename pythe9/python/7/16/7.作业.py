# 甲乙丙三人玩找七游戏，从甲开始，甲说任意一个数，乙在此基础上加1，丙加2，依次类推，
# 如果如果谁轮到了7的倍数或者包含7的数字，那么这个人需要将这个数字
# 保存起来，一直到100结束，最后统计每个人分别保存的数字的总和。
# 要求：使用类和对象方式来完成

import sqlite3

from urllib.request import urlopen

from urllib.parse import quote

import string
import json
from prettyprinter import pprint

url = 'http://api.map.baidu.com/telematics/v3/travel_city?location=杭州&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'
response = urlopen(quote(url,safe = string.printable))
responseData = response.read()
print(responseData)

responseJson = json.loads(responseData)
pprint(responseData)

print(responseJson['result'])


for dict in responseJson['result']['itineraries']:
    print(dict['name'])
    print(dict['description'])


url = 'http://api.map.baidu.com/telematics/v3/travel_city?location=北京&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&output=json'
response = urlopen(quote(url,safe=string.printable))
responseData = response.read()
print(responseData)

responseJson = json .loads(responseData)
print(responseData)
print(responseJson['result'])

for dict in responseJson['result']['itineraries'] :
    print(dict['name'])
    print(dict['description'])



class Customer(object):
    def __init__(self,time = '',location = ''):
        self.time = time
        self.location = location
# class Guider(object):
#     def __init__(self,find ,):

class DBAction(object):
    def __init__(self,dbName , tableName):
        self.dbName = dbName
        self.tableName = tableName
        self.connect = None
        self.cursor = None
    def createDBAndTable(self):
        self.connect = sqlite3.connect('{}'.format(self.dbName))
        self.cursor = self.connect.cursor()
        self.cursor.execute('create table if not exists "{}" (time int , location text)'.format(self.tableName))
    def commitAndClose(self):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()
    def openDB(self):
        self.connect = sqlite3.connect('{}'.format(self.dbName))
        self.cursor = self.connect.cursor()
    def addLocationAndTimeToTable(self,customer):
        self.openDB()
        self.cursor.execute('insert into "{}" (time , location) VALUES ("{}","{}")'.format(self.tableName,customer.time, customer.location ))
        self.commitAndClose()






