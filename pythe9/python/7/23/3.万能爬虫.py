
from urllib.request import Request,urlopen
import re
import sqlite3
class DBManager(object):
    connect = sqlite3.connect('okDB')
    cursor = connect.cursor()
    isOneInfo = True
    # dbData = None
    @classmethod
    def create_table(cls,info):
        if cls.isOneInfo ==True:
            cls.cursor.execute('create table if not exists spiderTable(value0 text)')
            cls.connect.commit()
        else:
            sqlStr = 'create table if not exists spiderTable('
            for index,value  in enumerate(info):
                # 'create_table if not exists spiderTable(value0 text,value1 text,value2 text)'
                sqlStr +='value' + str(index) + ' text,'
            sqlStr = sqlStr[0:-1]
            sqlStr +=')'
            cls.cursor.execute(sqlStr)
            cls.connect.commit()
    @classmethod
    def insert_into(cls,info):
        if DBManager.isOneInfo == True:
            cls.cursor.execute('insert into spiderTable (value0) VALUES("{}")'.format(info))
            cls.connect.commit()
        else:
            # 多条数据也要拼接插入
            sqlStr = 'insert into spiderTable('
            key = ''
            values = 'values('
            for index ,value in enumerate(info):
                key += 'value' + str(index) + ' ,'
                values += '"'+ info[index] + '"'+' ,'
            key = key[0:-1]
            key +=')'
            values = values[0:-1]
            values +=')'
            sqlStr += key +values
            cls.cursor.execute(sqlStr)
            cls.connect.commit()
# 数据管理
class DataManager(object):
    # 根据源码获取指定的内容
    @classmethod
    def get_info_with_code(cls,code,patternValue):
       pattern = re.compile(r'{}'.format(patternValue),re.S)
       result = pattern.findall(code)
       return result
    @classmethod
    def change_data_with(cls,oldData):
        # 如果获取的是一条数据 那么这条数据类型是字符串 会被放入到列表中
        # 如果获取的是多条数据，那么每条数据都是元祖 也会被放入到列表中
       space = re.compile(r'\s', re.S)
       element = re.compile(r'<.*?>', re.S)
       if type(oldData) == str:
            oldData = oldData.strip('\n')
            oldData = re.sub(space,'',oldData)
            oldData = re.sub(element,'',oldData)
            DBManager.isOneInfo = True
            return oldData
       else:
           list = []
           for content in oldData:
               content = content.strip('\n')
               content = re.sub(space,'',content)
               content = re.sub(element,'',content)
               list.append(content)
           DBManager.isOneInfo =False
           return list

class Spider(object):
    def __init__(self,base_url,pattern):
        self.base_url = base_url
        self.pattern = pattern
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
    def load_first_url(self):
        url = self.base_url +'1'
        request = Request(url,headers=self.headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('请求首页内容',e)
        else:
            result_list = DataManager.get_info_with_code(code,self.pattern)
            for value in result_list:
                # 字符串
                # 列表
                newData = DataManager.change_data_with(value)
                # 创建数据表
                DBManager.create_table(newData)
                # 将数据输入到数据库
                DBManager.insert_into(newData)

spider = Spider('https://www.qiushibaike.com/hot/page/','<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>')
spider.load_first_url()





