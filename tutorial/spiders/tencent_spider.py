import scrapy
from tutorial.items import RecruitItem

class RecruitSpider(scrapy.Spider):
    """
    创建一个Spider，继承自scrapy.Spider
    """
    # spider名称
    name = "tencent"
    # 
    allowed_domains = ["hr.tencent.com"]
    # 初始URL列表
    start_urls = [
        "https://hr.tencent.com/position.php?&start=0#a",
    ]


    def parse(self,response):
        """
        解析返回的网页数据，提取结构化数据，生成下一页需要请求的URL
        """
        for sel in response.xpath('//*[@class="even"]'):
            name = sel.xpath("./td[1]/a/text()").extract_first()
            detailLink = sel.xpath("./td[1]/a/@href").extract_first()
            catalog = sel.xpath("./td[2]/text()").extract_first()
            recruitNumber = sel.xpath('./td[3]/text()').extract_first()
            workLocation = sel.xpath('./td[4]/text()').extract_first()
            publishTime = sel.xpath('./td[5]/text()').extract_first()
            item = RecruitItem()
            item['name'] = name
            item['detailLink'] = detailLink
            item['catalog'] = catalog
            item['recruitNumber'] = recruitNumber
            item['workLocation'] = workLocation
            item['publishTime'] = publishTime

            yield item

        next = response.css('.pagenav #next::attr(href)').extract_first()
        url = "https://hr.tencent.com/" + next
        yield scrapy.Request(url,self.parse)