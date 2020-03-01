import urllib
from bs4 import BeautifulSoup
from lxml import etree
from urllib.request import urlopen
import getpdf
#写headers防止拒绝访问
headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'}
import csv
basic='https://www.google.com/search?q=filetype:pdf+site:'
basic1='&start='

country_url=[]#有country code 的url
url=[]#完整的url
page_num=['0','10','20','30','40']#定义pagenum
#写完整的url basic+countrycode+basic1+page
with open('country_code.csv','r',encoding='utf8') as csvfile:
    reader=csv.DictReader(csvfile)
    column=[colunmn['Code'] for colunmn in reader]
print(column)

for h in column:
    url_code=basic+h+basic1
    country_url.append(url_code)

for i in country_url:
    for t in page_num:
        res= i+ t
        url.append(res)
print(url)
filenum=1001#写入html文件
for y in range(1000,1100):
    page1=urllib.request.Request(url[y], headers=headers)
    page=urllib.request.urlopen(page1)
    html=page.read()#下载相应的html
    #写入文件
    with open('page%d.html'%filenum,'wb') as f:
        f.write(html)
    filenum+=1
for file in range(1001,1101):
    html=etree.parse('page%d.html'%file, etree.HTMLParser())
    url_list=html.xpath('''//*[@id="rso"]/div/div/div/div/div/div[1]/a/@href''')
    for ur in url_list:
        fileObject = open('urllist.txt', 'a')
        fileObject.write(ur)
        fileObject.write('\n')
        fileObject.close()

# #写URL
# url=[]
# basic='https://www.google.com/search?q=filetype:pdf+site:uk&start='
# page_num=['0']
# for i in range(1,10):
#     number=str(i)+'0'
#     page_num.append(number)
# for n in page_num:
#     res=basic+n
#     url.append(res)
# filenum=1
# #下载相应的html
# for y in url:
#     page1=urllib.request.Request(y,headers=headers)
#     page=urllib.request.urlopen(page1)
#     html=page.read()
#
# #写入文件
#     with open('page%d.html'%filenum,'wb') as f:
#         f.write(html)
#     filenum=filenum+1

#转化成 'lxml.etree._Element' 然后把所有url写入一个text文件
# file=1
# for file in range(1,1246):
#     html=etree.parse('page%d.html'%file, etree.HTMLParser())
#     url_list = html.xpath('''//*[@id="rso"]/div/div/div/div/div/div[1]/a/@href''')
#     fileObject = open('urllist.txt','a')
#     for ur in url_list:
#         fileObject.write(ur)
#         fileObject.write('\n')
#     fileObject.close()
#     file=+1
# html = etree.HTML(html)
# print(type(html))
#转化成bytes类型
# result=etree.tostring(html)
# print(type(result))
# url_list=html.xpath('''//*[@id="rso"]/div/div/div/div/div/div[1]/a/@href''')
# # for index in range(len(url_list)):
# #     print(url_list[index].tag)
# #     print(url_list[index].attrib)
# #     print(url_list[index].text)
# print(url_list)