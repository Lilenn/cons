from selenium import webdriver

from selenium.webdriver.common.by import By
import os
import time
driver = webdriver.Firefox()

driver.get('file:///'+os.path.abspath('4.index.html'))
# 通过标签名字找到指定标签
btns = driver.find_elements_by_tag_name('button')
print(btns)
# #1. 通过索引来找到指定的标签
btns[1].click()
#
# for btn in btns:
# # 2.通过属性来找到指定的标签
#     if btn.get_attribute('type') =='button':
#         btn.click()
#     time.sleep(3)
#     # btu.click()
#
# driver.find_element_by_tag_name('button').click()
# # find_element_by_XX 通过xx来找到所有标签当中的第一个标签
# # find_elements_by_X t通过xx来找到所有符合的标签
#
# #3. 弹出指定的元素 如果不写索引 默认为最后一个
# driver.find_elements_by_css_selector('button').pop(0).click()
# # [type=button] []里面为限制条件 限制选择的内容
# driver.find_elements_by_css_selector('button[type=button]').pop().click()
# # 4.通过。。。来找到指定的标签
# driver.find_element(by=By.ID , value='pink').click()