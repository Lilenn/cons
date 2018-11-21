# 一女子择偶，两个男士被选择
# 1.如果两男存款少于100万 都不考虑
# 2.如果两男存款大于1000万 跟存款多的走
# 3.男士
# 4.选择个子高的
# 5.如果个子都大于170 且相差不到5cm 看颜值（0,10）
# 6.低于7分的直接pass 高于7分选择颜值高的，如果相差不到2，看房子
# 7.房子不能低于100平且价值不能少于200万 如果都有的话 选择价值高的
#    价值相差不多的，看车子
# 8.车子价值不能少于50万 相差不到10万 抛硬币
# 使用继承
# 传入两个对象

# def 抛硬币()


class Person(object):
    def __init__(self,name='',sex='',salary='',height='',yanzhi='',house_area='',house_value='',car_value=''):
        self.name = name
        self.sex = sex
        self.salary = salary
        self.height = height
        self.yanzhi = yanzhi
        self.house_area = house_area
        self.house_value = house_value
        self.car_value = car_value
    def sexIsFit(self,othres):
        if self.sex == False and self.sex == othres.sex:
            print('都是女的，对不起了')
            return False
    def salary(self,Man1,Man2):
        if Man1.salary <1000000 and Man2.salary <1000000:
            print('你们太穷了')
            return False
        elif Man1.salary > 10000000 and Man2.salary >10000000 :
            print('看谁存款多喽')
        else:
            pass
    def height(self,others):
        if others.height < 170 :
            print('谁高跟谁走')
        else:
            pass
class Man1(Person):
    def __init__(self,name='',sex='',salary='',height='',yanzhi='',house_area='',house_value='',car_value=''):
        super(Man1, self).__init__(name,sex,salary,height,yanzhi,house_value,house_area,car_value)


