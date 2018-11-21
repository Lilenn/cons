
name = '张三'
age = 17      #int 整数
height = 1.78  # float 小数
# 其他语言 %s 代表字符串的占位符
# python   %s 代表所有类型的占位符
print('我的名字是%s,我的年龄是%s岁,我的身高是%s米' % (name ,age ,height))

    # 2018121212100
    # 0000020181111 
info = '我的年龄是%d岁'% age
print(info)
# 保留几位整数  如果整数位数不够 用0补齐
info = '我的年龄是%.6d' % age
print(info)

# 默认保留6位小数
info = '我的身高是%f米' % height
print(info)
# 精度丢失：当保留小数位太多的时候 会造成进度丢失
# 这个无需在意 因为计算机无法准备表示这么多位  float
info = '我的身高是%.2f米' % height
print(info)
