# 1.总页数     2.爬去姓名和内容    3.数据存入存数据库      4.楼主的小说内容拼接起来写入到txt中
# 按照今天上午的代码流程来写

import  re
from urllib.request import Request,urlopen
import sqlite3

class DataManager(object):
    def updata_new_data(self,oldData):
        name = oldData[0]
        name = name.strip('\n')
        content = oldData[1]
        content = content.strip('\n')
        # 去除<br/>
        pattern = re.compile(r'<br>')
        content = pattern.sub('',content)
        # 去除\u3000
        pattern = re.compile(u'\u3000')
        content = pattern.sub('',content)
        newData = (name,content)

        return newData
#
class DBManager(object):
    connect = None
    cursor = None
    @classmethod
    def create_db_and_table(cls):
        cls.connect = sqlite3.connect('tbDB')
        cls.cursor = cls.connect.cursor()
        cls.cursor.execute('create table if not exists tbTable (name text , content text)')
        cls.connect.commit()

    @classmethod
    def insert_info_to_table(cls,receiveData):
        cls.cursor.execute('insert into tbTable (name ,content) VALUES ("{}","{}")'.format(receiveData[0],receiveData[1]))
        cls.connect.commit()

    @classmethod
    def close_db(cls):
        cls.cursor.close()
        cls.connect.close()


class QSBKSpider(object):
    def __init__(self):
        self.base_url = 'https://tieba.baidu.com/p/4685013359'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        # 创建一个数据管理实体化对象datatool 并使其作为QSBKSpider 的属性
        self.dataTool = DataManager()

    def get_code_from_url(self):
        request = Request(self.base_url,headers= self.headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('获取信息失败',e)
            return None
        else:
            return code

    def get_userfull_info_from_code(self,code):
        # print(code
        pattern = re.compile(r'<span class="red">(.*?)</span>',re.S)
        result = pattern.findall(code)
        return result[0]
    def get_louzhu_info_from_code(self,result):
        full_url = self.base_url +'?pn='+ str(result)+'/'
        request = Request(full_url,headers=self.headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('获取信息失败',e)
            return None
        else:
            return code
    def get_full_from_code(self,code1):
        pattern = re.compile(r'<li class="d_name".*?>.*?<a.*?>(.*?)</a>.*?<cc>.*?<div.*?class="d_post_content.*?j_d_post_content.*?">(.*?)</div>',re.S)
        result1 = pattern.findall(code1)
        # print(result1)

        for oldData in result1:
         # oldData为元祖（年龄，内容）
         # 更新旧值 得到新的值
            newData = self.dataTool.updata_new_data(oldData)
            print(newData)

            DBManager.insert_info_to_table(newData)

DBManager.create_db_and_table()

tbSpider = QSBKSpider()
code = tbSpider.get_code_from_url()
y= tbSpider.get_userfull_info_from_code(code)
for x in range(int(y)):
    code1 = tbSpider.get_louzhu_info_from_code(x)
    tbSpider.get_full_from_code(code1)

DBManager.close_db()
