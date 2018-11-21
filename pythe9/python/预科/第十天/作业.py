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

import sqlite3
con = sqlite3.connect('myPhone')
cursor = con.cursor()
cursor.execute(('CREATE TABLE IF NOT EXISTS shuju(name test,money int,number int,yele test,memory int,inculb int,cunhuo int)'))
con.commit()

# cursor.execute('INSERT INTO shuju(name,money,number,yele,memory,inculb,cunhuo)VALUES("vivoX20","3299","20000","好","128GB","7.20","0")')
# con.commit()

cursor.execute('SELECT * FROM shuju WHERE cunhuo')
result = cursor.fetchall()
print(result)

class costomer(object):
    def __init__(self,demand='',consumption=''):
        self.demand = demand
        self.consumption = consumption

class salesman(object):
    def __init__(self,cunhuo='',find=''):
        self.cunhuo = cunhuo
        self.find = find


