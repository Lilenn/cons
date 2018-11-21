
# while后面的判断条件如果为真
# 那么里面的代码块会一直执行
# 直到程序结束或者跳出循环或者条件为假
# for 后面要填写一个循环的范围  注重自己来控制循环的次数
# while 后面要写判断的条件 注重的是条件的真假
age = 1
while age <18:
    print('未成年{}'.format(age))
    age += 1

count = 0
while True:
  count += 1
  if count >=10000:
    break
 # break  打断
  #  当循环里面执行了Break
  # 那么后面的循环都不再执行
print(count)

# break 跳出循环
# continue 跳出这一次循环，剩下的循环继续执行
# return 通常用在方法中 后面的代码统统不执行

count = 0
while count < 10:
    count += 1
    if count==4 :
        continue
    print('count为:{}'.format(count))
# SyntaxError: 'return' outside function
# return 不能再方法以外使用
# while True :
#     count += 1
#     if count == 20:
#         return
#
name = '小王'
age = '17'
# 类型错误  必须是一个字符串，不能是数字
# 解决办法：使用+拼接的时候 必须使用字符串 或者将数字转化为字符串
print('我的名字是'+ name + ',我的年龄是'+ age)


# IndentationError: unindent does not match any outer indentation level
# indent 缩进错误：未知缩进不匹配任何缩进等级
# 解决办法：TEB自动缩进
# SyntaxError: invalid syntax
#
for index in range(10):
  if name == '小王':
    print('hello')
else:
    print('nothing')




