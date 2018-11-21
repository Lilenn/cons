
# 字符串 ， 数字 ，布尔 ，列表 ，元组 ，字典

# 问题1：怎么判断输入的数字 为偶数
num = input('请输入一个整数')
num = int(num)
# 9   '9'
# TypeError: not all arguments converted during string formatting
if num % 2 == 0 :
    print('偶数')
else :
    print('奇数')

# 问题2：怎么判断一个数字既是3的倍数也是4的倍数
num = 123122
if num % 12 == 0 :
    print('既是3的倍数也是4的倍数')
else :
    print('不是3和4的倍数')

if num % 3 == 0 :
    if num %4 == 0 :
        print('是3和4的倍数')
    else:
        print('不是4的倍数')
else :
    print('不是3的倍数')

#-------------------  and 而且
if num % 3 == 0 and num % 4 ==0 :
    print('是3和4的倍数')
# 问题3 ：怎么判断一个数字是5的倍数或者是6的倍数
if num %  5 == 0 :
    if num % 6 == 0 :
        print('既是5又是6的倍数')
    else:
        print('是5的倍数不是6的倍数')
else :
    if num % 6 == 0:
        print('只是6的倍数')
    else :
        print('既不是5也不是6的倍数')

#------------ ||  or 多个条件只要一个满足就可以
if num % 5 == 0 or num % 6 ==0 :
    print('5或者6的倍数')
'''
总结 ： and和or用于多个条件需要判断的情况下，以两个条件举例
and：只要有一个条件为假，最终结果就为假
条件1    真    条件2    真     结果：真
条件1    假    条件2    真     结果：假
条件1    假    条件2    假     结果：假
or ：只要有一个条件为真，最终结果就为真
条件1    真    条件2    真     结果：真
条件1    真    条件2    假     结果：真
条件1    假    条件2    假     结果：假
'''
# 框架 ， 工具 ，包 ，插件
# 从random包中引出随机整数的方法
from random import randint
# 在0和3之间随机获得一个整数
# 计算机当中的随机数也称之为 ‘伪随机数’
# 计算机找随机数是根据计算机内部的算法来找到的
number = randint(0,3)
print(number)

user_num = input('请输入你要猜的数字')
user_num = int(user_num)
computer_num  = randint(0,3)
print(computer_num)
if(user_num == computer_num):
    print('you win')
else :
    print('you lose')


