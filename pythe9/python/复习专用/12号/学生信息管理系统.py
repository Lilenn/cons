import sqlite3

class Student(object):
    def __init__(self,name="",age="",tel=""):
        self.name = name
        self.age = age
        self.tel = tel

class DBAction(object):
    def __init__(self,dbName="",tableName=""):
        self.dbName = dbName
        self.tableName = tableName

        self.connect = None
        self.coursor = None

    def createDBAndTable(self):
            self.connect = sqlite3.connect("{}".format(self.dbName))
            self.coursor = self.connect.cursor()
            self.coursor.execute('create table if not exists "{}" (name text ,age text ,tel text)'.format(self.tableName))
    def Close(self):

            self.coursor.close()
            self.connect.close()

    def openDB(self):
            self.connect = sqlite3.connect('{}'.format(self.dbName))
            self.coursor = self.connect.cursor()

    def addNewStudentToTable(self,student):
            self.openDB()
            self.coursor.execute('insert into "{}" (name ,age,tel) values ("{}","{}","{}")'.format(self.tableName,student.name,student.age,student.tel))
            self.connect.commit()
            self.Close()

    def deleteStudentToTable(self,name):
            self.openDB()
            self.coursor.execute('delete from "{}" where  name ="{}"'.format(self.tableName,name))
            self.connect.commit()
            self.Close()

    def updateStudentToTable(self):
            self.openDB()
            select = input('请输入您想要的操作：0，全部修改；1，修改名字')
            name = input('请输入您要更新的名字：')
            new_name = input('请输入新的名字：')
            if select == '0':
                new_age = input('请输入新的年龄：')
                new_tel = input('请输入新的凉席方式：')
                self.coursor.execute('update "{}" set name ="{}" ,age ="{}",tel ="{}" where name="{}"'.format(self.tableName,new_name,new_age,new_tel,name))
            elif select == '1':
                self.coursor.execute('update "{}" set name="{}" where name="{}"'.format(self.tableName,new_name,name))
            self.connect.commit()
            self.Close()

    def getStudentToTable(self):
            self.openDB()
            self.coursor.execute('select * from "{}"'.format(self.tableName))
            self.connect.commit()
            print(self.coursor.fetchall())
            self.Close()

myDB = DBAction("DBAction","tableAction")
myDB.createDBAndTable()

while True:


    value = input("""
        请输入操作：
        1.增加学生信息
        2.删除学生信息
        3.修改学生信息
        4.查看学生信息
    """)
    value = int(value)

    if value == 1:
        name = input('请输入姓名：')
        age = input('请输入年龄：')
        tel = input('请输入联系方式：')
        student = Student(name,age,tel)

        myDB.addNewStudentToTable(student)

    elif value == 2:
        name = input('请输入需删除的学生姓名：')
        myDB.deleteStudentToTable(name)

    elif value == 3:
        myDB.updateStudentToTable()

    elif value == 4:
        myDB.getStudentToTable()

    else:
        print('退出程序')
        break