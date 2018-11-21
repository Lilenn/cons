
# for(int index  = 0 ; index < 10 ;index ++)
# {
#     循环；迭代
# }
# for in结构  index索引 range 范围
# range后面一个值
# 表示代码循环的次数
for index in range(10):
    print('老婆，我错了')
    print(index)

# 值1：循环开始的位置
# 值2：循环结束的位置
for index in range(50 ,100):
    print(index)

# 值1：循环开始的位置
# 值2：循环结束的位置
# 值3：增量
for index in range(50 ,100 ,5):
    print(index)

num = 100
num = num + 100
num += 100
print(num)

# 问题：获取1~100之间所有数字的和
sum = 0
for x  in range(1,101):
    sum = sum + x
    print('x=%s'% x)
print(sum)

# 问题2：获取1~100之间所有奇数之和与5的倍数之和的差
ji_he = 0
bei_he = 0
for index in range(1 , 101):
    if index % 2 == 1 :
        ji_he = ji_he + index
    if index % 5 == 0:
        bei_he = bei_he + index
print(ji_he - bei_he)

# 石头剪子布 小程序  三局两胜制
from random import randint
user_win = 0
compunter_win = 0
deuce = 0
# index 代表标号  value代表值
# for index ,value in enumerate('Hello wolrd'):
for index ,value in enumerate(range(3)):

    user_num = input('请输入数字')
    user_num = int(user_num)
    computer_num = randint(0 , 2)

    if user_num -computer_num == -1 or user_num -computer_num == 2:
        print('第{}局玩家胜'.format(index + 1))
        user_win += 1
    elif user_num - computer_num == 0:
        print('第{}局平局'.format(index + 1))
        deuce += 1
    else :
        print('第{}局电脑胜'.format(index +  1))
        compunter_win += 1
    print('-------------第{}局结束--------------'.format(index + 1))

    if compunter_win == 2 :
        print('电脑胜')
        break
    elif user_win == 2:
        print('玩家胜')
        break
    else:
        # 平1局 一胜一负  平两局 赢一局  平三局
        if deuce == 1 and compunter_win - user_win == 0 and index == 2:
            print('平局')
        elif deuce == 3 :
            print('平局')
        elif deuce == 2 and index == 2:
            if compunter_win -user_win == 1:
                print('电脑胜')
            else:
                print('玩家胜')
