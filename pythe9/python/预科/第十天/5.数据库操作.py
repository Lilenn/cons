
# 1.将数据拼接成字符串str
# 2.list
# 3.tuple
# 4.dict
# 以上方式其实是同属于一种方式即将数据存储到内存当中

# 实际再开发展过程当中，数据存储主要听有三种形式
# 1.将数据存储到内存当中
#    1.使用方便，读写速度快  2.程序关闭的时候，内存会被释放，数据会消失
# 2.将数据写入到文件当中
#    1.数据存储是永久性的，不易丢失  2.打开关闭文件，操作数据都会比较麻烦
# 3.将数据存储到数据库中
#    1.数据储存为永久性的，操作也比较方便  2.数据库学习难度比较大

# 数据库按照相纸分为两大类：
# 1.关系型数据库：数据和数据之间存在着广泛的联系 mysql  sqlite
#   1.通过一个数据可以访问到其他的数据
# 2.非关系型数据库：数据和数据之间没有联系  MongoDB redis
#   2.数据为单独的，疏计件的耦合度比较低，对数据进行增删更改不会影响到其他数据
#
#
# 数据库按照规模大小来说，分为四种：
# 1.大型数据库：oracle
# 2.中型数据库：SQlserver
# 3.小型数据库： mySQL
#
# 4.微型数据库： sqlite  大小大概只有4M左右
import  sqlite3
# databace
# 连接到一个数据库 如果数据库存在则连接
# 如果数据库不存在 则创建
con = sqlite3.connect('myDB')
# 设置数据库光标  数据库光标是用来执行数据库命令的
cursor = con.cursor()

# cursor.execute('CREATE  TABLE  IF NOT EXISTS  my_info(name text , age int , des test)')

# con.commit()


# execute 执行
# 数据库操作 增删改查
# 一个项目里面可能用到多个数据库（绝大多数情况下只有一个）
# 一个数据库里面有多张表
# 一个表里面有多个字段
# 一个字段里面有多条数据
cursor.execute('INSERT  INTO my_info (name , age , des) VALUES ("部落",17,"兽人永不为奴")')
con.commit()

# 删除数据

# cursor.execute('DELETE  FROM my_info WHERE  age >30')
# con.commit()

# 删除表中全部数据
# cursor.execute('DELETE FROM my_info')
# con.commit()

#    改数据
cursor.execute('UPDATE my_info set name="苏轼" WHERE   name="卡卡西"')
con.commit()

# 查询数据
cursor.execute('SELECT * FROM my_info')
fetch  = cursor.fetchone()
# result = cursor.fetchone()
result = cursor.fetchall()
# many()里面的数字表示获取几条数据 这时的数据记得是所有查询出来的数据
# ruslt = cuesor.fetchmany(3)
print(result)

# 慎用 删除整个表
# cursor.execute('DROP TABLE IF EXISTS my_info')
# con.commit()

# cls

