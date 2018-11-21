
# url 网址 lib  library 地址库
# request 请求
from urllib.request import urlopen
# parse 解析   quote引用
from urllib.parse import  quote

import string

import json

from prettyprinter import pprint
# URL不能够写中文 我们之所以能看到中文 是因为浏览器处于友好的目的
# 为了让用户识别特意显示的 但是在url执行的时候 中文会被转码
# 如果不进行转码 程序会出错
url = 'http://api.map.baidu.com/telematics/v3/weather?location=郑州市&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback='
response = urlopen(quote(url,safe = string.printable))
# urlopen 不支持中英文混写
responseData = response.read()
print(responseData)

# 地址栏不知此使用中文 所以需要进行转码
# 转码的时候 不只是将中文进行转码
# 同事以会将一些特殊符号进行转码  比如  ：？
# 如果不想让着些特殊符号进行转码
# 就要使用安全转码（只会转码中文）
print('没有使用 safe\n{}'.format(quote(url)))

print('使用了safe\n{}'.format(quote(url,safe = string.printable)))

responseJson = json.loads(responseData)
pprint(responseJson)

print(responseJson['date'])

for dict in responseJson['results'][0]['index']:
    print(dict['des'])
    print(dict['tipt'])
for dict in responseJson['results'][0]['weather_data']:
    print(dict['date'])






