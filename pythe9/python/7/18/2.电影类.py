import sqlite3
from urllib.request import urlopen
import json

class Movie(object):
    def __init__(self):
        self.connect = None
        self.cursor = None
        self.url = ''
    def getHotInfo(self):
        self.connect = sqlite3.connect('movieDB')
        self.cursor = self.connect.cursor()

        url = 'https://api.douban.com/v2/movie/in_theaters'

        response = urlopen(url)

        responseStr = response.read()

        responseDic = json.loads(responseStr)

        print(responseDic)
        self.cursor.execute('create table if not exists hotTable(title text , average text , year text , castName text)')

        for movieDic in responseDic['subjects']:
            title = movieDic['title']
            average = movieDic['rating']['average']
            year = movieDic['year']
            castLise = []
            for castDic in movieDic['casts']:
                castLise.append(castDic['name'])
            self.cursor.execute('insert into hotTable (title,average,year,castName) VALUES ("{}","{}","{}","{}")'.format(title,average,year,castLise))
            self.connect.commit()

    def getMovieWith(self,info):
        self.connect = sqlite3.connect('movieDB')
        self.cursor = self.connect.cursor()

        self.cursor.execute('select * from hotTable WHERE castName LIKE "%{}%"'.format(info))
        self.connect.commit()
        result = self.cursor.fetchall()
        if result:
            print(result)
        else:
            print('该演员暂无电影')

m = Movie()
m.getHotInfo()
m.getMovieWith(input('你喜欢哪个演员的电影'))