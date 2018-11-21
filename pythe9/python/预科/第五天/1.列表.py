# JSON
# [] , () , {}
list = [[],[],[]]
list = [('a','A'),('b','B'),('c','C')]
for x in list:
    print(x)
for x , y in list:
    print(x , y)
# 枚举 enumerate 可以让被遍历元素 添加一个编号（索引值）
# for 后面的第一个参数 即为索引值 第二个参数 为被遍历的元素
for x , y  in enumerate(list):
    print(x , y)
for x ,( y ,z ) in enumerate(list):
    print(x , y ,z )
list = [('a','A'),('b','B'),('c','C')]
list = [(1 ,[2, 3,]),(4,[5,6]),(7,[8,9])]
for index , ( x , [ y , z]) in enumerate(list):
    print(index , x , y , z)


list1 = ['a' , 'b' ,'c']
list2 = ['d','e','f']
# +可以使列表可以和字符串一样进行拼接
list3 = list1 + list2
print(list3)
# extend 扩展；添加
list1.extend(list2)
print(list1)

list1 = [['a'],['b'],['c']]
list2 = [['c'],['d'],['e']]
# extend 将被合并的集合的所有值给 主动进行合并的集合
# 最终结果 为两个集合的元素个数的总和
list1.extend(list2)
print(list1)
list1 = [['a'],['b'],['c']]
list2 = [['c'],['d'],['e']]
# 将list2作为一个整体 给list1 list1的元素的个数等于之前的个数+ 1
list1.append(list2)
print(list1)

list1 = range(1, 101)
list2 = []
for x in list1:
    if x % 2 == 1:
        list2.append(x)
        # print(list2)
print(list2)

# 列表推导式
list4 = [x for x in list1 if x % 2 ==1]
print(list4)

list = ['张三','张飞','张益达','关云长','赵子龙']
list5 = [x for x in list if x.startswith('张')]
print(list5)

list = ['1','2','3']
# reverse 相反的
list.reverse()
print(list)

list = [1, 2 ,3 ,4 ,5,6,7,8,9,10]
some = 0
for x in list:
    some += x
print(some)
result = sum(list)
print(result)

list = [ 1, 3, 5, 7 ,9 ,2 , 4 , 6 , 8, 10]
# revsrse 倒序  默认值为Flase
list2 = sorted(list , reverse = True)
print(list2)


list = ['a' , 'b' ,'c']
print(list[0])

list = [['a','b'],['c','d'],['e','f']]
print(list[1][0])

list = [
    [
        ['a'],  #[0][0][0]
        ['b']     #010
    ],
    [
        ['c'],  #100
        ['d']   # 110
    ],
    [
        ['e'],  # 200
        ['f']   # 210
    ]
]
print(list[2][0][0])

list1 = [ [1 ,2 ,4], [3, 4], [5 ,6]]
for x in list1:
    for y  in x :
        print(y)

list = [
        [
            ['a'],  # [0][0][0]
            ['b']  # 010
        ],
        [
            ['c'],  # 100
            ['d']  # 110
        ],
        [
            ['e'],  # 200
            ['f']  # 210
        ]
    ]

for x in list :
    for y in x :
        for z in y :
            print(z)
for x , [[y],[z]]in enumerate(list):
    print(y ,z)


# 作业: 获取下面列表当中的每一个值，不必在同一行显示
# list = [(1 ,[2 , 3]) ,( 4 ,[5 ,6 ,7]),(8, [9,10,11,12])]

# 作业2：将下面的列表进行排序 排序顺序为 正序 要求不能使用sorted方法
# list = [ 1, 3, 5, 7 ,9 ,2 , 4 , 6 , 8, 10]
