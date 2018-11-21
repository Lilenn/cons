
# 总结：xpath bs4和正则的区别
# 总结：数据方式的区别
# 举例说明

# https://www.meishij.net/chufang/diy/guowaicaipu1/japan/?&page=1
# Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Mobile Safari/537.36


url = 'https://www.meishij.net/chufang/diy/guowaicaipu1/japan/'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
}
# --------------------------------------------------正则 方法--------------------------------------------------
import  re
from urllib.request import Request,urlopen

request = Request(url ,headers=headers)
# 获取响应
response = urlopen(request)
code = response.read().decode()
pattern = re.compile(r'<div class="listtyle1".*?>.*?<a.*?class="big".*?title="(.*?)".*?>.*?<img class="img".*?src="(.*?)".*?>.*?<div class="c1">.*?<span>(.*?)</span>',re.S)
result = pattern.findall(code)
# print(result)
for image in result:
    image_alt =image[0]
    image_src = image[1]
    image_rq = image[2].split(' ')[3]
    print(image_alt+'('+image_rq+'人气'+')',image_src)

# --------------------------------------------------xpath 方法------------------------------------------------------
# from lxml import etree
# import requests
#
# response = requests.get(url,headers = headers)
# # print(response)# 将字符串转化为html代码
# root = etree.HTML(response.content)
# image_list = root.xpath('//div[@class="listtyle1"]/a')
# for image in image_list:
#       # . : 表示从当前节点开始获取
#     image_alt = image.xpath('./img/@alt')[0]
#     image_src = image.xpath('./img/@src')[0]
#     image_rq = image.xpath('./div/div/div/span/text()')[0].split(' ')[3]
#       # 拼接内容
#     print(image_alt+'('+image_rq+'人气'+')',image_src)

# -----------------------------------------------------bs4 方法------------------------------------------
# from bs4 import BeautifulSoup
# import requests
# # from lxml import etree
# response = requests.get(url , headers = headers).content
# soup = BeautifulSoup(response,'lxml')
# image_list = soup.select('div.listtyle1')
# # print(image_list)
# for tag in image_list:
#      value = tag.find_all('img')
#      # print(value)
#      for image in value:
#          image_alt = image.get('alt')
#          image_src = image.get('src')
#          # print(image_alt)
#          # print(image_src)
#      image_rq = tag.span.string.split(' ')[3]
#      # print(image_rq)
#      print(image_alt+'('+image_rq+'人气'+')',image_src)