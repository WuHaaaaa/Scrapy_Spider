<a href="https://996.icu"><img src="https://img.shields.io/badge/link-996.icu-red.svg"></a>


# Scrapy 学习
---
爬取腾讯招聘，并存储`.CSV`文件
```
scrapy crawl tencent -o tencent.csv
```

爬取quotes，并导出`.jsonline`格式
```
scrapy crawl quotes -o quotes.jl
```

+ 爬取腾讯招聘，并入库
```
scrapy crawl tencent
```

+ 爬取Quotes，并入库
```
scrapy crawl quotes
```

+ 设置随机User-Agent
```
scrapy crawl httpbin
```

+ 爬取360图片摄影页面
```
scrapy crawl images
```