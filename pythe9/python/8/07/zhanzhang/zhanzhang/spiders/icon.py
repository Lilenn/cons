# -*- coding: utf-8 -*-
import scrapy

from ..items import ZhanzhangItem
class IconSpider(scrapy.Spider):
    name = 'icon'
    allowed_domains = ['sc.chinaz.com']
    start_urls = ['http://sc.chinaz.com/']

    def parse(self, response):
        icon_url = response.xpath('//li[@class="nos"]/a[3]/@href').extract_first('')
        full_url = 'http://sc.chinaz.com'+ icon_url
        yield scrapy.Request(url=full_url,callback=self.parse_icon_url)
    def parse_icon_url(self ,response):
        a_list = response.xpath('//ul[@class="pngblock imgload"]/li/span/a')
        for a in a_list :
            href = a.xpath('@href').extract_first('')
            title = a.xpath('text()').extract_first('')

            # yield scrapy.Request(url=url,callback=self.get_detail_with_url)
            yield scrapy.Request(
                url=href ,
                # meta 负责传递往下个方法发送的内容
                meta={
                    'title':title
                },
                callback=self.get_detail_with_url
            )
        next_url = response.xpath('//div[@class="fenye"]/a[text()="下一页"]/@href').extract()
        if len(next_url)!=0:
            url = 'http://sc.chinaz.com/tubiao/'+next_url[0]
            yield scrapy.Request(url=url,callback=self.parse_icon_url)
        # 获取全部图标的下载链接
    def get_detail_with_url(self ,response):
        title = response.meta['title']
        img_list = response.xpath('//div[@class="png_sl"]/div/img/@src').extract()
        print(img_list)
        for img in img_list:
            item = ZhanzhangItem()
            item['title'] = title
            item['img'] = [img]
            yield item
