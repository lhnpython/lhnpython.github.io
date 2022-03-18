import requests as req
from lxml import etree
import re

def visit1(url):
    res = req.get(url).text
    etreeres = etree.HTML(res)
    idurl = etreeres.xpath('//*[@id="listdiv"]/table/tr/td[2]/a/@href')
    for endurl in idurl:
        visit2(endurl)

def visit2(endurl0):
    endurl = 'http://39.153.149.199:18180'+endurl0
    print(endurl)
    res2 = req.get(endurl).text.replace(' ', '').replace('\r', '').replace('\n', '')
    try:
        xm = re.findall('<tdclass="f-cb4"width="28%"><spanstyle="font-weight:bold">(.*?)</span></td>',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        xm = '-'
    try:
        mail = re.findall('<tdclass="f-cb4"title="#号改为@">(.*?)<br/>',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore").replace('#','@')
    except:
        mail = '-'
    f = open('内蒙古.csv','a')
    f.write(xm+",-,-,"+mail+"\n")
    print(xm,mail)
    f.close()

p = 1
while True:
    try:
        visit1('http://39.153.149.199:18180/dataservice/serve/request/law_lawyer?p='+str(p))
    except:
        pass
    p += 1
