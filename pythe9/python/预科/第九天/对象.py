# 机器语言：
# 汇编语言：
# 高级语言：1：面向过程的语言 C   注重方法实现的过程
#           2：面向对象的语言 java ,oc,C++,c#,python  注重谁来执行的方法
# 类和对象   群体     个体
# 一类人，A级车，中国人
# 小A  宝骏560豫A66666  热巴
# class 类 Poeple 类名 （)里面为继承的对象
# object  对象；物体  object 相当于祖类
# 对象 有两部分
# 1.属性  名字 性别 身高 体重
# 2.方法 sleep eat cry coding
# 类相当于模板  对象相当于用模板生成的产品
class People(object):
    # 类
    name =''
    sex =''
    age =0
    height  =''
    weight =''
    def eat(self):
        print('人类出生就会吃东西')
    def sleep(self):
        print('人类天生会睡觉')
    def work(self):
        print('每个人都有劳动的权利')

#    创建一个对象  叫做p
p=People()
list= list()
dic=dict()
p.name = '小王'
p.age = 17
p.sex = False
p.height = 176
p.weight = '69kg'

print(p.height)
p.eat()
p.sleep()
p.work()


class People(object):
    # init 初始化 魔术方法的一种 用来初始化对象
    #   init方法会自动调用  在创建对象的时候
    # init里面的属性   叫做对象属性
    def __init__(self , name ,age ,sex):
        # 将后面的值赋予自己的self.XX属性
        self.name = name
        self.age = age
        self.sex = sex
    def study(self):
        print('只有学习才能使我感到快乐')
# 在创建对象的时候，直接赋值
p=People('小明',17 ,True)
print(p.name)
class Person(object ):
    # 在初始化的时候  直接给参数增加默认值
    def __init__(self , name='',age=0,sex=True):
        self.name = name
        self.age =age
        self.sex =  sex
    def isFITmySelf(self,boy):
        print('男生的性别是{}'.format(boy.sex))

# 1.男生女生都属于人类， 有身高，性别，年龄，姓名等属性
# 2.创建一个男生，叫张生，包括其他一些属性
# 3.创建一个女生，叫崔莺莺，包括其他一些属性
# 4.女生来判别男生，如果是男的，年龄相差不超过5岁，身上没有负债
#   则愿意在一起
# p2 = People(_)
p1 = Person('aaa',12,False)
# p1.isFinMYSelf(p2)




class Human(object):
   def __init__(self ,name='',age=0,sex=False,height=120 , money=0):
       self.name =name
       self.age =age
       self.sex = sex
       self.height = height
       self.money = money
   def isFitMe(self , other):
    if self.sex == other.sex:
       print('同向相斥')
       return
    if self.age - other.age > 5 or self.age - other.age < -5:
       print('年龄不合适')
       return
    if other.money < 0:
       print('无身可依')
       return
   print('喜结良缘')
cuiYingYing = Human('崔莺莺',12,False ,165 ,100000)
zhangSheng = Human ('张生',14,True,175,-1000)
cuiYingYing.isFitMe(zhangSheng)


