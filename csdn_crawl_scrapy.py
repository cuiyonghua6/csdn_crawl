#-*- coding:utf-8 -*-
import time
import random
import requests

import scrapy
from scrapy.http import HtmlResponse

HEADERS = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0'},
    {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'},
    {'User-Agent': 'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'},
    {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)'},
]


def run(url):
    try:
        res_text = requests.get(url=url, headers=random.choice(HEADERS))
        request = scrapy.Request(url=url)
        res = HtmlResponse(url=request.url, body=res_text.content, request=request, status=200)

        # 提取文章页的链接并爬取
        article_urls = res.xpath('//div[@class="article-list"]/div/h4/a/@href').extract()
        for article_url in article_urls:
            res_article = requests.get(url=article_url, headers=random.choice(HEADERS))
            article = scrapy.Request(url=article_url, headers=random.choice(HEADERS))
            article_text = HtmlResponse(url=article.url, body=res_article.content, request=article, status=200)
            title = article_text.xpath('//h1[@class="title-article"]/text()').extract_first()
            publish_time = article_text.xpath('//div[@class="bar-content"]/span[@class="time"]/text()').extract_first()
            print(publish_time, title)
    except:
        pass


if __name__ == '__main__':
    start = time.time()
    for i in range(1, 10):  # 建立任务链接
        url = 'https://blog.csdn.net/cui_yonghua/article/list/{}'.format(i)
        run(url=url)
    print('time cost:{}'.format(time.time()-start))