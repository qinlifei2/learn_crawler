#!/usr/bin/python
# coding=utf8
import logging
import re
import sys
import urllib2
import bs4
from url_controller import web_downloader_opener

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(message)s')
reload(sys)
sys.setdefaultencoding('utf-8')

# TODO
'''
解析价值信息
提取新url进入待爬
1、正则表达式
2、http.parse
3、beautifulsoup
4、lxml
'''

'''
DOM(document object model)
树形结构
<html>
<head>---<body>
...
'''

'''
bs4
1. 创建bs对象
2. 搜索节点 find/find_all
3. 访问节点---名称、属性、文字

<a herf='www.baidu.com' class='article_link'>Python</a>
节点名称----------------节点属性href/class--------节点内容
'''

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""


def web_reader_example(html_doc):
    soup = bs4.BeautifulSoup(
        html_doc,
        'html.parser',  # HTML解析器
        from_encoding='utf8'  # HTML编码
    )
    # node1 = soup.find('a', href='/view/123.htm')
    # node2 = soup.find('a', href=re.compile(r'/view/\d+\.htm'))
    # node3 = soup.find_all('div', class_='abc', string='Python')

    # node1.name #返回标签名
    # node2['href'] #查找节点属性
    # node3.get_text() #查找节点的文字
    links = soup.find_all('a')
    # 获取所有的链接
    for link in links:
        logging.info('name:{0}\tlink:{1}\ttext:{2}'.format(link.name, link['href'], link.get_text()))

    link = soup.find('a', href=re.compile(r'.*elsie'))
    #正则表达式
    logging.info('name:{0}\tlink:{1}\ttext:{2}'.format(link.name, link['href'], link.get_text()))

    link = soup.find('p', class_="title")
    #获取p段落文字
    logging.info('name:{0}\tlink:{1}\ttext:{2}'.format(link.name, link['class'], link.get_text()))




if __name__ == '__main__':
    web_reader_example(html_doc)
