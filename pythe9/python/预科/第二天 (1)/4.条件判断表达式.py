
# 条件判断表达式
# score 分数
# 条件判断之  if结构
score = 59
if score >= 60 :
    print('带你去海洋馆')

# 条件判断之 if else 结构
# 薪水
salary = 999
if salary >= 10000 :
    print('哎呦，不错呦')
else :
    print('努力吧')

# 条件判断表达式之  if elif 结构
salary = 400000
if salary <= 2000 :
    print('Hello ,小屌丝')
elif salary <= 4000 :
    print('Hello ，小青年')
elif salary < 8000 :
    print('Hello ，小帅哥')
elif salary < 20000 :
    print('Hello ,小老板')
elif salary < 60000 :
    print('Hello ,小土豪')

# 条件判断表达式之 if elif else结构
# 价格
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

# 总结：如果if条件判断表达式里面写了else，那么
#       这些条件有且只有一个会被执行
# 数量
# 81  '81'
# 注意：不管在input里面输入任何内容 它的类型都是字符串类型

# TypeError: '<' not supported between instances of 'str' and 'int'
# type 类型 error 错误 not 不 supported 支持 between 两者。。。之间
# instances 实例  of 在  str 字符串类型  and 和  int 整型（数字类型）
# 类型错误：不支持在字符串和数字之间使用<

count = input('请输入数量')
# 强制类型转化 :将被转化对象转化成数字类型
# ValueError: value 值   '81'  81   "hello"
# is 是；是否
# digit 数字
# 如果值为“数字”的话    '81'
if count.isdigit():
    # 转化成真正的数字
    count = int(count)
    if count > 60 :
        print('及格')
    else :
        print('不及格')
else :
    print('输入的内容格式不正确')

