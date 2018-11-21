from urllib.request import urlopen
from urllib.parse import quote


from xpinyin import Pinyin
p = Pinyin()
import sqlite3

class DaoYou(object):
    def __init__(self,dbname = '', citylist = []):
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

            self.cursor.execute('create table if not exists "{}"(name txt , description text , areaName list)'.format())
