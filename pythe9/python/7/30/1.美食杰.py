
import requests
import xlwt
from bs4 import BeautifulSoup
import sqlite3
from fake_useragent import UserAgent

class MeiShiDB(object):
    connent = None
    cursor = None

    def openDB(self):
       self.connent = sqlite3.connect('meishiDB')
       self.cursor = self.connent.cursor()
       self.cursor.execute('create table if not EXISTS MeiShiTable (name text ,src text)')
       self.connent.commit()
    def add_info_db(self,name , src):
        self.cursor.execute('insert into MeiShiTable (name , src) VALUES ("{}","{}")'.format(name,src))
        self.connent.commit()
    def close_db(self):
        self.cursor.close()
        self.connent.close()
class MeiShiJie(object):
    def __init__(self):
        self.headers  =UserAgent()
        self.DB = MeiShiDB()
    def start_load(self):
        # 打开创建数据库和数据表
        self.DB.openDB()
        code = self.get_code_with_url('https://www.meishij.net/chufang/diy/')
        self.DB.close_db()
    def get_code_with_url(self,url):
        headers = {
            'User-Agent':self.headers.random
        }
        # print(headers)
        response = requests.get(url,headers = headers).text
        code = BeautifulSoup(response,'lxml')
        self.get_content_with_code(code)

    def get_content_with_code(self,code):
        divList = code.select('div.listtylel')
        print(divList)
        for div in divList:
            # a标签后面是href img后面为src source
            img_alt = div.select('img')[0]['alt']
            img_src = div.select('img')[0]['src']
            self.DB.add_info_db(img_alt,img_src)
        self.get_next_page_with_code(code)
    def get_next_page_with_code(self,code):
        next_url = code.select('a.next')
        if len(next_url) ==0 :
            print('最后一页')
            return
        self.get_code_with_url(next_url[0]['href'])

meishi = MeiShiJie()
meishi.start_load()