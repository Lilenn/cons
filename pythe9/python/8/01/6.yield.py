# return 和 yield 的区别
# return可以往方法外传递一个值，之后return后面的代码统统不在执行
# yield也可以往方法外面传递一个值，但是传递之后，继续回到yield后面开始执行
#   通过yield传递值的这个方法，是一个可迭代的对象
def test1(name):
    print('return方法')
    return name
    print('return方法结束')
name = test1('zhangsan')
print(name)

def test2(age):
    for i in range(age):
        yield i
        print('hello')
for x in test2(18):
    print('x=',x)

# cd change dricer 改变文件夹路径
# cd .. 回到上一级
# scrapy startproject baidu
# crawl