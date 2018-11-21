import requests
import os
from urllib.request import urlretrieve
from lxml import etree
import shutil
if os.path.exists('images'):
    shutil.rmtree('images')
os.mkdir('images')
os.chdir('images')
# 全局变量
current_page = 1
# 局部变量  声明的作用 是告诉程序该变量是个声明类型的变量
def get_image_with_code(url):
    global current_page
    # 总结： xpath  bs4和正则的区别
    # 总结：数据方式的区别
    # 举例说明
    # response = urlopen().read().decode()
    response = requests.get(url).text
    # print(response)
    # element 元素 节点 标签、
    code = etree.HTML(response)
    img_list = code.xpath('//div[@class="il_img"]/a/img')
    print('正在下载第{}页'.format(current_page))
    # 创建对应页面下的文件夹
    os.mkdir('Page{}'.format(current_page))
    # 移动光标
    os.chdir('Page{}'.format(current_page))
    for img in img_list:
        img_src = img.get('src')
        img_alt = img.xpath('@alt')[0]
        urlretrieve(img_src , img_alt +'.jpg')
    # 局部变量  声明的作用 是告诉程序该变量是个声明类型的变量
    current_page +=1
    os.chdir(os.path.pardir)
    # 如果还有下一页则返回[Element a ip]
    # 如果没有下一页 则返回[]
    next_page_uel = code.xpath('//a[@class="page-next"]')

    if len(next_page_uel) == 0:
        print('已经找到最后一页')
        return
    href = next_page_uel[0].get('href')

    full_url = 'http://www.ivsky.com/' + href
    get_image_with_code(full_url)

get_image_with_code('http://www.ivsky.com/tupian/meishishijie/')

# 爬虫流程 ：
# 1.拼接url
# 2.获取user-agent ，设置代理ip
# 3.请求url URLopen requests
# 4.获取响应（ response response。read（）  response。content（）  response。text（））
#    获取cookie
# 5.获取源码中指定数据（re xpath bs4）
# 6.美化数据  正则 strip
# 7.保存（文件读写 squlit3 xlwt）