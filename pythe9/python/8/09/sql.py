
# pymysql内置sql函数 与mySQL相连
# pymysql是与python3相匹配的mysql工具
# 在python2里面 需要使用MySQLdb
# 端口号必须为数字
import pymysql
# Unknown database 'pythond'" 未知的数据库
# 在写这句代码的时候 要确保 SQL里面已经创建了一个数据库，数据库里面有数据表，数据表里面有字段
db = pymysql.connect(host = "localhost",user = 'root',password = '123456',db = 'pythonDB',port=3306)
cursor = db.cursor()

# 增
# sql = 'insert into pythonTable (age , name , fond) VALUES (15 , "zhaoliu","drink")'
# cursor.execute(sql)
# db.commit()
# 删
# sql = 'delete from pythonTable WHERE age= %d'
# cursor.execute(sql %(12))
# db.commit()
# 改
# sql = 'update pythonTable set name = "%s" WHERE age = "%d"'
# cursor.execute(sql % ('lisi',15))
# db.commit()
# 查
# sql = 'select * from pythonTable'
# cursor.execute(sql)
# result = cursor.fetchall()
# for row in result:
#     print('年龄是',row[0])
#     print('姓名是',row[1])
#     print('爱好是',row[2])

 # host = settings['MY_HOST']
 #        user = settings['MY_USER']
 #        pwd = settings['MY_PASSWORD']
 #        db = settings['MY_DB']
 #        port = settings['MY_PORT']
 #        c = settings['CHARSET']

