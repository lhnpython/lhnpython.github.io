import requests as req
from lxml import etree


cityl = ['区直属|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a8bcd47b4a414079400268a02&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','钦州市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a007a423caa5c6c8226a01cf3&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','防城港市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a0ac24598920ad157529f470b&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','贵港市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a18b74c839835c7dee59f1b1d&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','河池市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a1c6941c998ef0b4a5ee777bb&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','北海市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a25e14ee582bad5188a4ca1e6&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','梧州市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a46f2482697001c5fca54c508&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','贺州市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a4cb94ddfa1e9dad75f08db59&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','柳州市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a4ff644738bbb3853947d36dc&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','百色市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a685c46aaa5d4fa4798d7cbfc&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','南宁市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a6a07493e9e4d28154a637885&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','来宾市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a6b354ff0a8a9d681e425df93&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','崇左市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942a84a84544a9990cabff534230&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','玉林市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942aea62431f8cda6eb2559fab2c&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','桂林市|http://www.gxlawyer.org.cn/searchLawyer?association=fe9e942af7d240b9ab56f373813c6793&gender=&practiceScope=43ea076234e049579dd12b9715c6783f']


def visit1(n,url):
    res = req.get(url).text
    etreeres = etree.HTML(res)
    f = open('{}.csv'.format(n), 'a')
    for i in range(6,16):
        try:
            xm = etreeres.xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[{}]/table/tr/td[2]/dl/dt/span/a/text()'.format(i))[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
        except:
            xm = '-'
        try:
            lb = etreeres.xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[{}]/table/tr/td[2]/dl/dt/text()'.format(i))[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
        except:
            lb = '-'
        try:
            mail = etreeres.xpath('/html/body/div[1]/div[3]/div[3]/div[1]/div[{}]/table/tr/td[2]/dl/dd[3]/a/@href'.format(i))[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")[7:]
        except:
            mail = '-'
        f.write(xm+","+lb+",-,"+mail+"\n")
        print(xm,lb,mail)
        if xm == '-' and lb == '-' and mail == '-':
            return False
    f.close()

    return True



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
