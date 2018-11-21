import sqlite3
import random
con = sqlite3.connect('phoneDB')
cursor = con.cursor()
cursor.execute("create table if not exists phone_init (brand text , price int  , memory text , function text , count int )")
con.commit()

class Customer(object):
    brand = ''
    memory = ''
    price = ''
    count = ''
    function = ''

class Seller(object):
    @classmethod
    def fullMyshop(cls):

        nameList = ['华为','小米','锤子','oppo','vivo','一加']
        memoryList = ['512M','1G','2G','4G','8G']
        priceList = ['1099','1999','2099','2499','3299','4999']
        functionList = ['美颜手机','双卡双待','超长续航','超性价比','娱乐专享','高清音质','人工智能']

        for x in range(20):
            cursor.execute('INSERT INTO phone_init (brand,price,memory ,function,count) VALUES ("{}","{}","{}","{}","{}")'.format(random.choice(nameList),random.choice(priceList),random.choice(memoryList),random.choice(functionList),random.randint(0,10)))
            con.commit()

    @classmethod
    def findPhone(cls , other):
        cursor.execute('SELECT * from phone_init WHERE brand = "{}" and price <= "{}" AND count > 0'.format(other.brand,other.price))
        con.commit()
        print(cursor.fetchall())


Seller.fullMyshop()

Customer.brand = 'vivo'
Customer.price = 2500

Seller.findPhone(Customer)
