# https://www.qiushibaike.com/hot/page/
import re
from urllib.request import Request,urlopen
import sqlite3

class DataManagent(object):
    def updata_new_data(self,oldData):
        # 去除换行符
        name = oldData[0]
        name = name.strip('\n')
        content = oldData[2]
        content = content.strip('\n')
        # 去除<br/>
        pattern= re.compile('<br/>')
        content = pattern.sub(r'',content)

        new_Data =(name ,oldData[1],content,oldData[3])

        return new_Data

class QBManagent(object):
    connect = None
    cursor = None
# 创建数据表
    @classmethod
    def create_info_to_table(cls):
        cls.connect = sqlite3.connect('qsbkDB')
        cls.cursor = cls.connect.cursor()

        cls.cursor.execute('create table if not exists qsbkTable (name text , age text , content text , pinglun text)')
        cls.connect.commit()
# 添加数据
    @classmethod
    def insert_info_to_table(cls,receiveData):
        cls.cursor.execute('insert into qsbkTable (name ,age ,content , pinglun) VALUES ("{}","{}","{}","{}")'.format(receiveData[0],receiveData[1],receiveData[2],receiveData[3]))
        cls.connect.commit()
# 关闭数据库
    @classmethod
    def close_db(cls):
        cls.cursor.close()
        cls.connect.close()

class QSBKSpider(object):
    def __init__(self):
        self.base_url = 'https://www.qiushibaike.com/hot/page/'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

        self.dataTool = DataManagent()
    def get_info_from_url(self,index):
        url = self.base_url + str(index) + '/'
        request = Request(url,headers=self.headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('未能获取搜索内容',e)
        else:
            return code

    def get_userfull_info_from_code(self,code):
        # print(code)
        pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>.*?<div class="articleGender.*?Icon">(.*?)</div>.*?<div class="content">.*?<span>(.*?)</span>.*?<span class="stats-comments">.*?<i class="number">(.*?)</i>',re.S)
        result = pattern.findall(code)
        # print(result)

        for oldData in result:

            new_Data = self.dataTool.updata_new_data(oldData)

            QBManagent.insert_info_to_table(new_Data)

QBManagent.create_info_to_table()
qbSpider = QSBKSpider()
code = qbSpider.get_info_from_url(1)
for x in range(1,9):
    code = qbSpider.get_info_from_url(x)
    qbSpider.get_userfull_info_from_code(code)
QBManagent.close_db()
