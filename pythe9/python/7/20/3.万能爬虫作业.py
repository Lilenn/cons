import re
from urllib.request import Request,urlopen,ProxyHandler,build_opener
import random
import sqlite3
user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13'
]
ip_list = [
    '125.118.75.215:808',
    '111.155.116.225:8123',
    '123.207.30.131:80',
    '61.135.217.7:80',
    '221.228.17.172:8181'
]
# class DataManager(object):


class RYManagent(object):
    connect = None
    cursor = None
# 创建数据表
    @classmethod
    def create_info_to_table(cls):
        cls.connect = sqlite3.connect('ryDB')
        cls.cursor = cls.connect.cursor()

        cls.cursor.execute('create table if not exists ryTable (name text , age text , content text , comment text)')
        cls.connect.commit()
# 添加数据
    @classmethod
    def insert_info_to_table(cls,receiveData):
        cls.cursor.execute('insert into qsbkTable (name ,age ,content ,comment) VALUES ("{}","{}","{}","{}")'.format(receiveData[0],receiveData[1],receiveData[2],receiveData[3]))
        cls.connect.commit()
# 关闭数据库
    @classmethod
    def close_db(cls):
        cls.cursor.close()
        cls.connect.close()


class RYSpiedr(object):
    def __init__(self):
        self.base_url = 'http://www.baidu.com'
        self.headers = {
            'User-Agent':random.choice(user_agent_list)
        }
        self.proxies = {
            'http:':random.choice(ip_list)
        }

    def get_info_from_url(self):
        request = Request(self.base_url,headers=self.headers)
        proxy = ProxyHandler(self.proxies)
        opener = build_opener(proxy)
        response = opener.open(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('未能找到搜索内容',e)
        else:
            return code
    def get_page_info_from_code(self,code):
        # 输入正则 获取所需页数
        pattern = re.compile(r'',re.S)
        result1 = pattern.findall(code)
        return result1[0]
    def get_info_from_code(self,result1):
        url = self.base_url + str(result1) + '/'
        request = Request(url, headers= self.headers)
        proxy = ProxyHandler(self.proxies)
        opener = build_opener(proxy)
        response = opener.open(request)
        try:
            code = response.read().deocde()
        except Exception as e:
            print('未能找到搜索内容',e)
        else:
            return  code

    def get_need_info_from_code(self,code1):
        pattern = re.compile(r'',re.S)
        result2 = pattern.findall(code1)
        print(result2)



rySpider = RYSpiedr()
code = rySpider.get_info_from_url()
page = rySpider.get_page_info_from_code(code)
for x in range(int(page)):
    code1 = rySpider.get_info_from_code(x)
    rySpider.get_need_info_from_code(code1)


