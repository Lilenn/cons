#
# 1. 写出基于socket的tcp的server和client端实现
# 服务端
import socket
sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
sock.bind(('127.0.0.1',9000))
sock.listen()

conn,addr = sock.accept()
msg = conn.recv(1024)
print(msg.decode('utf-8'))
conn.send('aa'.encode('utf-8'))
conn.close()

# 客户端
import socket
sock = socket.socket(family=socket.AF_INET,type=socket.SOCK_STREAM)
sock.connect(('127.0.0.1',9000))

server_msg = sock.recv(1024)
print(server_msg.decode('utf-8'))
sock.send('aaa'.encode('utf-8'),addr)

sock.close()


# 2. 写几个函数，分别计算
#     1. 给定半径，输出圆面积。
def mainji ():
    a = int(input('请输入半径'))
    b = 3.14*a*a
    print(b)
mainji()


#     2. 给定边长，计算正立方体的体积，公式 r^3 即边长的3次方。
def tiji():
   r = int(input('请输入边长'))
   tiji = r*r*r
   print(tiji)
tiji()


#     3. 给定半径，输出球的体积，公式(4/3)*π*r^3 即三分之四乘以派乘以半径的三次方（π等于3.14)。
def qiuti():
    a = int(input('请输入半径'))
    b = 3/4*3.14*a*a*a
    print(b)
qiuti()


# 3. 写函数，输入一个测验成绩，根据下面的标准，输出他的评分成绩（A-F）
#     ```
#     A:90~100
#     B:80~89
#     C:70~79
#     D:60~69
#     F:<60
#     ```
def b():
    a = input('请输入成绩')
    if a >= '90' and a < '100':
        print('A')
    elif a >= '80' and a < '89':
        print('B')
    elif a >= '70' and a < '79':
        print('C')
    elif a >= '60' and a < '69':
        print('D')
    else:
        print('E')
b()


# 4. 接收用户输入的年份，判断给定年份是否是闰年。
# 一个闰年后就是指它可以被4整除，但不能被100整除，或者它可以被400整除。
# 例如：2000年/4=500余0是闰年，2004年是闰年，1999年不是闰年。
# 提示：python中整除取余符号为 %
def nianfen():
    a = int(input('请输入年份'))
    if a%4 == 0 or a%400 == 0 and a%100 !=0:
        print('闰年')
    else:
        print('普通年')
nianfen()


# 5. 计算1+2+3+...+49的和
a = sum(range(1,50))
print(a)


# 6. 已知列表list1=[1,2,3,2,1,4,5] ,去除重复元素
list1=[1,2,3,2,1,4,5]
list = []
for i in list1:
    if i not in list1:
        list.append(i)
    print(list)


# 7. 已知列表list1=[2, -1, 5, 0, 99, -1], 求最大值
list1=[2, -1, 5, 0, 99, -1]
print(list1.index(max(list1)))


# 8. 写一个手机Phone类，属性有：手机品牌brand、手机价格price、库存数量stock
class Phone():
    def __init__(self,brand,price,stock):
        self.brand = brand
        self.price = price
        self.stock = stock
phone = Phone('mi',0,0)


# 9. 手机销售系统(函数封装或类封装任选)
# 菜单界面：
# ```
#  请输入要操作的编号：
#  1.查看所有手机品牌
#  2.添加新产品
#  3.修改原有产品信息
#  4.退出程序
# ```
# 功能要求：
# 1.查看所有手机品牌
#     """序号    编号   手机品牌   手机价格
#         1      001     vivoX9       2798
#         2      002     mate20       4000
#         3      003     iphone        8000
#     """"
# 2.添加新产品(添加新产品,包括产品名称、价格)
# 3.（选做）修改原有产品
#    先输出所有产品信息
#    然后询问用户要修改的产品序号
#    根据序号进行修改
# 4.退出程序

