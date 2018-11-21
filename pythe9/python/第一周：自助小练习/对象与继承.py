# 1.男生女生都属于人类， 有身高，性别，年龄，姓名等属性
# 2.创建一个男生，叫张生，包括其他一些属性
# 3.创建一个女生，叫崔莺莺，包括其他一些属性
# 4.女生来判别男生，如果是男的，年龄相差不超过5岁，身上没有负债
#   则愿意在一起
class Houman(object):
    def __init__(self,name = '', age = 0,sex =False ,height = 170,money =1000):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.money = money

    def isFitMe(self,other):
        if self.sex == other.sex:
            print('同性相斥')
            return
        if self.height > other.height:
            print('身高不合适')
            return
        if self.age - other.age > 5 or self.age - other.age < -5:
            print('年龄不合适')
            return
        if other.money < 0:
            print('都养不活自己')
            return
        print('喜结良缘')

cuiYingYing = Houman('崔莺莺', 22 ,False ,165, 10000 )
zhengSheng = Houman('郑生',23 ,True ,175 , 10000)
cuiYingYing.isFitMe(zhengSheng)


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
# 5.男方房子面积不能少于120，总价值不能少于200W
class Houman(object):
    def __init__(self,name = '',age = '',sex = '',yaowei = '',height = '',):
        self.name = name
        self.age = age
        self.sex = sex
        self.yaowei = yaowei
        self.height = height
    def sexIsFit(self,other):
        if self.sex ==True and self.sex == other.sex:
            print('我不搞基')
            return False
        if self.sex == False and self.sex == other.sex:
            print('都是小姐姐，算了吧')
            return False
    def ageIsFit(self,other):
        if self.age ==True and self.age < other.age:
            print('小姐姐你太大了')
            return False
        if self.age == False and self.age >other.age:
            print('弟弟你太小')
            return False
class Man(Houman):
    def __init__(self,name='',age='',height='',yaowei='',salary='',house_area='',house_value='' ):
        self.salary = salary
        self.house_arae = house_area
        self.house_value = house_value
        super(Man,self).__init__(name ,age ,height,yaowei)
    def makeFriendWithGril(self,other):
        result = super(Man,self).sexIsFit(other)
        if result == False:
            return
        result = super(Man,self).ageIsFit(other)
        if result == False:
            return
        if other.height < 165:
            print('身高不行')
            return
        if other.yaowei > self.yaowei:
            print('你太胖了')
            return
        if other.readcount < 100:
            print('思想浅薄')
            return
        else:
            print('跟我走吧，小姐姐')

class Woman(Houman):
    def __init__(self,name ='',age= '', height = '',yaowei = '',readcunt = ''):
        self.readcount = readcunt
        super(Woman,self).__init__(name,age,height,yaowei)
    def makeFriendWithBoy(self,other):
        result = super(Woman,self).sexIsFit(other)
        if result == False:
            return
        if other.age - self.age > 10:
            print('你太嫩了')
            return
        if self.yaowei * 1.5 < other.yaowei:
            print('肥宅拒绝')
            return
        if self.height > other.height:
            print('竟然还没我高')
            return
        if other.salary < 200000:
            print('工资太少了')
            return
        if other.house_area < 120:
            print('面积太小了')
            return
        if other.house_value < 2000000:
            print('价格有点低啊')
            return
        else:
            print('男神啊')

jack = Man()
jack.sex = True
jack.age = 21
jack.height = 175
jack.yaowei = 35
jack.house_value = 3000000
jack.house_arae = 150
jack.salary = 300000

rose = Woman()
rose.age = 20
rose.sex = False
rose.height = 167
rose.yaowei = 25
rose.readcount = 300

jack.makeFriendWithGril(rose)










