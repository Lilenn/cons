# 内存：变量 str list（列表 可变） dict tuple（元祖  不可变）
# 文件：with open('ddd.txt','w')as f:
# 常见的存储数据的三种方式：
# 1.内存存储：变量  优点：读写速度快 缺点： 程序关闭 内存释放
# 2.文件存储：文件读写操作  优点： 数据永久 缺点：读写操作麻烦
# 数据库几位数据存储仓库
# 3.数据库存储： 数据永久 缺点：难度大

# 数据库按性质划分 有两种：
# 1.关系型数据库：数据与数据之间有着紧密的联系
#   优点：可以进行多表查询   缺点： 删除维护数据麻烦 牵一发而动全身
# 2.非关系型数据库：数据和数据之间没有联系
#    优点：对数据进行增删维护简单 缺点： 数据之间少了耦合性
#   一人吃饱 全家不饿  mongoDB redis

# 数据库按照使用规模来划分：
# 可以划分为四个等级：
# 1.大型数据库  一般用于大型商业公司 例如 淘宝 京东
#    代表 oracle
# 2.中型数据库 使用非常广泛的数据库
#    代表 SQLServer
# 3.小型数据库 一般用于小的产品公司或者公司内部数据库
#  代表 mySQL
# 4。微型数据库 经常用于移动端
#   代表 sqlite

import sqlite3
# 创建一个数据库
con = sqlite3.connect('myDB')
# 创建一个数据库光标
# 使用光标对数据进行增删改查等操作
cursor = con.cursor()
# 使用光标执行命令： 创建一张表 如果不存在的话
cursor.execute('CREATE TABLE  IF NOT EXISTS  myTable (name  text , age int )')
con.commit()
# insert into 插入数据到指定的表中  每运行一次就多条数据
cursor.execute('INSERT INTO myTable(name , age )VALUES ("Lunne" ,7)')
con.commit()
# 删除指定数据
cursor.execute('DELETE FROM myTable WHERE name = "Tom"')
con.commit()
# 更改数据  将更改的新内容放前面 被更改的旧内容放后边
# cursor.execute('UPDATE myTable SET name = "jindang" WHERE name = "Lunne"')
# con.commit()
cursor.execute('UPDATE myTable SET name = "kong" , age = 20 WHERE name ="jindang"')
con.commit()
# 查看所有数据
cursor.execute('SELECT  * FROM myTable')
# 查看第一个值
result = cursor.fetchone()
# 查看多条数据
result = cursor.fetchmany()
# 查看所有数据
result = cursor.fetchall()
print(result)