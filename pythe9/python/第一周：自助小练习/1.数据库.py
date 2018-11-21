 # 新建一个数据库 ，里面有一个数据表
# 1.要求有这些字段
#    手机牌子
#    手机价格
#    手机数量
#    手机进货日期
#    手机内存
#    手机功能（yele）
#    手机存货量
# 2.可以根据手机的任意属性查询当前手机的存货量
#    如果手机数量不足，提示存货
#
#
# 新建一个对象，顾客
# 新建一个对象，售货员，售货员必须有部分手机存量为0
# 顾客有一个属性，叫做需求，消费能力
# 售货员根据顾客需求，在数据库中查找相应的手机
#  并将所有的结果返回给顾客，如果找不到指定手机则提示
#
# import sqlite3
# import random
#
# con = sqlite3.connect('myDB')
# cursor = con.cursor()
#
# cursor.execute('CREATE TABLE IF NOT EXISTS my_phone (brand text , price int , memory int , function text , count int)')
# con.commit()
#
# class Customer(object):
#     brand = ''
#     price = ''
#     memory = ''
#     function = ''
#     count = ''
#
# class Seller(object):
#     @classmethod
#     def fullMyShop(cls):
#         namelist = ['华为','小米','vivo','oppo','一加','美图','黑鲨']
#         memorylist = ['1GB','2GB','4GB','8GB']
#         pricelist = ['1799','1999','2299','2499','2899','3299','4599','4899','6899']
#         functionlist = ['商务制定','美颜拍照','游戏定制','人工智能','未来科技','性能怪兽','全面屏']
#
#         for x in range(20):
#             cursor.execute('INSERT INTO my_phone(brand, price, memory, function, count) VALUES ("{}","{}","{}","{}","{}")'.format(random.choice(namelist),random.choice(pricelist),random.choice(memorylist),random.choice(functionlist),random.randint(0,10)))
#             con.commit()
#
#     @classmethod
#     def findPhone(cls,other):
#         cursor.execute('SELECT *FROM my_phone WHERE brand ="{}" and price<="{}"  and count > 0 '.format(other.brand, other.price))
#         con.commit()
#         print(cursor.fetchall())
#
#
#
# Seller.fullMyShop()
#
# Customer.brand = '华为'
# Customer.price = 2900
#
# Seller.findPhone(Customer)


# 创建数据库的流程及其操作
# 1.创建数据
import sqlite3
# 连接数据库 创建光标
con = sqlite3.connect('myOB')
cursor = con.cursor()
# 创建数据表
cursor.execute('CREATE TABLE IF NOT EXISTS my_list(name test , age int , fond test )')
con.commit()
# 填充数据  每run 一次 就会添一条数据 所以要注意
# cursor.execute('INSERT INTO my_list(name ,age ,fond) VALUES ("嘿那达", 18 , "内向又厉害")')
# con.commit()
# 改数据  set name 放的是更改成的内容  where name 放的是原先的内容
cursor.execute('UPDATE my_list SET name = "卡卡西",age = 25 WHERE name = "嘿那达"')
con.commit()
# 查找数据
cursor.execute('SELECT  * FROM my_list')
con.commit()
fetch = cursor.fetchall()
# many ()里面是需要查询的数据的个数
result = cursor.fetchmany()
# result = cursor.fetchone()
print(result)
# 删除数据
cursor.execute('DELETE FROM my_list WHERE age>19')
con.commit()
# 删除整个数据
# cursor.execute('DELETE FROM my_list')
# con.commit()
