import requests as req
from lxml import etree
import re

cityl = ['成都市/5101','自贡市/5103','攀枝花市/5104','泸州市/5105','德阳市/5106','绵阳市/5107','广元市/5108','遂宁市/5109','内江市/5110','乐山市/5111','南充市/5113','眉山市/5114','宜宾市/5115','广安市/5116','达州市/5117','雅安市/5118','巴中市/5119','资阳市/5120','阿坝藏族羌族自治州/5132','甘孜藏族自治州/5133','凉山彝族自治州/5134']


def visit1(n,url):
    res = req.get(url).text
    etreeres = etree.HTML(res)
    pkids = etreeres.xpath('//ul/li/@onclick')
    if pkids == []:
        return False
    for pkid in pkids:
        visit2(n,'https://sc.12348.gov.cn/'+pkid[13:-2])
    return True

def visit2(n,endurl):
    print(endurl)
    res2 = req.get(endurl).text.replace(' ', '').replace('\r', '').replace('\n', '')
    try:
        xm = re.findall('姓名：(.*?)<',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        xm = '-'
    try:
        zylb = re.findall('<td>执业类别：(.*?)</td>',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        zylb = '-'
    try:
        phone = re.findall('<td>律师联系电话：(.*?)</td>',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        phone = '-'
    try:
        phone2 = re.findall('<td>本所电话：(.*?)</td>',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        phone2 = '-'
    print(xm,zylb,phone,phone2)
    f = open('{}.csv'.format(n),'a')
    f.write(xm+","+zylb+","+phone+","+phone2+"\n")
    f.close()


for city in cityl:
    n = city.split('/')[0]
    uid = city.split('/')[1]
    p = 1
    alive = True
    while alive == True:
        try:
            alive = visit1(n,'https://sc.12348.gov.cn/lsfw/lsfwlist.shtml?page='+str(p)+'&fydm='+str(uid)+'&kplb=2')
        except:
            pass
        p += 1
