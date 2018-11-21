#
# 分布式爬虫
# 什么是分布式爬虫？
# 1.默认情况下，scrapy爬虫是单机爬虫，只能在一台电脑上运行
# 因为爬虫调度器当中的队列queue去重和set集合都是在本机上创建的
# 其他的电脑无法访问另外一台电脑上的内存的内容
# 2.分布式爬虫用一个共同的爬虫程序，同时部署到多台电脑上运行。
# 这样可以提高爬虫速度，实现分布式爬虫
#
# 分布式爬虫的前提：
# 1.要保证每一台计算机都能够正常的执行scrapy命令，能够启动爬虫
# 2.要保证所有的爬虫程序可以访问同一个队列一个set集合
# scrapy_redis
# 想要保证多台机器共用一个queue队列和set集合，scrapy中是结合scrapy_redis完成的
# 分布式爬虫可以让所有机器上的爬虫程序，从同一个queue队列中获取request请求，并且
# 每个机器取出request请求的对象是不一样的，直到所有的request被请求完毕
#
#
# 分布式爬虫的适用范围/要求：
# 1.分布式爬虫对电脑的性能有一定的要求
# 2.分布式爬虫对网速也有一定的要求  电脑性能和网速如果不是很好的话，爬虫效率不如单机爬虫
# 注意：并不是任何时候都可以使用分布式爬虫，因为对硬件有要求，小公司可能负担不起
#
# 分布式爬虫经常和redis数据库一起使用
# redis数据的特点
# 优点：
# 默认是使用持久化数据方式
# 体积小，使用方便
# 如果储存数据量比较大的话，启动速度很快
# 数据库中的数据和内存的数据可以相互访问
# 缺点：
# 从安全性的角度来说，持久化可能在崩溃，造成数据丢失
#
#
# 要实现分布式爬虫，首先要配置服务器主从:
#
# 配置主从的目的：
# 1.达到一个备份的功能。一旦master出现崩溃，而数据库中还有数据,
#  可以将其中的一个slave重新设置为主服务器，从而恢复redis的正常运行
# 2.一个redis服务器负责读写，性能较低，通过主从来减轻一个redis的压力
#
#
# redis主从的配置
# redis作为缓存服务器，主要试讲数据在内存中进行缓存，但是一台几区的内存和性能是有限的
# 当对于redis数据库的数据进行读写量较大的时候，那么一台reids就不能满足需求了
# 此时，需要将redis部署到多台机器上，用于写入数据的redis，称之为master，，而只
# 负责读取数据的redis，称之为slave
#
# redis主从的特点
# 1.master只负责写入数据，slave只负责读取数据
# 2.当slave创建的时候，会向master发送一个同步的命令，master接受到命令以后
#  将数据同步给slave
# 3.master只能有一个，slave可以有多个
#
#
#
#
#
#
#
#
