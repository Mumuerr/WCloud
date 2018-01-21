#coding=utf-8
import requests
import re
import sys

reload(sys)

sys.setdefaultencoding('utf-8')

html = requests.get('http://acl2016.org/index.php?article_id=68')
html.encoding = 'utf-8'

html_doc = html.text

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc,'html.parser')

#print(soup.prettify()) #所有html文档内容
#print(soup.get_text()) #所有文字内容
#print(soup.p)   <p><a href="#long_papers">Long papers</a></p>

#for link in soup.find_all('p'):
#    res = r'<p>(.*?)<br/>'
#    m = re.findall(res,link,re.S|re.M)
#    print m
p_con = soup.find_all('p')

res_tr = r'<p>(.*?)<'
m_tr = re.findall(res_tr, html_doc, re.S | re.M)
for line in m_tr:
    print line
    title_f = open("title_acl_2016.txt",'a')
    title_f.write('\n'+line)
    title_f.close()
