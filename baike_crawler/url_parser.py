# coding=utf-8
import re
import urlparse

import bs4


class UrlParser(object):
    def parse(self, url, url_cont):
        if url is None or url_cont is None:
            return
        soup = bs4.BeautifulSoup(url_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_data(url, soup)
        return new_urls, new_data

    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/item/.*'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(url,new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, url, soup):
        #title
        #summary
        res_data = dict()
        res_data['url'] = url
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        summary_node = soup.find('div', class_="lemma-summary")
        res_data['summary'] = summary_node.get_text()
        return res_data


'''
入口：https://baike.baidu.com/item/Python
url格式： /item/xxxx
数据格式： 标题<dd class='lemmaWgt-lemmaTitle-title'><h1>xxx</h1></dd>
         简介<div class="lemma-summary" label-module="lemmaSummary">xxx</div>
页面编码： UTF-8
'''
