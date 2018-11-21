import re
from urllib.request import urlopen,Request
import sqlite3

class DataManager(object):
    def updata_new_data(self,oldData):
        # 去除换行
        name = oldData[0]
        name = name.strip('\n')
        content = oldData[2]
        content = content.strip('\n')
        # 去除<br/>
        pattern = re.compile(r'<br/>')
        content = pattern.sub('',content)
        newData = (name,oldData[1],content,oldData[3],oldData[4])

        return newData

class DBManager(object):
    connect = None
    coursor = None

    @classmethod
    def create_db_and_table(cls):
        cls.connect = sqlite3.connect("qbDB")
        cls.coursor = cls.connect.cursor()
        cls.coursor.execute('create table if not exists qbTable (name text ,'
                            'age text , content text , like text ,comment text)')
        cls.connect.commit()

    @classmethod
    def insert_into_table(cls,receiveData):
        cls.coursor.execute('insert into qbTable (name,age,content,like,comment) VALUES ("{}","{}","{}","{}","{}")'.format(receiveData[0],receiveData[1],receiveData[2],receiveData[3],receiveData[4]))
        cls.connect.commit()

    @classmethod
    def close_db(cls):
        cls.coursor.close()
        cls.connect.close()

class QSBKSpider(object):
    def __init__(self):
        # 设置基本网址，基本网址为所有需要爬虫的网址的共同部分
        self.base_url = 'https://www.qiushibaike.com/hot/page/'
        # 设置爬虫的用户标识
        self.headers = {
            "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36 OPR/56.0.3051.99'
        }
        # 创建一个数据管理的实例化对象
        # 并使其作为QSBKSpider的属性
        self.dataTool = DataManager()

    def get_code_from_url(self,index):
        # 拼接完整的url
        url = self.base_url + str(index) + '/'
        # 设置请求的url的请求头信息
        request = Request(url,headers = self.headers)
        # 获取响应信息
        response = urlopen(request)
        try:
            # 读取响应信息并解码
            code = response.read().decode()
        except Exception as e:
            print('获取信息失败',e)
            return None
        else:
            return code

    def get_userfull_info_from_code(self,code):
        pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<span class="stats-vote">.*?<i class="number">(.*?)</i>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
        result = pattern.findall(code)

        for oldData in result:
            newData = self.dataTool.updata_new_data(oldData)
            DBManager.insert_into_table(newData)

DBManager.create_db_and_table()

qbSpider = QSBKSpider()
# 获取网页源码并转码
code = qbSpider.get_code_from_url(1)

for x in range(1,6):
    code = qbSpider.get_code_from_url(x)
    # 提取网页数据
    qbSpider.get_userfull_info_from_code(code)
DBManager.close_db()