# # 创建列表的两种方式
# list1 =[]
# list2 =list ()
#
# # 每两个元素之间以，隔开
# list1 = ['hello world',[[]],1, 3.14 ,True,]
#
#
# list1 =['outMan', '小李子','诺兰','皮克斯']
# # 获取列表里面索引为0的元素
# print(list1[0])
# # IndexError: list index out of range
# # 索引错误：列表索引超出范围
# # print(list1[5])
# # 如果 ：左右两边都不写值，表示获取所有元素
# print(list1[:])
# # ：左边表示指定搜索引开始
# # ：右边表示到指定索引结束（不包括该位置）
# print(list1[1:1])
# # 值1：开始的位置
# # 值2：结束的位置
# # 值3：隔几个元素
# print(list1[1::2])
# # 倒叙
# print(list1[::-1])
#
# # ----------------------------------------insert 插入-----------------------------------------
# list1 = [1,2,3,4,5,6,7]
# # insert 会指定出入的位置
# list1.insert(2,'hello')
# print(list1)
# # append  追加的内容默认放在列表的队尾
# list1.append('world')
# print(list1)
# # extend  扩展
# list1.extend('张三')
# print(list1)
#
# # list1 = [1,2,3]
# # list2 = ['a','b''d','c']
# # list1.append(list2)
# # append 追加内容  [1, 2, 3, ['a', 'bd', 'c']]
# # 不管追加的事什么样的类型的内容
# # 都会讲者快内容当做一个整体
# # 放入到被添加的列表中
# # -------------------------
# # extend 扩展   [1, 2, 3, 'a', 'bd', 'c']
# # 将扩展对象的每一个元素
# # 分别添加到被扩展对象中
# # list1.extend(list2)
# print(list1)
#
# # 晚自习作业三：代码实现extend 将任意容器里面的所有元素放入到另外一个容器当中
# list1 = ['a','s','d','f','d','s','a']
# # 将最后一个元素弹出
# list1.pop()
# print(list1)
#
# # list1.pop(2)
# # print(list1)
# # 删除所有符合指定要求的这些元素中
# # 索引最小的这个  ['a', 's', 'f', 'd', 's']
# list1.remove('d')
# print(list1)
# # 查看列表当中有没有指定的元素
# if 'b'in list1 :
#     print('存在')
# else:
#     print('不存在')
#
# list1 = ['a','b','c','d']
# # reversed 相反的   ['d', 'c', 'b', 'a']
# list1.reverse()
# print(list1)
# # 获取列表里面指定的元素的索引
# result = list1.index('a')
# print(result)
#
# # sort  排序  [0, 2, 3, 4, 5, 7, 8]
# #reverse 倒排序  [8, 7, 5, 4, 3, 2, 0]
# list1 = [5,3,8,4,0,2,7]
# list1.sort()
# list1.reverse()
# print(list1)
# # 获取列表的长度
# print(len(list1))




a = {"var1": {"key6", "data2"}, "var2":{"key2", "data1"}, "var3": {"dataw", "333", "bbss"}}


for k in a:
    if k == 'var3':
        print(k)
    b = a[k]
    for c in b:
        if c == '333':
            print(c)


def count(a):
    a = a
    b = {}
    c = len(a)
    i = 0
    while i < c:
        if a[i] in b:
            b[a[i]] += 1
        else:
            b[a[i]] = 1
        i += 1
    for a in b.items():
        print(a)

count("aasdxzs123123sdf")