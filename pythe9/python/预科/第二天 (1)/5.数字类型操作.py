
name = '张三'
name1 = '李四'
print(name + name1)

age  = 18
year = 1
print(age + year )
# TypeError: must be str, not int
# 类型错误 必须是字符串 不能是数字
# print(name + age)

age = 18
year = 1
print(age  - year)
print(age * year)
# 求余
print(age % year)
# 除法
print(age / year)

'''
  美女征婚
  1.对方必须是男的
  2.对方房子面积不能小于100
  3.对方的工资不能少于20w
  4.对方的车子价值不能少于50w
  如果对方存款超过1000w 以上条件无视
  如果对方存款超过500w  车子 工资条件无视
  如果对方存款不超过100w  结束相亲
  要求：男方所有条件 以input形式输入
'''

sex = input('请输入性别')
house_area = input('请输入房子面积')
salary = input('请输入工资')
car_price = input('请输入车子价值')
money = input('请输入存款')
# 转化数字
house_area = int(house_area)
salary = int(salary)
car_price = int(car_price)
money = int(money)

# 大于1000w
if money > 10000000 :
    print('相亲成功')
    # 小于100w
elif money < 1000000 :
    print('凉凉')
# 大于100w 小于1000w
else :
    # 大于500w 小于1000w
    if money > 5000000 :
        # 如果性别是女的
        if sex == '女' :
            print('再见')
            # 男的
        else :
              # 房子面积小
            if house_area < 100 :
                print('世界那么大 我想去看看')
                # 房子面积满足要求了
            else :
                print('好想跟他回家')
    else :
        print('先处着看看')
