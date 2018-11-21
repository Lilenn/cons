import os
import requests
from lxml import etree

# 下载电影海报
def download_img(db_id,db_title,db_img_addr,headers):

    # 如果不存在图片文件夹，则自动创建
    if os.path.exists('./Top250_movie_images/'):
        pass
    else:
        os.makedirs('./Top250_movie_images/')

    # 获取图片二进制数据
    image_data = requests.get(db_img_addr,headers=headers).content
    # 设置画报存储的路径和名称
    image_path = './Top250_movie_images' + db_id[0] + '_' + db_title[0] + '.jpg'
    # 存储海报图片
    with open(image_path,'wb+') as f:
        f.write(image_data)

# 根据url获取数据，并打印到屏幕上，保存为文件
def get_movies_data(url,headers):

    # 获取页面响应的内容
    db_response = requests.get(url,headers=headers)

    # 将获取的源码转化为etree
    db_response_etree = etree.HTML(db_response.content)

    # 提取所有的电影数据
    db_movie_items = db_response_etree.xpath('//*[@id="content"]/div/div[1]/ol/li/div[@class="item"]')
    # 遍历电影数据列表
    for db_movie_item in db_movie_items:
        db_id = db_movie_item.xpath('div[@class="pic"]/em/text()')
        db_title = db_movie_item.xpath('div[@class="info"]/div[@class="hd"]/a/span[1]/text()')
        db_score = db_movie_item.xpath('div[@class="info"]/div[@class="bd"]/div/span[@class="rating_num"]/text()')
        db_desc= db_movie_item.xpath('div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()')
        db_img_addr = db_movie_item.xpath('div[@class="pic"]/a/img/@src')

        print('编号:',db_id,'标题:',db_title,'评分:',db_score,'电影描述:',db_desc)

        with open('./douban_movie_top250.txt','ab+') as f:
            tmp_data = '编号：' + str(db_id) + '标题：' + str(db_title)+ \
                '评分：' +str(db_score) + '电影描述：' +str(db_desc) + '\n'
            f.write(tmp_data.encode('utf-8'))
            db_img_addr = str(db_img_addr[0].replace("\'", ""))
            download_img(db_id,db_title,db_img_addr,headers)

def main():
    #使用列表生成式，生成待爬去的页面url的列表
    urls = ['https://movie.douban.com/top250?start=' + str(i*25) for i in range(10)]

    #设置请求头
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
    }
    #为了避免重复运行程序，造成内容的重复，这里把上次的文件清除（可跳过）
    if os.path.isfile('./douban_movie_top250.txt'):
        os.remove('./douban_movie_top250.txt')

    #从列表取出url进行爬取
    for url in urls:
        get_movies_data(url,headers)

if __name__ == '__main__':
    main()
