# 进程和线程的区别：
# 1.进程：每个程序都会有一个进程，负责管理每个程序的各个功能的执行，
#   进程只会有一个，而且至少有一个（相当于包工头）
# 2.线程：每个进程里面至少有一个线程，称之为 主线程，除此之外还会有其他线程，称之为分线程
#   线程是控制执行任务的最小单位（相当于农民工）
# 3.进程 负责控制各个线程 的执行，当程序运行，进程启动；程序关闭，进程结束
#
# 主线程和分线程：
# 1.代码运行默认在主线程里面 如果需要执行新的任务，可以开辟新线程
# 2.分线程没有个数限制，分线程里面的任务结束后，分线程结束
#
# 分线程的使用场景：
# 1.当有大量的任务需要执行的时候，可以将任务放入到分线程里面
# 2.当有大量任务需要执行的时候，而任务的执行顺序需要指定的时候，可以使用分线程
# 3.当界面有大量效果需要更新的时候，需要放入到分线程里面

# 同步任务：上一个任务没有完成，下一个任务不能开启
# 异步任务：可以同时执行多个任务，上一个任务没有完成，下一个任务也可以开启
# 分线程和异步的区别：
# 1.分线程 可以同时开启多个任务，所有的任务由分线程自己完成
# 2.异步可以同时开启多个任务，但是自己只做一个任务，其他任务命令有他人来完成
# python 里面又两个负责线程的模块，thread,threading
# threading在thread模块基础上做了扩展
# thread 线程
import threading
# import
# 获取当前线程的名称  main 主要的
print('当前线程为',threading.current_thread().name)
def myThread():
    print('位置1', threading.current_thread().name)
    print('位置2', threading.current_thread().name)
    print('位置3', threading.current_thread().name)
    print('位置4', threading.current_thread().name)
    print('位置5', threading.current_thread().name)
    print('位置6', threading.current_thread().name)

myThread()

class People(object):
    def Thread_test(self):
        print('对象方法',threading.current_thread().name)
p = People()
p.Thread_test()
# threading.Thread 开辟一个新的线程 target 目标 name 为分线程名称
sub_thread = threading.Thread(target=myThread,name='newThread')

# 开始执行分线程
sub_thread.start()
# 确保任务的执行顺序 自己的线程先完成，之后再执行其他线程
sub_thread.join()
# 当程序运行时，会先在主线程中执行， 因为在程序刚开始的时候，只有主线程，没有分线程
# 然后会根据情况进入到分先曾中，主线程和分线程的任务是交叉进行的
# （因为是两个路）自己线程的执行情况不会影响对方的线程
# 所以感觉是交叉的
# 分线程代码结束后，会回归到主线程

print('outside1',threading.current_thread().name)
print('outside2',threading.current_thread().name)
print('outside3',threading.current_thread().name)
print('outside4',threading.current_thread().name)
print('outside5',threading.current_thread().name)

