import xlwt
import requests
from lxml import etree
from fake_useragent import  UserAgent

class DBMoive(object):
    def __init__(self):
        self.base_url = 'https://movie.douban.com/top250'
        self.current_page = 1
        self.headers = UserAgent()
        self.wookBook = None
        self.sheet = None
        self.recode = 1
    def start_load_dbmoive(self):
        self.get_excle()
        # 第一次调用该方法，url值可以不用传
        self.get_code_with_url()

        self.workBook.save('豆瓣top251.xls')
    def get_excle(self):
        self.workBook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workBook.add_sheet('电影排行榜')
        self.sheet.write(0 , 0 ,'排名')
        self.sheet.write(0, 1 ,'影片')
        self.sheet.write(0 , 2, '导演和演员')
        self.sheet.write(0 , 3 ,'评分')
        self.sheet.write(0 ,4 ,'评论人次')

    def get_code_with_url(self,url = ''):
        headers ={
            # 随机获取一个用户标识
            'User-Agent':self.headers.random
        }
        full_url = self.base_url + url
        response = requests.get(full_url,headers= headers).text
        code = etree.HTML(response)
        item_div = code.xpath('//div[@class="item"]')
        for tag in item_div:
            # . ：表示从当前节点开始取
            # .. ：表示从父节点开始取
            rank = tag.xpath('.//em[@class=""]/text()')[0]
            print(rank)
            moive_name = tag.xpath('.//div[@class="hd"]/a/span/text()')
            # print(moive_name)
            name = ''
            for moive in moive_name:
                name += moive

            creater = tag.xpath('.//div[@class="bd"]/p[@class=""]/text()')[0]
            creater = creater.strip('\n').replace(' ','')

            start = tag.xpath('.//span[@class="rating_num"]/text()')[0]

            comment_num = tag.xpath('.//div[@class="star"]/span[last()]/text()')[0]
            comment_num = comment_num[0: -3]

            self.sheet.write(self.recode , 0, rank)
            self.sheet.write(self.recode , 1 , name)
            self.sheet.write(self.recode , 2 , creater)
            self.sheet.write(self.recode , 3, start)
            self.sheet.write(self.recode , 4 , comment_num)
            self.recode +=1
        self.get_next_page(code)

    def get_next_page(self,code):
        next_url = code.xpath('//span[@class="next"]/a/@href')
        if len(next_url) == 0:
            print('已经为最后一页')
            return
        self.get_code_with_url(next_url[0])

moive = DBMoive()
moive.start_load_dbmoive()