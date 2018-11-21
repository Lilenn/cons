# list = list()
# dic =dict

# 对象属性中凡是带下划线的，都是不想外部使用（道德上）
# 但并是说我们完全不能用
# 如果加入的是单下划线，可以通过 p1.name ='xiaozhang'这种方式使用
# 如果加入的是双下划线，可以通过p1.-People__name这种当时使用
class People(object):
    def __init__(self,name='' ,sex='',age='16' ,fond='学习'):
        self.name =name
        self._sex =sex
        self.__age =age
        self.__fond =fond
        # get set 方法
    @property
    def fond(self):
        return self.__fomd
    fond.setter
    def fongd(self,fond):
        self.__fond = fond

p =People()
p.name = '张三'
print(p.name)
print(p._sex)
p._sex ='男'
print(p._sex)
# p.__age = age
# print(p._People__age)
# p._age ='17'
# print(p._age)
# 如果有这个属性，则修改属性值
# 如果没有这个属性值，则添加
p.grilFriend ='小美'
print(p.grilFriend)


