
import requests
# import re
from  lxml import etree

url = 'http://www.qiushibaike.com/hot/page/1'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
response = requests.get(url,headers = headers)
print(response.content)
# pattern = re.compile(r'<div class="author clearfix">.*?<h2>(.*?)</h2>',re.S)
# result = pattern.findall()
# 将字符串转化成html代码
root = etree.HTML(response.content)
# element 元素；节点；标签
print(root)
# //从根标签开始找,不看层级关系 直接找到类名为author clearfix的标签
# /a 找到某一个标签下面的a标签
# text（）获取标签的文本
name_list= root.xpath('//div[@class="author clearfix"]/a/h2/text()')
print(name_list)
content_list = root.xpath('//div[@class="content"]/span/text()')
print(content_list)

# 美食杰 使用cookie模拟登陆 获取网页源码 使用xpath得到用户信息 存储到excel表格
