# csdn_crawl
#### 用selenium,scrapy,requests,asnycio爬取csdn文章，并用bs4,lxml等提取数据

1. [csdn_parser.py](https://github.com/cuiyonghua6/csdn_crawl/blob/master/csdn_parser.py) : 用selenium爬取博客文章的标题和时间，并用selenium自带的解析，etree，bs4，scrapy框架自带的selector等4种方式来解析网页数据；
2. [csdn_crawl_selenium.py](https://github.com/cuiyonghua6/csdn_crawl/blob/master/csdn_crawl_selenium.py) : 使用selenium爬取csdn数据;
3. [csdn_crawl_requests.py](https://github.com/cuiyonghua6/csdn_crawl/blob/master/csdn_crawl_requests.py) : 使用requests爬取csdn数据;
4. [csdn_crawl_scrapy.py](https://github.com/cuiyonghua6/csdn_crawl/blob/master/csdn_crawl_scrapy.py) : 用scrapy爬取csdn数据；
5. [csdn_crawl_asyncio.py](https://github.com/cuiyonghua6/csdn_crawl/blob/master/csdn_crawl_asyncio.py) : 使用asyncio异步爬取csdn数据。


博客一：[用selenium爬取csdn博客文章，并用4种方法提取数据](https://blog.csdn.net/cui_yonghua/article/details/106765193)

博客二：[分别用selenium,requests,模拟scrapy,asyncio爬取CSDN用户的全部文章，并比较差异 (附python源码)](https://blog.csdn.net/cui_yonghua/article/details/106814205)
