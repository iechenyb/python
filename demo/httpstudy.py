import requests
import lxml
from lxml import etree
# import urllib2
# 获取源码
html = requests.get("https://blog.csdn.net/it_xf?viewmode=contents")
# 打印源码
print(html.text)
etree_html = etree.HTML(html.text)

content = etree_html.xpath('//*[@id="mainBox"]/main/div[2]/div[1]/h4/a/text()')
for each in content:
    print(each)

html = requests.get("https://blog.csdn.net/it_xf?viewmode=contents")
# print html.text

etree_html = etree.HTML(html.text)
content = etree_html.xpath('//*[@id="mainBox"]/main/div[2]/div/h4/a/text()')

for each in content:
    replace = each.replace('\n', '').replace(' ', '')
    if replace == '\n' or replace == '':
        continue
    else:
        print(replace)








#-------------------------
html = requests.get("https://www.xicidaili.com/nn/")
f=open("F:/project/python/demo/file/ip.txt",'a+',encoding='utf-8')
f.write(html.text)#追加不换行
# print html.text
print('get ip proxy')
etree_html = etree.HTML(html.text)
content = etree_html.xpath('//*[@id="ip_list"]/tbody/tr[2]/td[2]/text()')
for each in content:
    replace = each.replace('\n', '').replace(' ', '')
    if replace == '\n' or replace == '':
        continue
    else:
        print(replace)

   









        

#r a w

f=open("F:/project/python/demo/file/book.txt",'r',encoding='utf-8')
print(f.read()) #all content

f=open("F:/project/python/demo/file/book.txt",'r+',encoding='utf-8')
f.write('vvvv,wwwww')#追加不换行
f.write('\nvv2vv,wwwww')#追加换行
print(f.readline())


f=open("F:/project/python/demo/file/book.txt",'r',encoding='utf-8')
print(f.readlines())
