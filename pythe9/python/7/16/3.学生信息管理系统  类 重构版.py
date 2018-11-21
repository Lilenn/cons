import sqlite3

class Student(object):
    def __init__(self,name ='',age ='',tel =''):
        self.name = name
        self.age = age
        self.tel = tel

class DBAction(object):
    def __init__(self, dbName='' , tableName=''):
        self.dbName = dbName
        self.tableName = tableName
    # 属性可以再任意地方使用
        self.connect = None
        self.cursor = None
    def createDBAndTable(self):
        self.connect = sqlite3.connect('{}'.format(self.dbName))
        self.cursor = self.connect.cursor()
        self.cursor.execute('create table if not exists "{}" (name text , age text , tel text)'.format(self.tableName))
    def commitAndClose(self):
        self.connect.commit()
        self.cursor.close()
        self.connect.close()
    def openDB(self):
        self.connect = sqlite3.connect('{}'.format(self.dbName))
        self.cursor = self.connect.cursor()

    def addNewStudentToTable(self,student):
        self.openDB()
        self.cursor.execute('insert into "{}" (name ,age ,tel ) VALUES ("{}","{}","{}")'.format(self.tableName,student.name, student.age , student.tel))
        self.commitAndClose()
    def deleteStudentToTable(self,name):
        self.openDB()
        self.cursor.execute('delete from "{}" WHERE nmae = "{}"'.format(self.tableName,name))
        self.commitAndClose()
    def updateStudentToTable(self,name):
        self.openDB()
        self.cursor.execute('update "{}" set name = "{}" WHERE name ="{}"'.format(self.tableName,name))
        self.commitAndClose()
    def getStudentToTable(self,student):
        self.openDB()
        self.cursor.execute('select * from "{}"')
        self.commitAndClose()
myDB = DBAction('DBAction','tableAction')
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
       name = input('请输入姓名')
       age = input('请输入年龄')
       tel = input('请输入联系方式')
       student = Student(name , age, tel )

       myDB.addNewStudentToTable(student)

   if value ==2:
        name = input('请输入要删除的学生信息')
        myDB.deleteStudentToTable(name)

   if value ==3:
       name = input('请输入要修改的名字')
       name = input('请输入新的名字')
       myDB.updateStudentToTable(name)

   if value == 4:
       myDB.getStudentToTable(student)
