# -*- coding: utf-8 -*-
import scrapy
from ..items import BoleItem
from ..items import ArticleItemLoad

class BlogSpider(scrapy.Spider):
    name = 'blog'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/category/career/']
    # 需求：获取所有文章的标题  图片地址 时间 详情页地址 收藏 点赞 评论
    def parse(self, response):
        all_info = response.xpath('//div[@class="post floated-thumb"]')
        for info in all_info :
            img = info.xpath('.//div[@class="post-thumb"]/a/img/@src').extract_first('')
            # print(img)
            url = info.xpath('.//a[@class="archive-title"]/@href').extract_first('')
            # print(url)
            yield scrapy.Request(url=url,meta={'img':img},callback=self.get_detail_url)
    def get_detail_url(self,response):
        # img = response.meta['img']
        # print(img)
        item_loader = ArticleItemLoad(item=BoleItem(),response=response)
        item_loader.add_value('img',[response.meta['img']])
        item_loader.add_xpath('title','//div[@class="entry-header"]/h1/text()')
        item_loader.add_xpath('data','//p[@class="entry-meta-hide-on-mobile"]/text()')
        item_loader.add_value('detail_url',[response.url])
        item_loader.add_xpath('zan','//span[contains(@class,href-style)]//h10/text()')
        item_loader.add_xpath('cang','//span[contains(@class,bookmark-btn)]/text()')
        item_loader.add_xpath('lun','//a[@href="#article-comment"]/span/text()')

        item = item_loader.load_item()
        yield item

