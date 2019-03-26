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
            name = sel.xpath("./td[1]/a/text()").extract()[0]
            detailLink = sel.xpath("./td[1]/a/@href").extract()[0]
            catalog = sel.xpath("./td[2]/text()").extract()[0]
            recruitNumber = sel.xpath('./td[3]/text()').extract()[0]
            workLocation = sel.xpath('./td[4]/text()').extract()[0]
            publishTime = sel.xpath('./td[5]/text()').extract()[0]
            with open('tencetn.csv','a+') as f:
                f.write(name +","+ detailLink +","+ catalog +","+ str(recruitNumber) +","+ workLocation+","+ str(publishTime) + '\n')
            print(name," ",detailLink," ", catalog," ", recruitNumber, " ", workLocation, " ", publishTime)
            item = RecruitItem()
            item['name'] = name
            item['detailLink'] = detailLink
            item['catalog'] = catalog
            item['recruitNumber'] = recruitNumber
            item['workLocation'] = workLocation
            item['publishTime'] = publishTime

            yield item