# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class RecruitItem(scrapy.Item):
    """
    定义腾讯招聘爬取字段
    """
    name = scrapy.Field()
    detailLink = scrapy.Field()
    catalog = scrapy.Field()
    recruitNumber = scrapy.Field()
    workLocation = scrapy.Field()
    publishTime = scrapy.Field()


class QuoteItem(scrapy.Item):
    """
    定义爬取网站字段
    """
    text = scrapy.Field()
    author = scrapy.Field()
    tags = scrapy.Field()
    

