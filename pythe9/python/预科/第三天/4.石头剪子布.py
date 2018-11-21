
from random import  randint

user_num = input('请输入一个数字')

# 0 石头  1 剪子  2 布  or或者  and 并且
# 0   1    -1
# 1   2    -1
# 2   0     2
computer_num = randint(0 , 2)
print(computer_num)
if user_num.isdigit():
    user_num = int(user_num)
    if  0 <= user_num <= 2 :
        if user_num - computer_num == -1 or user_num - computer_num == 2:
            print('you win')
        elif user_num - computer_num == 0 :
            print('deuce')
        else :
            print('you lose')
    else :
        print('输入的数值大于有效范围')
else :
    print('输入的内容格式错误，请输入0~2之间的一个数值')