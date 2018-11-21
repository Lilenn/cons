#条件判断表达式
# 条件判断之if
score=81
if score>=60:
    print('带你去海洋馆')
# 条件判断之 if else
salary=10000
if salary>=10000:
    print('哎呦，不错呦')
else :
    print('努力吧')
# 条件判断之if elif
salary = 40000
# salary 薪水
if salary<=2000:
    print('Hello,小屌丝')
elif salary<=4000:
    print('Hellow,小青年')
elif salary<8000:
    print('Hellow,小帅哥')
elif salary<20000:
    print('Hellow,小老板')
elif salary<60000:
    print('Hellow,小土豪')
# 条件判断表达之 if elif else结构
price = 28000
if price < 300 :
    print('老年机')
elif price < 1000 :
    print('千元机')
elif price < 3000 :
    print('时尚机')
elif price < 10000 :
    print('豪华机')
else :
    print('轰炸机')
# 总结：如果if条件表达式里面写了else,那么这些条件有且只有一个会被执行
# 注意：不管在input里面输入任何内容，他的类型都是字符串类型
count = input ('请输入数量')
# 强制类型转化：将被转化对象转化成数字类型
# count = int(count)
# if count < 100:
#     print('少于100')

if count.isdigit():
    count = int(count)
    if count > 60:
        print('及格')
    else :
        print('不及格')
else:
    print('输入的内容不正确')

