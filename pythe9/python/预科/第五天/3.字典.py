from  random import randint
# pretty 美好的；漂亮的  pretty boy printer打印；输出
from prettyprinter import pprint
# 字典   key  value   键值对
# list = ['a','b','c']
# key   0   1   2
# value a   b   c

# 声明字典的两种方式
dic1 = {}
dic2 = dict()

dic3 = {
    'name' : '小明' ,
    'age' :  17 ,
    # True代表男还是女 是自己规定的
    'sex' : True ,
    'height' : 1.76 ,
    'fond':['打游戏','学习','写代码','陪妹子逛街']
}
print(dic3)
print(dic3['fond'])
# 有的话 修改  没有属性则增加
dic3['age'] = 18
print(dic3['age'])
dic3['girlFriend'] = '凤姐'
print(dic3)

dic3.pop('girlFriend')
print(dic3)
# TypeError: pop expected at least 1 arguments, got 0
# pop期望得到最少1个参数 现在得到了0个
# dic3.pop()
print(dic3)


print(dic3.keys())
print(dic3.values())
# 判断key值是否存在
if 'fonds' in dic3.keys():
    print('fonds存在')
else :
    print('fonds不存在')

# 列表不需要添加字符串
if ['打游戏','学习','写代码','陪妹子逛街'] in dic3.values():
    print('学习存在')
else :
    print('不存在')

print(dic3)
pprint(dic3)

dic4 = {
    'name' : '小兰' ,
    'age' : 12 ,
    'fond' : '美食',
    'info':{
        'description':'很好的一个人',
        'phone':'123123123',
        'friend' : [
            {
                'friend_name':'小明' ,
                'frined_age' : 17
            },{
                'friend_name':'小王',
                 'friend_age':16
            },{
                'friend_name':'小张',
                'friend_age':14
            }
        ]
    }
}
# 获取key和value值
for key in dic4:
    # dic4['name']
    value = dic4[key]
    print(key , value)
# 获取key和value的第二种方法  （推荐这种写法）
for key ,value in dic4.items():
    print(key ,value)

# KeyError: 'class' 获取一个自己没有的key会报错
# value = dic4['class']
# print(value)

# 获取key对应的值 如果没有key 则赋予一个默认值
# 值1：key
# 值2：默认值
value = dic4.get('class','三年级二班')
print(value)

# 作业：获取所有的friend_name以及friend_age、















































