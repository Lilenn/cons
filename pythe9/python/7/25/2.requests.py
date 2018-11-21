
# requests 是对urllib3 的封装
import requests


url = 'http://www.baidu.com'
# get和pose请求
response = requests.get(url)
# 请求成功
print(response)
# 获取网页文本内容
print(response.text)
# reason 原因
# 请求状态的说明
print(response.reason)
# link 跳转的地址
print(response.links)
# 请求历史
print(response.history)
# 请求编码格式
print(response.apparent_encoding)
# 设置响应的编码格式为网页的编码格式
response.encoding = response.apparent_encoding
# 获取网页内容（bytes形式）
print(response.content)
# 获取网页cookie
print(response.cookies)
# 获取响应头信息
print(response.headers)
# 获取请求的网址
print(response.request.url)




