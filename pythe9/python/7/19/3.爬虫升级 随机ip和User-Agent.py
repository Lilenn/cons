import random
from urllib.request import Request,urlopen,ProxyHandler,build_opener

user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
]
headers = {
    'User-Agent':random.choice(user_agent_list)
}
ip_list = [
    '124.193.85.88:8080',
    '122.114.31.177:808',
    '111.155.116.207:8123',
    '220.249.185.178:9999'
]
# proxies 代理
proxies = {
    'http:':random.choice(ip_list)
}
# 设置爬虫目标 以及 用户标识
requset = Request('http://www.baidu.com',headers=headers)
# 创建ip代理对象
proxy_handler = ProxyHandler(proxies)
# urlopen(不支持http改机函数，cookie，验证， 代理等内容)
# 如果要使用这些内容，需要使用build_opener对象进行处理
opener = build_opener(proxy_handler)

response = opener.open(requset)

print(response.read().decode())
