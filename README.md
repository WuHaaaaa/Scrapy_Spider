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