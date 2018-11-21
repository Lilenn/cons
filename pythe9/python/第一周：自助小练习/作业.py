
# 作业：在控制台输入信息，程序执行不同命令：
# 控制台输入1：添加学生信息，学生所有信息需要通过控制台输入
# 控制台输入2：修改学生信息，需要在控制台指明哪个学生的信息需要修改，同时在控制台输入修改的内容
# 控制台输入3：删除学生信息，需要在控制台指明哪个学生需要被删除
# 控制台输入4：查询所有学生信息
# 控制台输入其他数字：退出查询系统
# 方法一：
import sqlite3
connect = sqlite3.connect('myStudentDB')
cursor = connect.cursor()
cursor.execute('create table if not exists myStudent_info (name text , age int , tel int)')
connect.commit()
cursor.close()
connect.close()

def add_myStudent_info_to_table():
    name = input('请输入名字')
    age = int(input('请输入年龄'))
    tel = int(input('请输入联系方式'))
    connect = sqlite3.connect('myStudentDB')
    cursor = connect.cursor()
    cursor.execute('insert into myStudent_info (name , age , tel) values ("{}","{}","{}")'.format(name , age , tel))
    connect.commit()
    cursor.close()
    connect.close()
# add_myStudent_info_to_table()

def delete_myStudent_info_to_table():
    name = input('请输入要删除的名字')
    connect = sqlite3.connect('myStudentDB')
    cursor = connect.cursor()
    cursor.execute('delete from myStudent_info WHERE name ="{}"'.format(name))
    connect.commit()
    cursor.close()
    connect.close()
# delete_myStudent_info_to_table()

def update_myStudent_info_to_table():
    connect = sqlite3.connect('myStudentDB')
    cursor = connect.cursor()
    select = int(input('请输入要执行的命令'))
    name = input('请输入要修改的名字')
    new_name = input('请输入新的名字')
    if select ==0:
        new_age = int(input('请输入新的年龄'))
        new_tel = int(input('请输入新的联系方式'))
        cursor.execute('update myStudent_info set name = "{}",age = "{}",tel = "{}" where name = "{}"'.format(new_name,new_age,new_tel,name))
    elif select ==1:
        cursor.execute('update myStudent_info set name ="{}" where name = "{}"'.format(new_name,name))
    connect.commit()
    cursor.close()
    connect.close()
# update_myStudent_info_to_table()
def get_myStudent_info_to_table():
    connect = sqlite3.connect('myStudentDB')
    cursor = connect.cursor()
    cursor.execute('select * from myStudent_info')
    connect.commit()
    print(cursor.fetchall())
    cursor.close()
    connect.close()
# get_myStudent_info_to_table()

print("""
学生信息管理系统;
控制台输入1：添加学生信息
控制台输入2：修改学生信息
控制台输入3：删除学生信息
控制台输入4：查询所有学生信息
控制台输入其他数字：退出查询系统
""")

while True:
    value = int(input('请输入要执行的命令'))
    if value == 1:
        add_myStudent_info_to_table()
    if value == 2:
        update_myStudent_info_to_table()
    if value == 3:
        delete_myStudent_info_to_table()
    if value == 4:
        get_myStudent_info_to_table()
    else:
        print('退出系统')
        break




# 甲乙丙三人玩找七游戏，从甲开始，甲说任意一个数，乙在此基础上加1，丙加2，依次类推，
# 如果如果谁轮到了7的倍数或者包含7的数字，那么这个人需要将这个数字
# 保存起来，一直到100结束，最后统计每个人分别保存的数字的总和。
# 要求：使用类和对象方式来完成

# num = int(input(' 请输入一个数值'))
# yi = num+1
# bing = yi+2