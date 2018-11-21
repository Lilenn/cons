import re
import random
from urllib.request import Request,urlopen,ProxyHandler,build_opener
base_url = 'https://www.qiushibaike.com/article/120708350'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
ip_list = [
    '111.155.124.84:8123',
    '61.135.217.7:80',
    '218.241.234.48:8080'
]
proxies = {
    'http:':random.choice(ip_list)
}
def down_load_qiubai_info():
    request = Request( base_url,headers= headers)
    proxy_handler = ProxyHandler(proxies)
    opener = build_opener(proxy_handler)
    response =opener.open(request)
    code = response.read().decode()

    pattern = re.compile(r'<div class="replay">.*?<a.*?href=(.*?)>.*?',re.S)
    result = pattern.findall(code)

    for href in result:

        href = href.strip('\n')

        print('主页是',href)

down_load_qiubai_info()