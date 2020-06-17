# -*- coding:utf-8 -*-
import asyncio
import aiohttp
import time
import tqdm
from lxml import etree

headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gb2312,utf-8',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'Connection': 'Keep-alive'
           }

targe_url = []
for i in range(1, 10):  # 建立任务链接
    targe_url.append('https://blog.csdn.net/cui_yonghua/article/list/{}'.format(i))


async def run(url):
    async with aiohttp.ClientSession() as session:
        aiohttp.ClientTimeout(total=3)
        async with session.get(url, headers=headers) as response:
            res_text = await response.text()
            res = etree.HTML(res_text)

            # 提取文章页的链接并爬取
            article_urls = res.xpath('//div[@class="article-list"]/div/h4/a/@href')
            for article_url in article_urls:
                async with session.get(url=article_url, headers=headers) as article:
                    article_text = await article.text()
                    article_result = etree.HTML(article_text)
                    title = article_result.xpath('//h1[@class="title-article"]/text()')[0]
                    publish_time = article_result.xpath('//div[@class="bar-content"]/span[@class="time"]/text()')[0]
                    print(publish_time, title)


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()
    tasks = []
    for u in targe_url:
        tasks.append(asyncio.ensure_future(run(u)))
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    print('total {}pages,time cost:{}'.format(len(tasks), time.time()-start))