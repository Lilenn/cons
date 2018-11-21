# 首先引入网页驱动
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fwww.meishij.net%2F')
# 输入账号
driver.find_element_by_name('username').send_keys('846077763@qq.com')
# 输入密码
driver.find_element_by_class_name('password').send_keys('doudou12354.')
title = driver.find_element_by_id('more_dsf_btn').text
print(title)
# text获取的是标签之间的文本 而不是填充的内容
# time.sleep(3)
# username = driver.find_element_by_name('username').text
password = driver.find_element_by_class_name('password').text
# print(username)
print(password)
# driver.find_element_by_name('username').clear()
# driver.find_element_by_class_name('password').clear()

# 点击登陆
# driver.find_element_by_xpath('//div[@class="nl_loginitem"]/input[@class="submit"]').click()

