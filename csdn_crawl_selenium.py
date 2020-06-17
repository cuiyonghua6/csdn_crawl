# -*- coding:utf-8 -*-
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree


def run(url):
    # 设置无头浏览器，字符编码，请求头等信息，防止反爬虫检测
    options = Options()
    options.add_argument('--headless')
    options.add_argument('lang=zh_CN.UTF-8')
    UserAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    options.add_argument('User-Agent=' + UserAgent)
    browser = webdriver.Chrome()
    browser.get(url)
    res = etree.HTML(browser.page_source)

    # 提取文章页的链接并爬取
    article_urls = res.xpath('//div[@class="article-list"]/div/h4/a/@href')
    for article_url in article_urls:
        browser.get(article_url)
        article_result = etree.HTML(browser.page_source)
        title = article_result.xpath('//h1[@class="title-article"]/text()')[0]
        publish_time = article_result.xpath('//div[@class="bar-content"]/span[@class="time"]/text()')[0]
        print(publish_time, title)
    browser.close()


if __name__ == '__main__':
    start = time.time()
    for i in range(1, 2):  # 建立任务链接
        url = 'https://blog.csdn.net/cui_yonghua/article/list/1'
        run(url=url)
    print('time cost:{}'.format(time.time() - start))