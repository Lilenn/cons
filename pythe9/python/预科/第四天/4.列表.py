
# 两种方式声明列表
# 声明是列表
# 容器 用来存放对象，变量等内容
list1 = []
list2 = list()
list3 = ['hello', 17 , True , 3.14]
list4 = [['hello'],[17],[True]]
print(list4)

list = ['张三','李四','王五','赵六']
print(list)
# append 追加；添加  默认添加在最后一位
list.append('冯七')
print(list)
# insert 插入
# 值1：插入的位置
# 值2：插入的内容
list.insert(0,'小二')
print(list)
list.insert(3,'中间人')
print(list)
# 如果插入的位置 超出了列表的长度 那么就插入到最后一位
list.insert(100 ,'大神')
print(list)
list.append('张三')
print(list)
# remove方法 默认将列表里面的元素 从左往右依次删除
list.remove('张三')
list.remove('张三')
print(list)
# pop 弹出最后一个元素  append相反
list.pop()
print(list)
list.pop(2)
print(list)

if '冯七' in list:
    print('冯七在')
else :
    print('冯七不在')

index = list.index('冯七')
print(index)

list[0] = '阿三'
print(list)

# 值1：开始位置 （包括该位置）
# 值2：结束位置 （不包括该位置）
print(list[1:-1])
print(list[1:])
# 值3：增量
print(list[1:4:3])
# 倒序

print(list[::-1])
print(list[::2])
print(list[1::2])
print(list)

print(len(list))
print(len('QWERTYUIOP{'))
# 分别获取每一个元素
for x , y  in list:
    print(x , y)
