import sqlite3
import random
connect = sqlite3.connect('nameDB')
cursor = connect.cursor()
cursor.execute('create table if not exists nameTable (name text)')
connect.commit()

str ="""
赵钱孙李，周吴郑王。
冯陈褚卫，蒋沈韩杨。
朱秦尤许，何吕施张。
孔曹严华，金魏陶姜。
戚谢邹喻，柏水窦章。
云苏潘葛，奚范彭郎。
鲁韦昌马，苗凤花方。
俞任袁柳，酆鲍史唐。
费廉岑薛，雷贺倪汤。
"""
str = str.replace('，','').replace('。','').replace('\n','')
print(str)
# for x in range(1000):
#     name = ''
#     for y in range(random.randint(2,3)):
#         char = random.choice(str)
#         name += char
#     print(name)
#     cursor.execute('INSERT INTO nameTable(name) VALUES ("{}")'.format(name))
#     connect.commit()

def get_all_match_info():
    # like 是数据库进行匹配的关键字 后面为匹配的规则
    # x_ 表示找到以x开头，后面智游一位的数据
    # __多少位 就表示找到后面有几位的数据

    # cursor.execute('SELECT * FROM nameTable WHERE name LIKE "张_")
    # print(cursor.fetchall())
    # %x 表示找到所有以x结束的数据
    # cursor.execute('SELECT * FROM nameTable WHERE  name LIKE "%李"')
    # x% 表示找到所有以x开头的数据
    # cursor.execute('SELECT  * FROM nameTable WHERE  name LIKE "分%"')
    # %x% 表示找到所有包含x 的数据
    cursor.execute('SELECT * FROM nameTable WHERE  name LIKE "%花%"')
    print(cursor.fetchall())
get_all_match_info()

x = 72
i= x//10
print(i)
