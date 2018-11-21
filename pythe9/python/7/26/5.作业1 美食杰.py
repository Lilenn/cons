# 1. 美食杰网站爬取菜谱名及人气，以 “莴笋炒蛋（2047人气）” 形式打印，并将图片链接与菜谱名称存入数据库
#
# 2.斗鱼直播网站   爬取  “分类“ 页面的全部图片和名字，然后爬取 “分类”页面中任意一个类型游戏的 全部图片和名字（即该游戏当前所有的直播间封面和对应标题），最后将两次爬取的数据存入对应的Excel表格
# 美食杰作业爬取的数据存入数据库，斗鱼作业爬取的数据保存到Excel表格
# https://www.meishij.net/chufang/diy/?&page=2
import shutil,os
from bs4 import BeautifulSoup
from urllib.request import Request,urlopen,urlretrieve
import sqlite3

class DBManager(object):
    connect = sqlite3.connect('msDB')
    cursor = connect.cursor()
    @classmethod
    def create_db(cls):
        cls.cursor.execute('create table if not exists meishiTable (name text , lianjie text)')
        cls.connect.commit()

    @classmethod
    def insert_info(cls,image_alt,image_src):
        cls.cursor.execute('insert into meishiTable (name , lianjie) VALUES ("{}","{}")'.format(image_alt,image_src))
        cls.connect.commit()

    @classmethod
    def close_db(cls):
        cls.cursor.close()
        cls.connect.close()

class Image_download(object):
    def __init__(self):
        self.base_url = 'https://www.meishij.net/chufang/diy/'
        self.current_page = 1
    def start_downLoad(self):
    # 如果存在，则删除；如果不存在，就创建
        if os.path.exists('meishi'):
            shutil.rmtree('meishi',True)
        os.mkdir('meishi')
        os.chdir('meishi')
        first_page = '?&page=1'
        self.get_page_code_with_url(first_page)
    def get_page_code_with_url(self,url):
        full_url = self.base_url + url
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        request = Request(full_url,headers=headers)
        try:
            response = urlopen(request)
            code = response.read().decode()
        except Exception as e :
            print('请求失败:',e)
        else:
            self.get_data_with_url(code)
    def get_data_with_url(self,code):
        print('正在下载第{}页...'.format(self.current_page))
        soup = BeautifulSoup(code,'lxml')
        page_name ='Page{}'.format(self.current_page)
        os.mkdir(page_name)
        os.chdir(page_name)
        image_list = soup.select('div.listtyle1 a img')
        for image in image_list:
            image_alt = image.get('alt')
            image_src = image.get('src')
            DBManager.insert_info(image_alt, image_src)
            # 保存图片到文件夹
            image_alt = image_alt.split('(')[0]+'.jpg'
            urlretrieve(image_src,image_alt)

        os.chdir(os.path.pardir)
        self.current_page +=1
        self.get_next_page(code)
    def get_next_page(self,code):
        soup = BeautifulSoup(code,'lxml')
        naxt_page = soup.select('a.next')[0]
        url =naxt_page.get('href')
        if len(url) == 0:
            print('已经为最后一页')
            return
        self.get_page_code_with_url(url)

DBManager.create_db()
download = Image_download()
download.start_downLoad()
DBManager.close_db()