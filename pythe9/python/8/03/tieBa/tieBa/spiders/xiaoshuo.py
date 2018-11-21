# -*- coding: utf-8 -*-
import scrapy
import re

class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/5815118868']
    f = open('tieba.txt', 'a', encoding='utf-8')
    def parse(self, response):
        # 找到指定类名 的div标签 该标签为贴吧内容的集合体
        div_list = response.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
        # print(div_list)
        # 找到作者
        for div in div_list:
            # 获取含有楼主标识类名的标签 该类名只有楼主才有
            author = div.xpath('.//div[@class="louzhubiaoshi_wrap"]').extract()
            # print(author)
            if len(author) !=0:
                # 获取标签内部全部文本的几种方式:
                # 1.获取最外面标签，遍历内部获取所有的子标签，获取标签文本
                # 2.正则去掉所有的标签 <.*?> re.comlipe.sub()
                # 3./text()获取标签的文本 //text()获取标签以及子标签的文本
                # 4.使用xpath（string（.））这种方式来获取所有文本并拼接
                content_list = div.xpath('.//div[@class="d_post_content j_d_post_content "]//text()').extract()
                # content_list = div.xpath('.//div[@class="d_post_content j_d_post_content "]').xpath('string(.)').extract()[0]+'\n'
                # print(content)
                remove = re.compile('\s')
                douhao = re.compile(',')
                content =''
                for string in content_list:
                   string = re.sub(remove,'',string)

                   string = re.sub(douhao,'',string)
                   content +=string +' '
                print(content)
                self.f.write(content)
                self.f.write('\n')


# https://tieba.baidu.com/p/5241715342


