import requests as req
import re
from lxml import etree

cityl = ['沈阳市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942ae37c4f608da79122aafcb5c1'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '大连市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942a4bce4a278d438bd4d2036158'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '鞍山市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942ac80e4d6fbfe6248927efe622'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '抚顺市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942a0ddf44669855edfe8522ce84'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '本溪市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942adc20470fad42cebe3971ad2b'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '丹东市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942a2f304d7bb952866602402249'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '锦州市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942a3ad5455da7b61bb78add7859'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '营口市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942a562c42278a068806403c938c'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '阜新市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942a44f64f64b62b723baf5b0417'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '辽阳市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942a2d7c4d499c766f79b48a5f71'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '盘锦市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942a3d2b475390a891305068b4ea'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '铁岭市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942ae0c945a2ad3e7b1f1286f824'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '朝阳市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942ab1934c47bf06fc33ca15e743'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f',
         '葫芦岛市|http://www.lnlawyers.net/member/yellowPage/searchLawyer?association=fe9e942a04e34357bab0097e500a83d7'
         '&gender=&practiceScope=43ea076234e049579dd12b9715c6783f']


def visit1(n,url):
    res = req.get(url).text
    etreeres = etree.HTML(res)
    pkids = etreeres.xpath('/html/body/div/div[2]/div[2]/div[2]/div/div[3]/ul/li/div[2]/p[1]/a/@href')
    if pkids == []:
        return False
    for pkid in pkids:
        visit2(n,pkid)
    return True


def visit2(n,pkid):
    endurl = 'http://www.lnlawyers.net'+pkid
    res2 = req.get(endurl).text.replace(' ', '').replace('\r', '').replace('\n', '')
    try:
        xm = re.findall('>律师姓名：(.*?)<',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        xm = '-'
    try:
        zylb = re.findall('>执业类别：(.*?)<',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        zylb = '-'
    try:
        phone = re.findall('>联系电话：(.*?)<',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        phone = '-'
    try:
        mail = re.findall('>E-mail:(.*?)<',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        mail = '-'
    print(xm,zylb,phone,mail)
    f = open('{}.csv'.format(n),'a')
    f.write(xm+","+zylb+","+phone+","+mail+"\n")
    f.close()


for city in cityl:
    n = city.split('|')[0]
    uid = city.split('|')[1]
    p = 1
    alive = True
    while alive == True:
        try:
            alive = visit1(n,uid+"&page="+str(p))
        except:
            pass
        p += 1
