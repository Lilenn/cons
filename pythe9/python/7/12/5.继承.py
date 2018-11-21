# object 祖类or超类
# 子类能够继承父类的属性和方法
class People(object):
      def __init__(self,name ,sex,age):
          self.name = name
          self.sex = sex
          self.age = age
      def eat(self):
          print('活着目的就是为了吃')
          # 函数可以为任意类型
      def makeFriendWithOtherPeople(self,other):
          print('{}想和{}交朋友'.format(self.name,other.name))


class Man(People):
    def __init__(self,name ='', sex='',age= '',huZi = ''):
        # 继承父类的属性
        super(Man,self).__init__(name,sex,age)
        self.huZi = huZi
        # 重写父类的同名方法
    def eat(self):
        # 继承父类的方法
        super(Man,self).eat()
        print('我张三丰饿死也不吃你们一口饭')
sanfeng = Man('张三丰')
print(sanfeng.huZi)
sanfeng.name = '三丰'
print(sanfeng.name)
sanfeng.eat()
damo = Man('达摩','男',148,'没有')
sanfeng.makeFriendWithOtherPeople(damo)

# 一女子择偶，两个男士被选择
# 1.如果两男存款少于100万 都不考虑
# 2.如果两男存款大于1000万 跟存款多的走
# 3.男士
# 4.选择个子高的
# 5.如果个子都大于170 且相差不到5cm 看颜值（0,10）
# 6.低于7分的直接pass 高于7分选择颜值高的，如果相差不到2，看房之
# 7.房子不能低于100平且价值不能少于200万 如果都有的话 选择价值高的
#    价值相差不多的，看车子
# 8.车子价值不能少于50万 相差不到10万 抛硬币


# 使用继承
# 传入两个对象
# def 抛硬币()
