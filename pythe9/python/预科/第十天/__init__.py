class People(object):
    def __init__(self,name='',age='',sex='',height='',yaowei=''):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.yaowei = yaowei
    def sexIsFit(self,other):
        if self.sex == True and self.sex == other.sex
            print('同性相斥')
            return False
    def sexIsFit(self,other):
        if self.sex == False and self.sex == other.sex
            print('都是女的')
            return False
    def ageIsFit(self,other):
        if self.sex == True and self.age > other.age
            print('姐姐你太大')
            return False
        if self.sex == False and self.age < other.age
            print('弟弟你太小')
            return False

class Man(People):
    def __init__(self,name,age,sex,height,yaoewei,ysal,house,havlues):
        super(Man,self).__init__(name,age,sex,height,yaowei)
        self.house = house
        self.havlues = havlues
        self.ysal = ysal
    def makeFrientWithGril(self,other):
