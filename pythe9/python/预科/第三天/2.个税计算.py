

salary = input('请输入你的工资')
# 将输入的内容转化成数字
salary = int(salary)
sanXian = 0
if salary >= 7662 :
    sanXian = 7662 * 0.225
else:
    sanXian = salary * 0.225
# 所得额
suoDeE = salary - sanXian - 3500
shuiLv = 0
kouChuShu = 0

if suoDeE <= 0 :
    print('loser')
else :
    if suoDeE <= 1500 :
        shuiLv = 0.03
    elif suoDeE <= 4500:
        shuiLv = 0.1
        kouChuShu = 105
    elif suoDeE <= 9000 :
        shuiLv = 0.2
        kouChuShu = 555
    elif suoDeE <=35000 :
        shuiLv = 0.25
        kouChuShu = 1005
    elif suoDeE <=55000 :
        shuiLv = 0.3
        kouChuShu =2755
    elif suoDeE <= 80000 :
        shuiLv = 0.35
        kouChuShu = 5505
    else :
        shuiLv = 0.45
        kouChuShu = 13505
    geShui = suoDeE * shuiLv - kouChuShu
    print(geShui)

sum = 10 / 3
print(sum)
