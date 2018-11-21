#  文件处理的高级模块 功能比os更加强大
import  shutil, os
from bs4 import BeautifulSoup
# urlretrieve 可以用来下载图片
from urllib.request import Request,urlopen,urlretrieve
class Image_downLoad(object):
    def __init__(self):
        self.base_url = 'http://www.ivsky.com/'
        self.current_page = 1
    def start_downLoad(self):
        # 判断是否存在指定文件夹 如果存在择删除
        if os.path.exists('image'):
            # rm remove 删除 tree 树
            # 删除树状结构的文件夹
            # True 忽略错误信息
            shutil.rmtree('image',True)
        os.mkdir('image')
        # 如果要对某一个文件夹内部进行操作
        # 首先要进入到该文件夹内部
        os.chdir('image')
        frist_page = 'tupian/index_1.html'
        self.get_page_code_with_url(frist_page)
    def get_page_code_with_url(self,url):
        full_url = self.base_url + url
        print(full_url)
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
        }
        request = Request(full_url,headers=headers)
        try:
            response = urlopen(request)
            code = response.read().decode()
        except Exception as e :
            print('请求失败:',e)
        else:
            self.get_data_with_code(code)
    def get_data_with_code(self,code):
        print('正在下载第{}页...'.format(self.current_page))
        soup = BeautifulSoup(code,'lxml')
        page_name = 'Page{}'.format(self.current_page)
        os.mkdir(page_name)
        os.chdir(page_name)
        image_list = soup.select('ul.ali a img')
        for image in image_list:
            image_src = image.get('src')
            image_alt = image.get('alt')
            image_alt = image_alt.split('(')[0]+'.jpg'
            print(image_src)
            print(image_alt)
            urlretrieve(image_src,image_alt)
         # 将光标移到pardir 父级文件夹外面
        os.chdir(os.path.pardir)
        # 告诉下一页当前是哪一页
        self.current_page += 1
        self.get_next_page(code)
    def get_next_page(self,code):
        # 强当前页码转化成soup对象 进行解析
        # 从所有符合要求的标签中找到第一个
        soup = BeautifulSoup(code,'lxml')
        next_page = soup.select('a.page-next')[0]
        # 获取该标签的href属性
        url = next_page.get('href')
        self.get_page_code_with_url(url)


download = Image_downLoad()
download.start_downLoad()
