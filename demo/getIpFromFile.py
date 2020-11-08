import requests
import lxml
from lxml import etree
# import urllib2
# 获取源码


#-----------------------------------------------
f = open("file/contract.html","r",encoding="utf-8") #读取文件
f = f.read()#把文件内容转化为字符串
html = etree.HTML(f)#把字符串转化为可处理的格式

def test1(html):
    result = html.xpath('//tbody/tr/td/text()') #把html文件中所有表格数据都存入result中，需注意result是一个列表
    num = len(result)
    i = 1
    while 6 * i <= num:  #示例html文件中每一行有6列，所以以6个单元为一组对列表进行分片读取，需注意，这种方法需要保证表格中没有空元素或者和开发约定好假如有空元素以空格为占位符
        first = (i - 1) * 6
        last = i * 6 - 1
        print(result[first:last + 1])
        i += 1
def test2(html):
    result = html.xpath('//tbody/tr/td[@lang]/text()')
    result2 = html.xpath('//tbody/tr/td[@lang=20]/text()')
    result3 = html.xpath('//tbody/tr/*/text()')
    print(result)
    print(result2)
    print(result3)
    
test1(html)
print('-------------------1-------------------')
test2(html)
print('-------------------2-------------------')





def test4(html,collen):
    result = html.xpath('//table/tr/td[2]/text()') #把html文件中所有表格数据都存入result中，需注意result是一个列表
    num = len(result)
    i = 1
    while collen * i <= num:  #示例html文件中每一行有6列，所以以6个单元为一组对列表进行分片读取，需注意，这种方法需要保证表格中没有空元素或者和开发约定好假如有空元素以空格为占位符
        first = (i - 1) * collen
        last = i * collen - 1
        print(result[first:last + 1])#数组
        i += 1


def test5(html,collen,exp):
    result = html.xpath(exp) #把html文件中所有表格数据都存入result中，需注意result是一个列表
    num = len(result)
    i = 1
    while collen * i <= num:  #示例html文件中每一行有6列，所以以6个单元为一组对列表进行分片读取，需注意，这种方法需要保证表格中没有空元素或者和开发约定好假如有空元素以空格为占位符
        first = (i - 1) * collen
        last = i * collen - 1
        print(result[first:last + 1])#数组
        i += 1







#-------------------------
def get_text_link_from_sel(r,sel):
    mylist = []
    try:
        results = r.html.find(sel)
        for result in results:
            mytext = result.text
            mylink = list(result.absolute_links)[0]
            mylist.append((mytext, mylink))
        return mylist
    except:
        return None


f=open("F:/project/python/demo/file/ip.txt",'r',encoding='utf-8')
# print html.text
print('get ip proxy')
etree_html = etree.HTML(f.read())# 如何把文本转化为hml
test4(etree_html,10)#10个一组
print('-------------------3-------------------')

test4(etree_html,100)#100个一组
print('-------------------4-------------------')
test5(etree_html,100,'//table/tr/td[2]/text()')#100个一组

print('-------------------5-------------------')
test5(etree_html,100,'//table/tr/*/a/text()')#100个一组







        
