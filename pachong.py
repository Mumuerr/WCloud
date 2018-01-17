# -*- coding: utf-8 -*-

import urllib2
import re

#加载页面内容
def load_page(url):
    '''
    发送url请求
    返回url请求的静态html页面
    :param url:
    :return:
    '''
    user_agent = "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    headers = {"User-Agent" : user_agent}
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    html = response.read()
    #print html
    #print "--------------------------"
    getTitle(html)


#生成url地址，加载页面内容
def tieba_spider(url,startPage,endPage):
    for i in range(startPage,endPage + 1):
        page = (i - 1) * 50
        my_url = url + str(page)
        load_page(my_url)
        print "--------第%d页----------" % i

#获得贴吧的标题
def getTitle(html):
    info = re.findall(r'class="j_th_tit ">(.*?)</a>',html,re.S)
    for titleList in info:
        print titleList
        print "---------------"



if __name__ == '__main__':
    url = "http://tieba.baidu.com/f?kw=java&ie=utf-8&pn="
    startPage = 1
    endPage = 8
    tieba_spider(url, startPage, endPage)
    print "---------------------结束------------------"