# 声明方法1
# 创建一个txt文件，里面存放1000条数据，每条数据长度为10 ，包含大小写字母和数字
# import random
# str = 'qwertyuiopASDFGHJKL1234567890'
# def getRandom():
#     with open('random.txt','w')as f:
#         for index in range(1000):
#             contend = ''
#             for x in range(10):
#                 char = random.choice(str)
#                 contend +=char
#             f.write(contend + '\n')
#         f.close()
# getRandom()


# 声明方法2
# 读取txt文件里面的所有数据，如果该条数据只有数字，那么创建一个txt文件 保存起来
def readAllInfo():
    list = []
    with open('random.txt','r')as f:
        for line in f.readlines():
            line = line[0:-1]
            list.append(line)
    f.close()
    return  list

def getAllInfo():
    list = readAllInfo()
    with open('Num.txt','w')as f:
        for value in list:
            if value.isdigit():
                f.write(value + '\n')
        f.close()
getAllInfo()

# 声明方法3
# 读取txt文件里面的所有数据 如果该条数据只有字母 那么创建一个txt文件 保存起来
def getAllCharInfo():
    list =readAllInfo()
    with open('char.txt','w')as f:
        for value in list:
           if value.isalpha():
               f.write(value + '\n')
        f.close()
getAllCharInfo()


# 声明方法4
# 读取txt文件里面的所有数据 如果该条数据包含数字和字母 那么创建一个txt文件 保存起来

def getNumWithCharInfo():
    list= readAllInfo()
    with open('numwithchar.txt','w')as f:
        for value in list:
            isHasNum = False
            isHasChar = False
            for char in value:
                if char.isdigit():
                    isHasNum = True
                else:
                    isHasChar = True
            if isHasChar == True and isHasNum == True:
                f.write(value + '\n')
            f.close()
getNumWithCharInfo()
