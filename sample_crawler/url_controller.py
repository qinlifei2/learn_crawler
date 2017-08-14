#!/usr/bin/python
# coding=utf8
import logging
import sys
import urllib2

logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(message)s')
reload(sys)
sys.setdefaultencoding('utf-8')


# TODO
# 防止重复抓取、循环抓取
# 1、添加新url到待爬取集合
# 2、判断url是否在容器中
# 3、判断是否还有待爬url
# 4、获取待爬url
# 5、将待爬取url添加到已爬取集合



# 实现方式
# 1.内存
# 2.mysql
# 3.redis

def web_downloader(url):
    response = urllib2.urlopen(url)
    logging.info('state is {0}'.format(response.getcode()))
    logging.info('content is {0}'.format(response.read()))


def web_downloader_request(url):
    # 创建request对象
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0')
    response = urllib2.urlopen(request)
    logging.info('state is {0}'.format(response.getcode()))
    logging.info('content is {0}'.format(response.read()))



def web_downloader_opener(url):
    '''
    需要cookie，使用HTTPCoockieProcessor
    需要代理，使用ProxyHandler
    需要加密，使用HTTPSHandler
    需要跳转，使用HTTPRedirectHandler
    '''
    import cookielib
    cj = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    urllib2.install_opener(opener)
    web_downloader(url)
    logging.info('cookie is {0}'.format(cj))


if __name__ == '__main__':
    url = 'http://www.baidu.com'
    logging.info('test method {0}'.format(1))
    web_downloader(url)
    logging.info('test method {0}'.format(2))
    web_downloader_request(url)
    logging.info('test method {0}'.format(3))
    web_downloader_opener(url)
