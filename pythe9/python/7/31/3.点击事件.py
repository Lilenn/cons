from selenium import webdriver
# action 行动 chains 链
from selenium.webdriver.common.action_chains import  ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import time
driver = webdriver.Firefox()
# driver.get('http://www.baidu.com'
# 右键点击
# driver.find_element_by_class_name('index-logo-src')
# logo = driver.find_element_by_xpath('//div[@id="lg"]/img')
# 等待直到目标标签出现
# logo = driver.find_element_by_css_selector('#lg >img')
# WebDriverWait(driver,10).until(lambda driver : logo.is_displayed())
# 双击事件
# ActionChains(driver).double_click(logo).perform()


# context 上下文
# content 内容
# context_click 右击
# action = ActionChains(driver).context_click(logo)
# 操作时间会跑到perform队列里面 perform实现
# action.perform()
# time.sleep(5)
# 鼠标移动
# more = driver.find_element_by_class_name('bri')
# WebDriverWait(driver,10).until(lambda driver : more.is_displayed())
# ActionChains(driver).move_to_element(more).perform()

