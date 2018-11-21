# 类：抽象 整体 全局
# 对象： 具体 个体 局部
# 对象是从累中分离出来的一个具体的个体
# 面向对象编程
# object 任何一个对象都直接或间接继承自object
# 从功能上定义：类是属性和方法的集合
# /robots.txt

class Hero(object):
    # 属性 称之为类属性
    # a,b =100,200
    blood = 700
    attact = 67
    level = 1
    # 方法
    def skill(self):
        print('致盲射击')
timo = Hero()
timo.skill()
print(Hero.blood)
print(timo.blood)

class People(object):
    # init初始化
    # 当对象创建的时候 属性的默认值
    # 魔术方法
    # 类属性
    count = 0
    # 对象创建的时候会自动调用init方法
    # 如果init方法需要参数的话
    # 那么对象在创建的时候也需要参数
    def  __init__(self,name ,age,sex):
        # 对象属性
        self.name = name
        self.age = age
        self.sex = sex
        # 对象方法
    def sleep(self):
        print('{}一天要睡十七八个小时'.format(self.name))
    def work(self):
        print('工作时间太短， 不开心')
    def fond(self):
        print('人生苦短 辛亏我甜')

zhangSan = People('张三','男','17')
zhangSan.sleep()

list = People('李四','男','17')
list.sleep()

print(People.count)
# 类属性可以通过对象来调用
print(list.count)

print(zhangSan.name)
# AttributeError: type object 'People' has no attribute 'name'
# 属性错误：People没有属性
# print(People.name)
zhangSan.work()
# TypeError: work() missing 1 required positional argument: 'self'
# 类型错误：work需要用到一个参数self
# work 方法是People里面的对象方法 self指的就是People的对象
# 所以在调用的时候 需要传入一个People的对象

People.work(zhangSan)

class Person(object):
# 如果初始化的时候设置了默认值 那么在创建对象的时候 可以不必设置参数
    def __init__(self,name= '', age ='',sex= '',fond=''):
        self.name = name
        # 属性前面加下划线 这种方式叫做私有属性
        # 也就是不想被别人访问
        # 但这种属性也不是绝对访问不了
        # 可以通过在属性前面添加下划线的方式来访问
        self._age = age
        self._sex = sex
        # 属性如果是双下划线 如果想要调用
        # 需通过p1._Person__fond这种方式调用
        self.__fond = fond

    # get set 方法
    #     property属性
    #     attribute属性
    #     arbument参数
    #     声明set get 方法的标记
    @property
    def fond(self):
        print('get方法被调用了')
        return self.__fond
    @fond.setter
    def fond(self , fond):
        print('set方法被调用了')
        self.__fond = fond

  # get 方法
p1 = Person('张三丰',149,'男','练剑')
print(p1.name)
print(p1._age)
print(p1._sex)
# AttributeError: 'Person' object has no attribute '__fond'
# 属性错误：people里面没有__fond属性
print(p1._Person__fond)
# set方法
p1.name = '张三丰'
print(p1.fond)
