import re
from urllib.request import urlopen,Request,build_opener

class QSBKSpide(object):
    def __init__(self):
        self.url = 'http://alfheim.cc/aggo-5.html/7/'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }

    def get_info_from_url(self):
        request = Request(self.url,headers=self.headers)
        response = urlopen(request)
        try:
            code = response.read().decode()
        except Exception as e:
            print('未获取搜索内容',e)
        else:
            return code

    def get_geci_info_from_code(self,code):
        # print(code)

        pattern = re.compile(r'<div class="single-content">(.*?)</div>',re.S)
        result = pattern.findall(code)
        print(result)


gcSpider = QSBKSpide()
code = gcSpider.get_info_from_url()
gcSpider.get_geci_info_from_code(code)
