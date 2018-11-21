# 作业：在控制台输入信息，程序执行不同命令：
# 控制台输入1：添加学生信息，学生所有信息需要通过控制台输入
# 控制台输入2：修改学生信息，需要在控制台指明哪个学生的信息需要修改，同时在控制台输入修改的内容
# 控制台输入3：删除学生信息，需要在控制台指明哪个学生需要被删除
# 控制台输入4：查询所有学生信息
# 控制台输入其他数字：退出查询系统

# 方法一
import sqlite3
connect = sqlite3.connect('xueXinWangDB')
cursor = connect.cursor()

cursor.execute('create table if not exists xueKong_info (name text , age int , tel int)')
connect.commit()
# 先关光标，再断链接
cursor.close()
connect.close()

def add_xueKong_info_to_table():

    name = input('请输入名字')
    age = int(input('请输入年龄'))
    tel = int(input('请输入联系方式'))
    # 重新连接到数据库
    connect = sqlite3.connect('xueXinWangDB')
    cursor = connect.cursor()

    cursor.execute('insert into xueKong_info (name ,age ,tel) VALUES ("{}","{}","{}")'.format(name ,age ,tel))
    connect.commit()
    cursor.close()
    connect.close()

# add_xueKong_info_to_table()

def delete_xueKong_info_to_table():
    name = input('请输入要删除的名字')

    connect = sqlite3.connect('xueXinWangDB')
    cursor = connect.cursor()

    cursor.execute('delete from xueKong_info WHERE name = "{}"'.format(name))
    connect.commit()
    cursor.close()
    connect.close()
# delete_xueKong_info_to_table()

def update_xueKong_info_to_table():
    select = input('请输入要执行的命令  0：修改全部内容  1：只修改名字')
    name = input('请输入要修改的名字')
    new_name = input('请输入新的名字')
    connect = sqlite3.connect('xueXinWangDB')
    cursor = connect.cursor()
    if select == '0':
        new_age = int(input('请输入年龄'))
        new_tel = int(input('请输入联系方式'))
        cursor.execute('update  xueKong_info set name = "{}",age = "{}",tel = "{}" WHERE  name = "{}"'.format(new_name,new_age,new_tel))
    elif select =='1' :
        cursor.execute('update  xueKong_info set name = "{}" WHERE name = "{}"'.format(new_name ,name))
    else:
        print('命令无效')
    connect.commit()
    cursor.close()
    connect.close()
# update_xueKong_info_to_table()

def get_xueKomn_info_to_table():
    connect = sqlite3.connect('xueXinWangDB')
    cursor = connect.cursor()

    cursor.execute('select * from xueKong_info')
    result = cursor.fetchall()
    print(result)
    connect.commit()
    cursor.close()
    connect.close()
# get_xueKomn_info_to_table()

while True:
    value = int(input('请输入要执行的命令'))

    if value == 1:
        add_xueKong_info_to_table()
    elif value == 2:
        update_xueKong_info_to_table()
    elif value == 3:
        delete_xueKong_info_to_table()
    elif value == 4:
        get_xueKomn_info_to_table()
    else:
        print('退出系统')
        break

# 方法二、

