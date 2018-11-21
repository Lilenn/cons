from urllib.request import Request,urlopen

url = 'http://www.baidu.com'
# 如果直接这样写，等于告诉网页获取网页内欧人难过的不是自然人而是程序
# 程序自带User-Agent:Python urllib/3.6

hearders = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
# 替换程序的User-Agent
requset = Request(url,headers=hearders)
response = urlopen(requset)
# decode 解码 encode 编码
print(response.read().decode())

# 爬虫\反爬流程：
# 1.禁止爬虫 解决办法： 伪装User-Agend，进行爬虫
# 2.判断同一个User-Agent 是否多次访问 解决办法： 换成不同的User-Agent进行访问
# 3.判断同一个ip是否多次访问 解决办法：使用不同ip进行访问


