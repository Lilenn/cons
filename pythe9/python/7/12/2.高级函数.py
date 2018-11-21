
space = '--------------'
code = 'Hello World'
print(space.join(code))
# 插入
def test(content , insert):
    print(insert.join(content))
test('今天是周四，马上是周六，好开心','!')


#----------------- -----------map reduce--------------------------------

def newMap(value):
    print(value)
# map 里边需要两个函数
# 值1.：必须是函数
# 值2. ： 序列/容器
# 作用： 将序列里面的每个元素单独放入函数中执行
# list(map)
list(map(newMap , [1,2,3,4]))
# map 的作用就依次处理序列里面的所有元素
# 和for循环非常相似
# 需求将数据表里面所有的数据前面添加一个完成时间
def changeAllData(value):
   return '完成时间：2018-8-8 ' + value
result = list(map(changeAllData , ['学习 ajaxs','学习AFnet','学习FMBB']))
print(result)
# def changeData(value):
#     pass
# changeData('学习ajaxs')


from  functools import  reduce

def newReduce(value1, value2):
    # reduce会将序列里面的所有的元素操作两次
    # 实现步骤：将任意一个值前边的两个值进行处理
    # 处理的结果再给这个值进行处理
    # 处理的结果给下一个值使用
    # 所以必须有返回值
    return  value1 + '的好朋友是' + value2
result = reduce(newReduce ,['小王','小美','小明','小张'])
print(result)

def count(index1 , index2):
    return  index1 + index2
result = reduce(count, [1,2,3,4,5])
print(result)

def test(a , *args, **kwargs):
    print(a)
    print(args)
    # kwargs必须一个关键参数，不能为字典类型
    # key = value  name = '账号三' age = 17
    print(kwargs)

# SyntaxError: positional argument follows keyword argument
# 方法里面的实参必须和 形参对应

test('张三', 17, True, '李四',{'name':'王五'},'fff团',friend= 'zhao')


content = 'print("hello world")'
print(content)
# eval  将指定的字符串当做代码处理
content = eval(content)

# 声明一个函数 可以进行任意的加减乘除运算
def myFun(content , method= '+'):
    content = method.join(content)
    print(eval(content))
myFun('123456789','-')

# 匿名函数

# 函数都是有名字的 没有名子的函数都叫做匿名函数

def test():
    pass
test()
# lambda 表示该函数为匿名函数
# 匿名函数后面的x表示接受的参数
# ：x  表示返回x
result = lambda  x :x
print(result(2))
 #上下 差不多
def test(x):
    return x
print(result(2))
# -------------------、
result= lambda  x,y : x+y
print(result(3,4))

def test(x,y):
    return  x+y
print(test(3,4))

list = [13,55,43,7,99,32]
# sorted排序 x 为里边的值  reverse = True 反序
list = sorted(list, key= lambda  x :x , reverse = True)
print(list)



# 声明方法1
# 创建一个txt文件，里面存放1000条数据，每条数据长度为10 ，包含大小写字母和数字
import  random
str = 'qwertyuiopASDFGHJKL1234567890'

f = open('数据.txt','w',encoding='utf-8')
with open('数据.txt','w',encoding='utf-8') as f:
    for index in range(1000):
        content = ''
        for x in range(10):
            char_str = random.choice(str)
            content += char_str
            print(content)
        f.write(content +'\n')
f.close()


# 声明方法2         if.os.path.exisit()
# 读取txt文件里面的所有数据，如果该条数据只有数字，那么创建一个txt文件 保存起来



# 声明方法3
# 读取txt文件里面的所有数据 如果该条数据只有字母 那么创建一个txt文件 保存起来

# 声明方法4
# 读取txt文件里面的所有数据 如果该条数据包含数字和字母 那么创建一个txt文件 保存起来





