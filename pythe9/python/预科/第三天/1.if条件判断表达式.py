
age = 10
name ='小明'
if age < 4 :
    print('幼儿')
if age < 12 :
    print('儿童')
if age < 18 :
    print('青少年')
if age < 25 :
    print('青年')

if age < 100 :
    print('少于100')
else :
    print('大于100')

if age < 10 :
    print('age')
if name == '小明':
    print('小明')

# 局部变量  影响部分代码 在部分代码中有效
# 全局变量  在全部代码中都有效

if age < 5 :
    info = '小学生'
    print(info)
else :
    # is not defined
    # XXX 未定义：使用了一个没有的东西
    print(info)