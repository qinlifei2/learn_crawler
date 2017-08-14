#!/usr/bin/python
# coding=utf8
import logging
import re
import sys
import urllib2
import bs4

import url_downloader, url_manager, url_outputer, url_parser

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(message)s')
reload(sys)
sys.setdefaultencoding('utf-8')


#TODO:
'''
爬取Python 百度百科页面抓取爬虫
确定目标
分析目标---url格式/数据格式/网页编码
编写代码
执行爬虫
'''


'''
入口：https://baike.baidu.com/item/Python
url格式： /item/xxxx
数据格式： 标题<dd class='lemmaWgt-lemmaTitle-title'><h1>xxx</h1></dd>
         简介<div class="lemma-summary" label-module="lemmaSummary">xxx</div>
页面编码： UTF-8
'''


class BaikeCrawler(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = url_downloader.UrlDownloader()
        self.parser = url_parser.UrlParser()
        self.outputer = url_outputer.UrlOutputer()


    def crawl(self, root_url):
        count = 0
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                #判断是否还有待爬url
                new_url = self.urls.get_new_url()
                url_cont = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, url_cont)
                self.outputer.collector(new_data)
                #解析url，获得网页内容，收集新的url待爬
                self.urls.add_new_urls(new_urls)

                count += 1#计数
                logging.info('Has crawled {0} url'.format(count))
                if count == 100:
                    logging.info('Finish crawling')
                    break
            except:
                logging.info('Crawling failed')
        self.outputer.output_url()



if __name__ == '__main__':
    root_url = 'https://baike.baidu.com/item/Python'
    obj_crawler = BaikeCrawler()
    obj_crawler.crawl(root_url)