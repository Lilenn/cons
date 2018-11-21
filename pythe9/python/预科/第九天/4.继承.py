# 子类继承于父类
# 子类会有父类的属性和方法
# 子类也可以重写父类的属性和方法
# 子类也可以拥有自己独有的属性和方法
class People(object):
    def __init__(self,age='77',sex=''):
       self.age =age
       self.sex =sex
    def eat(self):
        print('人类为吃而活')
    def breath(self):
        print('美国的空气如此香甜')
class Man(People):
    def __init__(self,age='',sex='',huZi=''):
        # 继承父类已有的属性
        super(Man,self).__init__(age,sex)
    def smoke(self):
        print('吸烟有害健康')
    def eat(self):
        # 继承父类的eat方法
        super(Man,self).eat()
        print('上面这句话是继承自people的，正在说的这句话才是我自己的')
class Boy(Man):
    def __init__(self):
        pass
m =Man()
print(m.age)
m.smoke()
m.eat()

# 面向对象编程的三大特点：
# 1.封装：函数
# 2.继承：子类继承父类
# 3.多态：不同对象调用同样方法  出现不同结果  就是多态
class A(object):
    def say(self):
        print('my name is A')
class B(A):
    def say(self):
        print('my name is B')
class C(A):
    def say(self):
        print('my name is C')
class D(B , C):
     pass