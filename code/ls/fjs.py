import requests as req
from lxml import etree
import re

cityl = ['三明', '泉州', '福州', '厦门', '莆田', '漳州', '南平', '龙岩', '宁德']

def visit1(url, c):
    res = req.get(url).text
    etreeres = etree.HTML(res)
    idurllist = etreeres.xpath('//ul[@class="firm-ul"]/li/a/@href')
    if idurllist == []:
        return False
    for idurl in idurllist:
        try:
            visit2("http://220.160.52.136:97/"+idurl, c)
        except:
            print("None")
    return True

def visit2(infourl, c):
    print(infourl)
    res1 = req.get(infourl).text.replace(' ', '').replace('\r', '').replace('\n', '')
    try:
        mail = re.findall('电子邮箱：(.*?)<', res1)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        mail = '-'
    try:
        phone = re.findall('联系电话：(.*?)<', res1)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        phone = '-'
    try:
        zylb = re.findall('执业类别：(.*?)<', res1)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        zylb = '-'
    try:
        name = re.findall('<divclass="firm-li-tit">(.*?)</div>', res1)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        name = '-'
    f = open("{}.csv".format(str(c)), 'a')
    f.write(name+","+zylb+","+phone+","+mail+"\n")
    f.close()
    print(name,zylb,mail,phone)


for c in cityl:
    print(c)
    alive = True
    p = 1
    while alive == True:
        print("Page "+str(p))
        try:
            alive = visit1('http://220.160.52.136:97/LawyerList.aspx?current={}&CityId='.format(str(p))+str(c), c)
        except:
            pass
        p += 1
