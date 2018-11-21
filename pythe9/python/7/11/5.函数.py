
# 函数就是方法非常类似于现实生活当中的模板/模具
# 声明方法 def define 定义 test方法名称 （)内部写参数
# def test()
#     pass
0# test()
# 无参数无返回值
def firstFun():
    print('this is my frist function')
firstFun()
# 有参数无返回值  声明方法时候的参数叫做形式参数 简称形参，
# 形参没有具体的值 本身为一个变量

def secondFun(values):
    print('我喜欢{}'.format(values))
# 调用方法时候的参数 叫做实际参数 简称实参
# 实参不是变量 而是具体的值
secondFun(3)
# ---------------------局部变量 和全局变量----------------------------
# 在方法内部声明的变量叫做局部变量
# 只能在方法内部使用
# 出了这个方法就释放了
# 无参数有返回值
# return 将love 返回到方法中
def thirdFun():
    love = '游戏'
    return love
result = thirdFun()
print(result)

def fourFun():
    print('Hello')
    # return后面如果没有跟值得话，默认返回None
    # return只能写在方法里面， 不能再方法外面使用
    # 代码执行了return以后， return到方法结束之前的部分 统统不执行
    return
print('World')
fourFun()


# 无参数无返回值

# 有参数有返回值
def fiveFun(a,b):
    return  a+b
print(fiveFun(12,13))

def sixFun(a,b,c,d,e,f):

   print(e)
sixFun('a',0,[1,2,3,4,5,6],True,{'name':'张三'},(1,2,3))

# 默认参数
def myGirlFun(name,age,sex=True,born='未知'):
    print('我的女朋友是{}，年龄是{}，性别是{}，出生日期是{}'.format(name,age,sex,born))
myGirlFun('小玲',100)
myGirlFun('小王',100,True,'1918年')
myGirlFun('小黄',100,True)
# 关键参数
def myBoyFriend(name,age,sex=False,bron='未知'):
    print('我的男朋友是{}，年龄是{}，性别是{}，出生日期是{}'.format(name,age,sex,bron))
myBoyFriend('小张',100)
# 指明给哪一个参数设置值 这种参数叫做关键参参数
myBoyFriend('小寒',20, bron='1995年1月25日')

# *args参数
# argument 参数  **：指针的指针  **XXX
# *args能够将多余的参数 统统放入到自己内部
def myArgu(name,*args,**kwargs):
    print(name)
    print(type(args))
    print(args)
    print(kwargs)
myArgu('张三丰','149','武当创始人','太极剑','太极拳',friend = 'damo')

# 有多参有返回值
def retManyValue(a,b,c):
    return a ,b ,c
print(retManyValue(10,11,12) )