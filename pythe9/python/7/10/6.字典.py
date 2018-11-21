
# 创建字典的两种方式
# dic1 ={}
# dic2 = dict()

# 字典里面所有的值都是以键值对的形式出现的
dic1 = {
    'name':'张三',
    'age' :'17',
    'friend ':['李四','王五','赵六','冯七']
}
# 获取指定的key值对应的name 值
# print(dic1['name'])
# KeyError: 'fond
# key 键错误 没有指定的键值“fond”
# print(dic1['fond'])

# 给字典中指定的键赋值
# 如果有这个键 则重新修改这个键对应的值
# 如果没有这个键，则创建这个键 病设置对应的值
# dic1['fond'] = '学习'
# print(dic1)

# dic1.pop('friend')
# pop里面需要写参数 参数为想要删除的
# TypeError: pop expected at least 1 arguments, got 0
# arguments 参数 expected 期望 at least至少
# 类型错误：pop方法希望得到至少一个参数 但是现在参数为0
# print(dic1)
# # 输出所有的zhi
# print(dic1.values())
# print(dic1.keys())
#
# if 'name' in dic1.keys():
#     print('存在')
# else:
#     print('不存在')
#
# if '张三' in dic1.values():
#     print('存在')
# else:
#      print('不存在')
# # 获取所有的key value
# for key in dic1:
#     value = dic1[key]
#     print(key,value)
# for key , value in dic1.items():
#     print(key ,value)

info = {
'name': '张三',
    'friend_list':[
        {
            'name': ' 李四',
            'friend_list': [
                {
                    'name': '王五',
                    'friend_list': [
                        '赵六', '冯七'
                    ]

                }
            ]
        }
    ]
}

for index , value in enumerate(info.values()):
    if index == 1 :
        for  value1 in value:
            for index2 ,value2 in enumerate(value1.values()):
                if index2 == 1:
                    for value3 in value2:
                        for index4 ,value4 in enumerate(value3.values()):
                            if index4 == 1 :
                                print(value4)


# for index , value in enumerate(info.values()):
#     print(index , value)
#     for value2 in info.values()[1]:
#         for value3 in value2:
#             for value4 in value3 :
#                 print(value4)
#




