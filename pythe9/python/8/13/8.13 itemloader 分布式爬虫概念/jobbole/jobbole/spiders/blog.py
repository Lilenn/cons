# -*- coding: utf-8 -*-
import scrapy
from ..items import JobboleItem
from ..items import ArticleItemLoader

class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    # 需求：获取所有文章的标题  图片地址 时间 详情页地址 收藏 点赞 评论
    def parse(self, response):
        item_list = response.xpath('//div[@class="post floated-thumb"]')
        for item in item_list :
            img = item.xpath('.//div[@class="post-thumb"]/a/img/@src').extract_first('')
            url = item.xpath('.//a[@class="archive-title"]/@href').extract_first('')
            yield  scrapy.Request(url=url,meta={'img':img},callback=self.get_detail_with_url)

        # next_url = response.xpath('//a[@class="next page-numbers"]/@href').extract()
        # if len(next_url) != 0 :
        #     page_url = next_url[0]
        #     yield scrapy.Request(url=page_url,callback=self.parse)

    def get_detail_with_url(self ,response):
        # img = response.meta['img']
        # # 标题
        # title = response.xpath('//div[@class="entry-header"]/h1/text()').extract_first('')
        # #时间
        # date_time = response.xpath('//div[@class="entry-meta"]/p/text()').extract_first('')
        # time = date_time.split('·')[0].strip()
        #
        # # 详情页地址
        # detail_url = response.url
        #
        # # 点赞数
        # dian_zan = response.xpath('//h10/text()').extract_first('')
        #
        # # 收藏数
        # book_mark = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract_first('')
        #
        # book_mark_array = book_mark.split(' ')
        # book_mark_num = 0
        # if len(book_mark_array[1]) != 0:
        #     book_mark_num = int(book_mark_array[1])
        #
        # # 评论数
        # comment = response.xpath('//a[@href="#article-comment"]/span/text()').extract_first('')
        # comment_arr = comment.split(' ')
        # comment_num = 0
        # if len(comment_arr[1]) != 0:
        #     comment_num = int(comment_arr[1])
        #
        # item = JobboleItem()
        # item['img'] = img
        # item['title'] = title
        # item['detail_url'] = detail_url
        # item['date_time'] = time
        # item['dian_zan'] = dian_zan
        # item['book_mark'] = book_mark_num
        # item['comment'] = comment_num


        # 创建ItemLoader的实例化对象的时候
        # 需要传入两个参数
        # 参数1：item的实例化对象 item里面为还要提取的数据的字段
        # 参数2：网页的源码
        item_loader  = ArticleItemLoader(item=JobboleItem(),response=response)
        # add_xpath()用于给一个field设置值
        # 后面需要追加两个参数
        # 参数1；需要设置的field的名称
        # 参数2：xpath路径
        item_loader.add_xpath('title','//div[@class="entry-header"]/h1/text()')

        item_loader.add_xpath('time','//div[@class="entry-meta"]/p/text()')

        item_loader.add_xpath('dianzan','//div[@class="post-adds"]//h10/text()')

        item_loader.add_xpath('book_mark_num','//span[contains(@class,"bookmark-btn")]/text()')

        item_loader.add_xpath('comment_num','//a[@href="#article-comment"]/span/text()')

        item_loader.add_value('img',[response.meta['img']])

        item_loader.add_value('detail_url',response.url)
        # 将itemloader加载器中保存的每一个field数据收集起来
        # 赋值给item 并且返回到管道
        item = item_loader.load_item()

        yield item