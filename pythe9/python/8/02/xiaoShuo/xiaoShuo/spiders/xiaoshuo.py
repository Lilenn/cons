# -*- coding: utf-8 -*-
import scrapy

from ..items import XiaoshuoItem
class XiaoshuoSpider(scrapy.Spider):
    name = 'xiaoshuo'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['https://tieba.baidu.com/p/5815118868']

    def parse(self, response):

        all_list = response.xpath('//div[@class="l_post l_post_bright j_l_post clearfix  "]')
        # print(all_content)
        for juti in all_list:
            item = XiaoshuoItem()
            username = juti.xpath('.//ul[@class="p_author"]/li[@class="d_name"]/a/text()').extract()[0]
            content_list = juti.xpath('.//div[@class="p_content  "]/cc/div[@class="d_post_content j_d_post_content "]/text()').extract()

            for content in content_list:
                if username == '乔深沉':
                   with open('知更鸟.txt','a',encoding='utf-8') as f:
                       f.write('{}'.format(content)+'\n')
                   f.close()

            item['username'] = username
            item['content_list'] = content_list

            yield item

        next_url = response.xpath('//ul[@class="l_posts_num"]/li[@class="l_pager pager_theme_5 pb_list_pager"]/a[text()="下一页"]/@href').extract()
        # print(next_url)
        if len(next_url) != 0 :
            url = 'https://tieba.baidu.com' + next_url[0]
            # print(url)
            yield scrapy.Request(url=url , callback=self.parse)












