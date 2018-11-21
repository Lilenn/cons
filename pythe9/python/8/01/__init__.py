# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# import time
#
# driver = webdriver.Firefox()
# driver.get('http://www.baidu.com')
# # 获取当前的window对象
# current_window = driver.current_window_handle
# # 获取当前 窗口的编号 和网页标题
# print(current_window,driver.title)
#
# new = WebDriverWait(driver,10).until(lambda driver : driver.find_element_by_css_selector('.hdline0 . a3'))
# new.click()
# # 获取所有的窗口
# all_windows = driver.window_handles
# print(all_windows)
#
# for window in all_windows:
#     if window != current_window:
#         # switch 切换
#         driver.switch_to.window(window)
# title = driver.find_element_by_css_selector('.text_title h1').text
# WebDriverWait(driver,10).until(lambda driver : title.is_displayde())
#
# print(title)
#
# time.sleep(3)
# # 关闭窗口
# driver.close()
# # 关闭浏览器
# # driver.quit()
#
# driver.switch_to.window(current_window)
# print(driver.find_element_by_css_selector('#footer span').text)

from selenium import  webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Firefox()
driver.get('https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fi.meishi.cc%2Flogin.php%3Fac%3Dzhuce')

driver.find_element_by_name('username').send_keys('846077763@qq.com')
driver.find_element_by_class_name('password').send_keys('doudou12345.')
# input[@class="submit"] submit 是将input输入框变为 按钮
driver.find_element_by_xpath('//div[@class="nl_loginitem"]/input[@class="submit"]').click()

caipu = driver.find_elements_by_css_selector('li[class=hasmore]').pop(0)
ActionChains(driver).move_to_element(caipu).perform()

driver.find_elements_by_css_selector('.pngFix dd').pop(7).click()

for row in range(1,7,2):
    x = float(row) / 6
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % x
    # driver.execute_script(js) 和数据库中 执行光标相似 ,python里边的 eval 高级函数
    driver.execute_script(js)
    time.sleep(3)

caidan_list = driver.find_elements_by_id('listtyle1_list')
for caidan in caidan_list:
    with open('caipu.txt' ,'a',encoding='utf-8') as f:
        f.write(caidan.text)
        f.write('\n')