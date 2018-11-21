from urllib.request import Request,urlopen
from urllib.parse import quote
import re
import string
# 处理Excel文件的必须模块
import xlwt
# 目的：1.爬取相关数据2.存储到excle
class ZLZP(object):
    def __init__(self,cityList = [],workname = ''):
        self.cityList = cityList
        self.workname= workname
        self.baseUrl = 'https://sou.zhaopin.com/jobs/searchresult.ashx?'
        self.cityString = ''
        self.currentIndex = 1
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }
        self.total_page = 1
        for cityName in cityList:
            if cityName == self.cityList[-1]:
                self.cityString += quote(cityName)
            else:
                self.cityString += quote(cityName)
                self.cityString +='%2B'

    def start_spider(self):
        # 5.第一次调用该方法
        # 获取第一个昂也源码 目的：得到总页数（信息数/ 每页显示的信息）
       code = self.get_code_with_url(1)
       # print(code)
       #  6.获取总页数
       self.get_total_page(code)
        # 7.创建一个excel对象，并设置编码格式 设置标题sheet
       sheet , workBook = self.open_excel_file()
       # 8.记录写入的行数 目的：让后来的数据插入到之前数据的后方
       record_row = 1
       # 获取每一页的数据
       for index in range(1, self.total_page +1):
           # 分别获取每一页的源码
           code = self.get_code_with_url(index)
           if code == None:
               continue
            # 分别剥离每一页的数据
           result_list = self.get_all_data(code)
           # 获取具体的每一条数据
           for job ,company , salary , location in result_list:
                sheet.write(record_row,0,job)
                sheet.write(record_row,1,company)
                sheet.write(record_row,2,salary)
                sheet.write(record_row,3,location)
                record_row +=1
       workBook.save('Python职位介绍表.xls')

    def get_all_data(self,code):
        pattern = re.compile(r'<table.*?class="newlist".*?>.*?<td class="zwmc".*?>.*?<a.*?>(.*?)</a>.*?<td class="gsmc">.*?<a.*?>(.*?)</a>.*?<td class="zwyx">(.*?)</td>.*?<td class="gzdd">(.*?)</td>', re.S)
        result = pattern.findall(code)
        print(result)
        list = []
        for value in result:
            jobName = value[0]
            companyNmae = value[1]
            salary = value[2]
            location = value[3]
            pattern = re.compile(r'<.*?>',re.S)
            jobName = re.sub(pattern,'',jobName)
            companyNmae = re.sub(pattern,'',companyNmae)
            list.append([jobName,companyNmae,salary,location])
        return list

# 创建excel
    def open_excel_file(self):
        # 创建工作表对象，并设置编码方式为utf-8
        workBook = xlwt.Workbook(encoding='utf-8')
        # 新增sheet
        sheet = workBook.add_sheet('python职位表')
        # 值1：行 索引从0开始
        # 值2. 列 索引从0开始
        # 值3. 标题
        sheet.write(0,0,'职位名称')
        sheet.write(0,1,'公司名称')
        sheet.write(0, 2, '薪资水平')
        sheet.write(0, 3, '工作地点')
        return  sheet , workBook

    def get_total_page(self,code):
        # pattern = re.compile(r'<table.*?class="newlist".*?>.*?<td class="zwmc".*?>.*?<a.*?>(.*?)</a>', re.S)
        pattern = re.compile(r'<span class="search_yx_tj">.*?<em>(.*?)</em>',re.S)
        result = pattern.findall(code)
        print(result)
        number = int(result[0])
        if number :
            if number % 60 == 0:
                self.total_page = number // 60
            else:
                self.total_page = number //60 +1
        print(self.total_page)

    def get_code_with_url(self,pageIndex):
        full_url = self.baseUrl + 'jl=' + self.cityString + '&kw=' + self.workname + '&p=' + str(pageIndex)
        print(full_url)
        resquse = Request(full_url,headers=self.headers)

        try:
            response = urlopen(resquse)
            code = response.read().decode()
        except Exception as e:
            print('请求失败',e)
        else:
            return code
citys = []
while True:
    city = input('请输入你想去的城市')
    if city =='E':
        break
    citys.append(city)
job = input('请输入你喜欢的工作')
zp = ZLZP(citys , job)
zp.start_spider()