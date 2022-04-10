import re
import time
from requests import get
from lxml import etree
from re import findall


def visit1(p, slp):
    print("Doing Page " + str(p))
    res = get('http://www.csres.com/new/run_{}.html'.format(str(p))).text.replace('\r\n', '\n')
    etreeres = etree.HTML(res)
    boxes = etreeres.xpath('//td[@valign="top"]/table[@width="100%"]/tr/td[3]/table[@width="100%"]')
    for box in boxes:
        try:
            t1 = box.xpath('tr[1]/td/a[1]/text()')[0].replace(",", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            t1 = 'None'
        try:
            t2 = box.xpath('tr[1]/td/font/strong/text()')[0].replace(",", ";").encode("gbk", "ignore").decode("gbk",
                                                                                                              "ignore")
        except:
            t2 = 'None'
        try:
            zbfls = box.xpath('tr[2]/td/a/text()')
            zbflt = ''
            for z in zbfls:
                zbflt += z + '>>'
            t3 = zbflt[:-2].replace(",", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            t3 = 'None'
        try:
            icss = box.xpath('tr[3]/td/a/text()')
            icst = ''
            for c in icss:
                icst += c + '>>'
            t4 = icst[:-2].replace(",", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            t4 = 'None'
        try:
            t5 = box.xpath('tr[4]/td/text()')[0].replace(",", ";").encode("gbk", "ignore").decode("gbk",
                                                                                                  "ignore").replace(
                ' ', '').replace('\n', '').replace('实', ',实')
        except:
            t5 = 'None'
        try:
            t6 = box.xpath('tr[5]/td/text()')[0].replace(",", ";").encode("gbk", "ignore").decode("gbk",
                                                                                                  "ignore").replace(' ',
                                                                                                                    '').replace(
                '	', '').replace('\n', '')
        except:
            t6 = 'None'
        try:
            t7 = box.xpath('tr[6]/td/font/text()')[0].replace(",", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            t7 = 'None'
        url = 'http://www.csres.com' + box.xpath('tr[1]/td/a[1]/@href')[0]
        t8 = visit2(url)
        time.sleep(slp)
        datas = str(
            pin) + ",链接: " + url + ',标准号和标准名称: ' + t1.strip() + ',状态: ' + t2.strip() + ',中标分类: ' + t3.strip() + ',ICS分类: ' + t4.strip() + ',' + t5.strip() + ',' + t6.strip() + ',价格: ' + t7.strip() + ',' + t8+",标准状态"+t2.strip()[1:-1]
        f = open('data.csv', 'a')
        f.write(datas + "\n")
        f.close()
    print("Finish Page " + str(p))


def visit2(url):
    print(url)
    headersdata = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }
    res20 = get(url, headers=headersdata)
    while 404 == res20.status_code:
        print('IP被禁, 请更换')
        time.sleep(3)
        res20 = get(url, headers=headersdata)
    res21 = res20.text.encode("gbk", "ignore").decode("gbk", "ignore").replace('\r\n', '\n')
    res2 = res21.replace(',', ';')
    try:
        bzmc = findall('<h3>(.*?)<a name="1">', res2)[0]
    except:
        bzmc = 'None'
    try:
        i1 = findall('标准编号：<font size=3><strong>(.*?)<', res2)[0]
    except:
        i1 = 'None'
    # try:
    #     i2 = findall('英文名称：\D*"sh14">(.*?)<', res2, re.I)[0]
    # except:
    #     i2 = 'None'
    # try:
    #     i3 = '替代' + findall('替代<a href=/detail/\d+.html target=_blank>(.*?)<', res2, re.I)[0]
    # except:
    #     i3 = 'None'
    # try:
    #     i4 = findall('发布部门：\D*"sh14">(.*?)<', res2, re.I)[0]
    # except:
    #     i4 = 'None'
    # try:
    #     i5 = findall('发布日期：\D*"sh14">(.*?)<', res2, re.I)[0]
    # except:
    #     i5 = '-'
    # try:
    #     i6 = findall('实施日期：\D*"sh14">(.*?)<', res2, re.I)[0]
    # except:
    #     i6 = 'None'
    # try:
    #     i7 = findall('提出单位：\D*"sh14">(.*?)<', res2, re.I)[0]
    # except:
    #     i7 = 'None'
    # try:
    #     i8 = findall('归口单位：\D*"sh14">(.*?)<', res2, re.I)[0]
    # except:
    #     i8 = 'None'
    # try:
    #     i9 = findall('起草单位：\D*"sh14">(.*?)<', res2, re.I)[0]
    # except:
    #     i9 = 'None'
    # try:
    #     i10 = findall('起草人：\D*"sh14">(.*?)<', res2, re.I)[0]
    # except:
    #     i10 = 'None'
    # try:
    #     i11 = findall('出版社：\D*"sh14">(.*?)<', res2, re.I)[0]
    # except:
    #     i11 = 'None'
    try:
        i0 = findall('<table width="99%"(.*?)</table>', res2, re.S)[1].replace('\n', '').replace('&nbsp;', '')
    except:
        i0 = 'None'
    # f1 = open('{}.txt'.format(url.split('/')[-1]), 'w')
    # f1.write(res2)
    # f1.close()
    # return i1.strip() + '","' + i2.strip() + '","' + i3.strip() + '","' + i4.strip() + '","' + i5.strip() + '","' + i6.strip() + '","' + i7.strip() + '","' + i8.strip() + '","' + i9.strip() + '","' + i10.strip() + '","' + i11.strip() + '","' + i0.strip().replace(
    #     '"', "'")
    infot = ''
    info = findall('>(.*?)<', i0, re.S)
    for a in info:
        if a != ' ' and a != '' and '   ' not in a:
            if '：' in a:
                infot = infot + '\n' + a
            else:
                infot += a
    return "标准名称"+bzmc+",标准号"+i1 + ',"' + infot[1:] + '"'


if __name__ == '__main__':
    pin = int(input("输入开始页码: "))
    slp = float(input("输入访问间隔时间: "))
    while True:
        visit1(pin, slp)
        pin += 1
