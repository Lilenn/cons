# 作业：奇书网 ，玄幻奇幻类小说
# 将：小说名，点击次数，文件大小，书籍类型。更新日期，连载状态。书籍作者，小说简介，下载地址存储到excel里面

from lxml import etree
import requests
import xlwt

class XHQH(object):
    def __init__(self):
        self.base_url = 'https://www.qisuu.la/'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.current_page = 1
        self.recode = 1
        self.sheet = None
        self.workBook = None
    #
    def start_downLoad(self):
        self.get_excel()
        frist_page = 'soft/sort01/index_1.html'
        self.get_code_with_url(frist_page)
        #
        self.workBook.save('奇书网小说.xls')

    def get_excel(self):

        self.workBook = xlwt.Workbook(encoding='utf-8')
        self.sheet = self.workBook.add_sheet('奇幻小说类')
        self.sheet.write(0, 0, '小说名称')
        self.sheet.write(0, 1, '作者')
        self.sheet.write(0, 2, '小说简介')
        self.sheet.write(0, 3, '书籍类型')
        self.sheet.write(0, 4, '连载状态')
        self.sheet.write(0, 5, '更新日期')
        self.sheet.write(0, 6, '文件大小')
        self.sheet.write(0, 7, '点击次数')
        self.sheet.write(0, 8, '在线阅读地址')

    def get_code_with_url(self,url):
        full_page_url = self.base_url + url
        response = requests.get(full_page_url,headers = self.headers).content
        code =etree.HTML(response)
        self.get_lianjie_with_code(code)

    def get_lianjie_with_code(self,code):
        print('正在下载第{}页'.format(self.current_page))
        lj_list = code.xpath('//div[@class="listBox"]/ul/li/a/@href')
        # 拼接小说具体内容网址，并取出相关简介
        for juti in lj_list:
            xiaoshuo_url = self.base_url +juti
            response = requests.get(xiaoshuo_url,headers = self.headers).content
            root = etree.HTML(response)
            # print(root)
            content_list = root.xpath('//div[@class="show"]')
            # print(content_list)
            for content in content_list:
                name = content.xpath('.//div[@class="detail_right"]/h1/text()')[0]
                jianjie = content.xpath('.//div[@class="showInfo"]/p/text()')[0].replace(' ','')
                download = content.xpath('.//div[@class="showDown"]/ul/li/a[@class="downButton"]/@href')[0]
                download = self.base_url+download
                all_content = content.xpath('.//ul/li[@class="small"]/text()')[:-1]
                rq = all_content[0]
                daxiao = all_content[1]
                type = all_content[2]
                date = all_content[3]
                lZZT = all_content[4]
                zuozhe = all_content[5]
                # print(name)
                # print(zuozhe)
                # print(jianjie)
                # print(rq)
                # print(daxiao)
                # print(date)
                # print(lZZT)
                # print(type)
                # print(download)

                # 将相关内容写入excel表格中
                self.sheet.write(self.recode, 0, name)
                self.sheet.write(self.recode, 1, zuozhe)
                self.sheet.write(self.recode, 2, jianjie)
                self.sheet.write(self.recode, 3, type)
                self.sheet.write(self.recode, 4, lZZT)
                self.sheet.write(self.recode, 5, date)
                self.sheet.write(self.recode ,6, daxiao)
                self.sheet.write(self.recode, 7, rq)
                self.sheet.write(self.recode , 8, download)
                self.recode +=1

        self.current_page +=1
        self.get_page_with_code(code)

    def get_page_with_code(self,code):
        next_page = code.xpath('//div[@class="tspage"]/a')
        next_page = next_page.xpath('.//')
        if len(next_page) == 0:
            print('已经为最后一页')
            return
        print(next_page)
        self.get_code_with_url(next_page[0])


xiaoshuo = XHQH()
xiaoshuo.start_downLoad()