# 允许外部使用的方法
__all__ =['work']
def work():
    print('人人都有工作的权利')
def study():
     print('学习使我快乐')
def play():
     print('我最大的爱好是coding')
def rule():
    print('以上都是假的')

     # 没有在外部使用这个包
     # 包是本身自己内部在使用
    if __name__=='_main_':
        work()
        study()
