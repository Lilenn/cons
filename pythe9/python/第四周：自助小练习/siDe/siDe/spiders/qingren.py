# -*- coding: utf-8 -*-
import scrapy
import re
from siDe.items import SideItem
class QingrenSpider(scrapy.Spider):
    name = 'qingren'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/5825744040']
    # f = open('走不出你.txt','a',encoding='utf-8')
    def parse(self, response):
        # 获取小说楼主的名字以及小说内容
        div_list = response.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
        # print(div_list)
        for div in div_list:
            img =div.xpath('.//li[@class="icon"]/div/a[@class="p_author_face "]/img/@src').extract_first()
            # print(img)
            author = div.xpath('.//div[@class="louzhubiaoshi_wrap"]').extract()
            # print(author)

            if len(author) != 0:
#               xpath('string(.)')提取多个子节点中的文本
                content_list = div.xpath('.//div[@class="d_post_content j_d_post_content "]').xpath('string(.)').extract()
                remove = re.compile('\s')
                content = ''
                for string in content_list:
                    string = re.sub(remove,'',string)
                    content += string
                # print(content)

                item = SideItem()
                item['content'] = [content]
                item['img'] = [img]
                yield item

                # self.f.write(content)
                # self.f.write('\n')

        next_url = response.xpath('//div[@class="l_thread_info"]/ul/li/a[text()="下一页"]/@href').extract()
        if len(next_url) != 0:
            url = 'https://tieba.baidu.com' + next_url[0]
            yield scrapy.Request(url= url ,callback=self.parse)



                 # content_list = div.xpath('.//div[@class="p_content  "]/cc/div/text()').extract()
                 # remove = re.compile(r'\s')
                 # douhao = re.compile(',')
                 # content = ''
                 # for string in content_list:
                 #    string = re.sub(remove, '', string)
                 #    string = re.sub(douhao, '', string)
                 #    content += string
                 # print(content)
# -----------------------------------------------//text()形式--------------------------------------------------------------------
#                 content_list = div.xpath('.//div[@class="p_content  "]//text()').extract()
#                 remove = re.compile(r'\s')
#                 douhao = re.compile(',')
#                 content = ''
#                 for string in content_list:
#                     string = re.sub(remove,'',string)
#                     string = re.sub(douhao,'',string)
#                     content += string
#                 print(content)

# -------------------------------------------------正则去掉<.*?>--------------------------------------------------------
#                  content_list = div.xpath('.//div[@class="p_content  "]/cc/div').extract()
#                  remove = re.compile('\s')
#                  br = re.compile(r'<.*?>')
#                  content = ''
#                  for string in content_list:
#                     string = re.sub(remove,'',string)
#                     string = re.sub(br,'',string)
#                     # strip去除的为首位的指定内容（默认为空格or换行符），而不能去除中间的位置
#                     # string = string.strip(' ')
#                     content += string +'\n'
#                  print(content)
