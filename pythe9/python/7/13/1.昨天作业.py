# 一女子择偶，两个男士被选择
# 1.如果两男存款少于100万 都不考虑
# 2.如果两男存款大于100万 跟存款多的走,如果都大于10000万 看其他
# 3.男士
# 4.选择个子高的
# 5.如果个子都大于170 且相差不到5cm 看颜值（0,10）
# 6.低于7分的直接pass 高于7分选择颜值高的，如果相差不到2，看房子
# 7.房子不能低于100平且价值不能少于200万 如果都有的话 选择价值高的
#    价值相差不到20万，看车子
# 8.车子价值不能少于50万 相差不到10万 抛硬币
# 使用继承
# 传入两个对象

# def 抛硬币()

class People(object):
    def __init__(self,name='',sex='',money='',height='',face='',house_area='',housre_value='',car_value='',win=''):
        self.name = name
        self.sex =sex
        self.height = height
        self.money = money
        self.face = face
        self.house_area = house_area
        self.house_value = housre_value
        self.car_value = car_value
        self.win = win
class Woman(People):
    # 判断男方当中是否已经产生了赢家
    def isHasWin(self,man1,man2):
        if man1.win == False and man2.win ==False:
             return False
        else:
            return  True
    def choiceBoyFriendWithBoy(self,xiaowang ,xiaoli):
        if xiaowang.money <1000000 and xiaoli <1000000:
            print('俩人都钱少')
            return
        # 小王少于100 小李大于100
        elif xiaowang.money <1000000 and xiaoli.money>= 1000000:
            print('小李胜出')
            return
        # 小王大于100，小王少于100
        elif xiaowang.money>=1000000 and xiaoli.money<1000000:
            print('小王胜出')
            return

        elif  xiaowang.money<= 10000000 and  xiaoli.money<=10000000:
            if xiaowang.money < xiaoli.money:
                print('小李胜出')
                return
            else:
                print('小王胜出')
                return
        elif xiaowang.money <1000000 and xiaoli.money>=10000000:
            print('小李胜出')
            return
        elif xiaowang.monry>=10000000 and xiaoli.money <1000000:
            print('小王胜出')
            return
        if xiaowang.sex ==False and xiaoli.sex == False:
            print('都不是男的')
            return
        elif xiaoli.sex ==False and xiaowang.sex == True:
            print('小王的性别是对的')
            return
        elif xiaoli.sex ==True and xiaowang.sex == False:
            print('小李的性别是对的')
            return
        # 判断身高

        if xiaowang.height <170 and xiaoli.height <170 and  xiaowang.height < xiaoli.height:
            print('小李高')
            return
        elif xiaowang.height <170 and xiaoli.height <170 and xiaowang.height > xiaoli.height:
            print('小王高')
            return
        elif xiaowang.height-xiaoli.height >5:
            print('小王高')
            return
        elif xiaowang .height-xiaoli.height <5:
            print('小李高')
            return

        if xiaowang.face <7 and xiaoli.face<7:
            print('都太丑')
            return
        elif xiaowang.face>=7 and xiaoli.face <7:
            print('小王帅')
            return
        elif xiaoli.face>=7 and xiaowang.face<7:
            print('小李帅')
            return
        elif xiaowang.face-xiaoli.face>=2:
            print('小王帅')
            return


class Man(People):
    def __init__(self,name,sex,height,money,face,house_area,house_value,car_value,win):
        super(Man,self).__init__(name,sex,height,money,face,house_area,house_value,car_value,win)


xiaoMei = Woman()
xiaoWang = Man('小王',True,10000000,169,7,100,200,50,False)
xiaoLi = Man('小李',True,1000000,180,10,50,80,20,False)

xiaoMei.choiceBoyFriendWithBoy(xiaoWang,xiaoLi)





