# selenium  硒
# selenium 是一个自动化测试工具
# 测试---------岗位
# 手动测试
# 自动测试
# 白盒测试
# 黑盒测试
# 在python中的应用为：
# 1.selenium 可以完全模拟人对浏览器操作 对动态数据进行获取
# 动态数据由代码生成 在页面初始化的过程当中是没有的
# 也无法获取 单数可以通过selenium来获取
# 2.有些数据时需要进行登录才能获取的 比如说：
# 好友列表 评论 消费记录。。。。登陆以后获取cookie
# 才能进行以上的操作 但是使用selenium以后，可以避免人工登录
# 值需要得到账号 密码即可实现selenium代替登陆
#
# selenium 特点:
# 1.由程序控制浏览器进行操作 人不是手动操作浏览器
# 2.程序控制浏览器进行操作的时候 速度非常慢 所以要谨慎使用selenium
# 3.使用selenium控制浏览器的时候 需要下载浏览器对应的驱动程序
# 4.selenium为开源 免费 但是更新速度没有浏览器快 不是selenium更新慢 而是浏览器更新速度快
#   但是要注意selenium和浏览器之间的对应关系

# 引入网页驱动
from selenium import webdriver
import time
# 使用网页驱动来运行火狐浏览器
driver = webdriver.Firefox()
# 通过驱动来执行指定的网页
driver.get('http://www.baidu.com')

# selenium 提供了找到元素的方法 find element by XXX
# 这些方法全都是用python实现的
# 如果只是想对着个元素进行查找，定位 建议使用xpath或者 css_selecotor
# 如果需要对只熬到的内容那个进行点击等操作
# 建议使用find_element_by xxxx
# find 找到
# element 元素 节点  by 通过
# 通过kw这个id来找到一个指定的标签
# 报错：
# selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: [id="kw"]
# 错误原因： 代码执行速度很快 氮素浏览器响应很慢
# 代码执行到这里的的时候 浏览器里面的匀速可能还没加载完
# 所以报错 找不到指定元素
# time.sleep(3)
driver.find_element_by_id('kw').send_keys('selenium')
# 通过name值来找
# driver.find_element_by_class_name('wd').send_keys('csdn')
# 如果后面有中文 那么前边需要加一个u(unicode)
# driver.find_element_by_class_name('s_ipt').send_keys(u'智游')
# tag_name(标签的名字)
# driver.find_element_by_tag_name('input')
# 前端
# html
# css
# js
# selector 选择器 #id   .类名
# driver.find_element_by_css_selector('#kw')
# 通过xpath语法 定位一个元素
# driver.find_element_by_xpath('//form[@id="form"]/span/input[@id="kw"]')
# link 链接
# driver.find_element_by_link_text('贴吧')

# time.sleep(3)
#
# driver.close()