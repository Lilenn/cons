
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get('https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fi.meishi.cc%2Flogin.php%3Fac%3Dzhuce')
# 登陆
driver.find_element_by_name('username').send_keys('846077763@qq.com')
driver.find_element_by_class_name('password').send_keys('doudou12345.')
driver.find_element_by_xpath('//div[@class="nl_loginitem"]/input[@class="submit"]').click()

# 移动鼠标到菜谱大全
caipu = driver.find_elements_by_css_selector('li[class=hasmore]').pop(0)
ActionChains(driver).move_to_element(caipu).perform()

# 点击操作
driver.find_elements_by_css_selector('.pngFix dd').pop(7).click()

# 爬取网页数据
for row in range(1,7,2):
    x = float(row) / 6
    js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % x
    driver.execute_script(js)
    time.sleep(3)
# 写入文档
caidan_list = driver.find_elements_by_id('listtyle1_list')
for caidan in caidan_list:
    with open('caipu.txt','a',encoding='utf-8')as f :
        f.write(caidan.text)
        f.write('\n')