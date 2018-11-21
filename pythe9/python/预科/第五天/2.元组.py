
# 创建元组的两种方式
tp1 = ()
# 如果元组在创建的时候没有放入元素
# 那么这个元组就没有意义
tp2 = tuple()
# 元组和列表的区别：
# 列表可以任意进行增删改查等操作
# 元组只可以进行 查操作
list1 = []
list2 = list()

tp3 = ('a','b','c','d')
if 'a' in tp3:
    print('存在')
else :
    print('不存在')

item = tp3[3]
print(item)

# length 长度 在此表示元素的个数
print(len(tp3))

tp4 = ('q','w','e','r')
print(tp3 + tp4)
print(tp3)
print(tp4)


