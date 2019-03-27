# -*- coding: utf-8 -*-
import scrapy
from tutorial.items import QuoteItem


class QuotesSpider(scrapy.Spider):
    # 每个项目的唯一名称
    name = 'quotes'
    # 当前项目允许爬取的域名
    allowed_domains = ['quotes.toscrape.com']
    # 包含启动爬取的URL，起始链接
    start_urls = ['http://quotes.toscrape.com/']

    # 解析返回响应数据，进一步生成要处理的请求
    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            text = quote.css('.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tags .tag::text').extract()
            item = QuoteItem()
            item['text'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

        next = response.css('.pager .next a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url, self.parse)
