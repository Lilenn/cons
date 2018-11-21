# class People(object):
#     # 类属性
#     count = 0
#     size = 0
#     def __init__(self,name='',age=''):
#         # 对象属性
#         self.name =name
#         self.age =age
#         # 对象方法
#     def say(self):
#         print('hai')
#
#    # class 类method 方法
#    @classmethod
# # cls  class
#     def classFun(cls):
#         print('Hello, 我是类方法')
#         # static 静态 method方法
#     @staticmethod
#     # 不需要指定self或者cls来调用
#     def method():
#         print('我是静态方法')
#
# People.classFun()
# People.method()
# p1  =People()
# p1.classFun()
# p1.method()
# 总结：任何一种类型大方法  都可以用类或者对象来调用
# ？什么时候可以使用对象方法 什么时候使用类方法和静态方法
# 1.在绝大多数情况下我们的方法都会声明成  对象方法
# 2.如果我们希望用类方法来处理这个方法，或者不希望某一个属性值不因对象
#    而改变的时候  就可以使用类方法
# 3.静态方法的使用绝大部分都可以使用实例方法挥着类方法来代替

# 统计：某一类的对象  一共被创建了多少个  想要知道投多少个对象
# class FoodTemplate(object):
#     # 一旦对象被创建会自动调用这个方法
#     # 类属性
#     count=0
#     def __init__(self):
#         print('创建了一次')
#     pass
#    @classmethod
#    def myCount(cls):
#     print('一共被创建了{}个'.format(FoodTemplate.count))
#
# yueBing = FoodTemplate()
# manTou = FoodTemplate()


# 男女相亲
# 男方对女方的要求：
# 0.对方必须是女的
# 1.女方的年龄不能比自己大
# 2.女方的腰围一定要比自己小
# 3.女方读的书不能少于100
# 4.女方身高不小于165

# 女方对男方的要求：
# 0.对方必须是男的
# 1,.对方的年龄不能比自己小不能大于10岁
# 2.对方的身高不能比自己小
# 3.对方的腰围不能超过自己的1.5倍
# 4.男方应该有稳定收入，年薪不能少于20w
# 5.男方房子面积不能少于12哦，总价值不能少于200W

class People(object):
    def __init__(self,name='',age='',sex='',yaowei='',height=''):
        self.name = name
        self.age = age
        self.sex = sex
        self.yaowei = yaowei
        self.height = height
    def sexIsFit(self,other):
        if self.sex == True and self.sex == other.sex:
            print('我是男的，但你也是男的')
            return False
        if self.sex == False and self.sex == other.sex:
            print('我是女的，但你也是女的')
            return False
    def ageIsFit(self,other):
        if self.age == False and self.age> other.age:
            print('弟弟你太小')
            return  False
        if self.age == True and self.age < other.age:
            print('姐姐你太大')
            return False
#         在此用False表示相亲失败
class Man(People):
    def __init__(self,salary='',house_arae='',house_value=''):
        super(Man,self).__init__(name='',sex='',age='',height='',yaowei='')
        self.salary = salary
        self.house_arae = house_arae
        self.house_value = house_value
    def makeFrierndWithGirl(self,other):
        result = super(Man,self).sexIsFit(other)
        if result == False:
            return
        result = super(Man,self).ageIsFit(other)
        if result == False:
            return
        if other.height<165:
            print('对不起，身高不够')
            return
        if other.yaowei>self.yaowei:
            print('我喜欢稍微瘦一点的')
            return
        if other.readCount<100:
            print('好看的皮囊和有趣的灵魂我都喜欢')
            return
        print('你是我的女神')

class Woman(People):
    def __init__(self,name='',age='',height='',sex='',yaowei='',readCount='',):
        super(Woman,self).__init__(name,age ,height ,sex,yaowei,)
        self.readCount = readCount
    def makeFriendWithBoy(self,other):
        result = super(Woman,self).sexIsFit(other)
        if result == False:
            return
        if self.age<other.age -10:
            print('你比我大了10岁')
            return
        if self.yaowei*1.5<other.yaowei:
            print('你太胖了')
            return
        if other.salary<20000:
            print('你工资太低')
            return
        if other.house_arae<120 and other.house_value<2000000:
            print('你的房子不行')
            return
        print('你是我男神')


jack = Man()
jack.sex = True
jack,age = 21
jack.height = 176
jack.yaowei = 35
jack.salary = 20000000
jack.house_arae = 130
jack.house_value = 2000000

rose = Woman(name='rose',sex=False,age=16,height=167,yaowei=25,readCount=108)

rose.makeFriendWithBoy(jack)





