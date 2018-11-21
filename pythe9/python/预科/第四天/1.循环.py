
# 布尔值  值只能为真假
isOk = False
if isOk == False:
    print('ok')
else :
    print('no ok')

for  x in range(10):
    print(x)

# while 当.....的时候
age = 0
# 重点：在于控制循环的次数
for x in range(18):
    # print('x={}'.format(x))
    x += 1
# 重点：在于循环的条件 只要条件为真 就一直循环
# for循环做的事情 while都能做 反之就不行
# 获取现在的时间函数  获取12点的时间函数
# 绝大部分情况下 我们用for
while age < 18 :
    # print('未成年，今年{}岁了'.format(age))
    age += 1

# break
index = 1
while index < 10 :
    index += 1
    if index == 4 :
        # break  后面的循环统统不执行
        # continue  当次循环不执行 后面的继续执行
        # 当前位置没有东西可写 防止代码报错
        # 用pass进行站位
        # 这样
        # 代码就不会报错 pass无任何意义
        pass
    print(index)
