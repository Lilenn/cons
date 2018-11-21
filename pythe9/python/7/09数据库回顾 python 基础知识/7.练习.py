# 1.计算1到100之和
index = 0
for x in range(1,101):
    index += x
    print(index)

# 2.计算n的n次方

# 3.鸡兔同笼，笼子里一共有32个头，96条腿，问各有几只?
chickenHead = ''
for chickenHead in range(33):
    rabbitHead = 32 - chickenHead
    if chickenHead*2 + rabbitHead*4 == 96:
      print(chickenHead , rabbitHead)

# 4.有一百匹马，一百担货物，大马一只可以驼三担，中码可以驼两担，两只小马可以托一dan，问各有几只马？
horse_count = 100
goods = 100
bigHorse = ''
for bigHorse in range(101):
    zhongHorse = 100 - bigHorse
    smallHorse = 100 - zhongHorse - bigHorse
    if bigHorse*3 + zhongHorse*2 + smallHorse*0.5 == 100 :
        print(bigHorse,zhongHorse,smallHorse)






