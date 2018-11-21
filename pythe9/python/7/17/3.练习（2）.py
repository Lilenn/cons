from urllib.request import urlopen
from urllib.parse import quote
import string
import json

from xpinyin import Pinyin
p = Pinyin()
import sqlite3

class Film(object):
    def __init__(self,dbname = '',movieslist = [] ):
        self.dbname = dbname
        self.movieslist = movieslist
        self.tablename = ''
        self.connect = None
        self.cursor = None
    def getFlimInfo(self):

        self.connect = sqlite3.connect('{}'.format(self.dbname))
        self.cursor = self.connect.cursor()

        for movie in self.movieslist:
            self.tablename = p.get_pinyin(movie)
            self.tablename = self.tablename.replace('-','')

            self.cursor.execute('create table if not exists "{}"(name text , actor text , pingfen int , nianfen int'.format(self.tablename))
            self.connect.commit()

            url = 'https://api.douban.com/v2/movie/in_theaters'

            response = urlopen(quote(url,safe=string.printable))

            responseStr = response.read()
            responseJson = json.loads(responseStr)

            for dict in responseJson['subjects']:
                print(dict['title'])
                print(dict['year'])
                for actor in dict['casts']:
                     print(actor['name'])

dianying = Film()
print(dianying.movieslist)
dianying.getFlimInfo()


