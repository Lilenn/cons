# https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fi.meishi.cc%2Flogin.php%3Fac%3Dzhuce

# username	846077763@qq.com
# password	doudou12345.

# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36

# 美食杰 使用cookie模拟登陆 获取网页源码 使用xpath得到用户信息 存储到excel表格

from http.cookiejar import CookieJar,LWPCookieJar
from urllib.parse import urlencode
from urllib.request import Request,HTTPCookieProcessor,build_opener
import requests
from lxml import etree
import re

cookie = LWPCookieJar(filename='meishijie.txt')
cookie_handler = HTTPCookieProcessor(cookie)
opener = build_opener(cookie_handler)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
post_url = 'https://i.meishi.cc/login.php?redirect=https%3A%2F%2Fi.meishi.cc%2Flogin.php%3Fac%3Dzhuce'
post_data = urlencode({
    'username':'846077763@qq.com',
    'password':'doudou12345.'
})
request = Request(post_url,bytes(post_data,encoding='utf-8'))
response = opener.open(request)
print(response.read().decode())
cookie.save(ignore_expires=True,ignore_discard=True)

cookie = LWPCookieJar()
cookie.load('meishijie.txt',ignore_expires=True,ignore_discard=True)
opener = build_opener(HTTPCookieProcessor(cookie))
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
request = Request('https://www.meishij.net/')
response = opener.open(request)
print(response.read().decode())

response = requests.post('https://www.meishij.net/',headers = headers)
print(response.content)

root = etree.HTML(response.content)
print(root)

caidan_url = root.xpath('//div[@class="listtyle1"]/a/@href')
print(caidan_url)













