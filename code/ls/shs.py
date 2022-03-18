import requests as req
from lxml import etree
import re

cityl = ['黄浦/310101','徐汇/310104','长宁/310105','静安/310106','普陀/310107','虹口/310109','杨浦/310110','闵行/310112','宝山/310113','嘉定/310114','浦东/310115','金山/310116','松江/310117','青浦/310118','奉贤/310120','崇明/310151']

def visit1(n, cid, p):
    url = 'http://credit.lawyers.org.cn/lawyer-list.jsp?zoneCode='+str(cid)+'&businessArea=&q=&page='+str(p)
    res = req.get(url).text
    etreeres = etree.HTML(res)
    idurllist = etreeres.xpath('//a[@class="list-item"]/@href')
    if idurllist == []:
        return False
    for idurl in idurllist:
        try:
            visit2("http://credit.lawyers.org.cn/"+idurl, n)
        except:
            print("None")
    return True

def visit2(infourl, n):
    print(infourl)
    res1 = req.get(infourl).text.replace(' ', '').replace('\r', '').replace('\n', '')
    print(res1)
    try:
        mail = re.findall('email：</label>(.*?)<', res1)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        mail = 'None'
    try:
        zylb = re.findall('执业类型：</label>(.*?)<', res1)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        zylb = 'None'
    try:
        name = re.findall('<ddclass="name">(.*?)<', res1)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        name = 'None'
    f = open("{}.csv".format(str(n)), 'a')
    f.write(name+","+zylb+",-,"+mail+"\n")
    f.close()
    print(name,zylb,mail)


for c in cityl:
    n = c.split('/')[0]
    cid = c.split('/')[1]
    alive = True
    p = 1
    while alive == True:
        print("Page "+str(p))
        try:
            alive = visit1(n, cid, p)
        except:
            pass
        p += 1
