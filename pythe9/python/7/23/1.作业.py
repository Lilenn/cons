# request
# connect
# manager
# commit
# close
# execute
# 在。。。内部 inside
# 在。。。外部 outside
# load
# open
# 主机 host
# response
# 寻找search


import sqlite3
import re
from urllib.request import Request,urlopen
# 目的：获取贴吧的内容存入到数据库和txt
# 1.获取网页内容
#   A.拼接url （拼接第一页以后要获取一共多少页）
#       1. 注意url规律
#   B.拼接后获取玩野源码code
#       2.用不用代理ip User-Agent   注意源码内容
#   c.分离数据 （pattern）
#         3.注意源码中是否有该数据  正则
#   D.存储到数据库
#         4.是否连接到数据库  光标是否初始化  数据库的格式
#   E。如果数据属于楼主， 则同时存储到txt
#        5.'w', 'a', 'r'

class DBManager(object):
    connect = sqlite3.connect('TieBa')
    cursor = connect.cursor()
    @classmethod
    def create_table(cls):
        cls.cursor.execute('create table if not exists tiebaTable (name text , content text)')
        cls.connect.commit()

    @classmethod
    # receive接收
    def insert_into_table(cls,receive_name , receive_content):
        cls.cursor.execute('insert into tiebaTable (name , content) VALUES ("{}","{}")'.format(receive_name,receive_content))
        cls.connect.commit()

    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.connect.close()
# 数据管理
class DataManager(object):
    def __init__(self):
        self.code = ''
    # 获取总页码数
    def get_total_page(self,code):
        # 注意: 代码执行到这里的时候self.code 就被赋值了
        self.code = code
        pattern =re.compile(r'<span class="red">(.*?)</span>',re.S)
        result = pattern.findall(code)[0]
        # 将result的值返回给 调用get_total_page 方法的对象
        return  result

    def get_name_and_content(self):
        pattern  =re.compile(r'<a.*?class="p_author_name.*?".*?>(.*?)</a>.*?<div.*?class="d_post_content j_d_post_content.*?">(.*?)</div>',re.S)
        result = pattern.findall(self.code)
        print(result)
        space_content  = re.compile(r'\s',re.S)
        italic_content = re.compile(r'\u3000',re.S)
        # 去除任意标签
        br_content = re.compile(r'<.*?>',re.S)
        for name , content in result:
            # 去除换行符
            name = name.strip('\n')
            # 去除空格
            name = re.sub(space_content,'',name)
            name = re.sub(italic_content,'',name)
            name = re.sub(br_content,'',name)

            content = content.strip('\n')
            content = re.sub(space_content,'',content)
            content = re.sub(italic_content,'',content)
            content = re.sub(br_content,'',content)

            DBManager.insert_into_table(name , content)

            if name == '恶人能活一世纪':
                with open('ck.txt','a',encoding='utf-8') as f:
                    f.write('{}'.format(content) + '\n')
                f.close()




class tieBaSpider(object):
    def __init__(self):
        self.base_url = 'https://tieba.baidu.com/p/4685013359?pn='
        self.headers  ={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        # 将数据管理作为自己的属性
        self.dataMananger = DataManager()
        self.total_paga = '1'
        self.current_page = 1
    def start_spider(self,pageIndex):
        url = self.base_url + str(pageIndex)
        # 拼接url 以及headers
        request = Request(url,headers=self.headers)
        # 获取响应内容
        response = urlopen(request)
        # 读取获取内容并解码
        result = response.read().decode()
        # 将所有的数据传给dataManager 对象的 get_total_page方法
        # 如果代码中要调用其他方法 那么先执行其他方法里面的代码
        # 然后在回到这里执行代码
        self.total_paga=self.dataMananger.get_total_page(result)
        # 代码执行到这里， 获取源码 分离数据 存入数据库已经完成
        self.dataMananger.get_name_and_content()

        if self.current_page <int(self.total_paga):
            self.current_page +=1
            self.start_spider(self.current_page)

DBManager.create_table()
tieBa = tieBaSpider()
tieBa.start_spider(1)
DBManager.close()

# for username in user_list:
#     print(username)
    # if username == '乔深沉':
    #     with open('知更鸟.txt', 'a', encoding='utf-8') as f:
            # f.write('{}'.format(content))