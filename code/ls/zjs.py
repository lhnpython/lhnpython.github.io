import requests as req
from lxml import etree

cityl = ['宁波市|http://www.zjbar.com/searchLawyer?association=fe9e942a02d14781bfb4caa52c3b4f61&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','金华市|http://www.zjbar.com/searchLawyer?association=fe9e942a1346499d87afed23d4bfd3f5&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','湖州市|http://www.zjbar.com/searchLawyer?association=fe9e942a18434269b37e96160beaf043&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','温州市|http://www.zjbar.com/searchLawyer?association=fe9e942a5ced48898f05caa24c611337&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','台州市|http://www.zjbar.com/searchLawyer?association=fe9e942a722b494c82dc383009f40df6&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','丽水市|http://www.zjbar.com/searchLawyer?association=fe9e942a81454b2d95f447538149bfe9&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','杭州市|http://www.zjbar.com/searchLawyer?association=fe9e942a8e844efdbcc78f4d5921cdf7&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','绍兴市|http://www.zjbar.com/searchLawyer?association=fe9e942ad13b482db7661c437a23e925&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','嘉兴市|http://www.zjbar.com/searchLawyer?association=fe9e942ade1c4a55a3cae4614ec27024&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','衢州市|http://www.zjbar.com/searchLawyer?association=fe9e942adfd5453d82e907d9770c2c20&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','舟山市|http://www.zjbar.com/searchLawyer?association=fe9e942ae788471d91ec770904e7c4f1&gender=&practiceScope=43ea076234e049579dd12b9715c6783f','金华市义乌市|http://www.zjbar.com/searchLawyer?association=fe9e942af0964a21a3b13fa54f16e88a&gender=&practiceScope=43ea076234e049579dd12b9715c6783f']


def visit1(n,url):
    res = req.get(url).text
    etreeres = etree.HTML(res)
    f = open('{}.csv'.format(n), 'a')
    for i in range(3,13):
        try:
            xm = etreeres.xpath('/html/body/div[2]/div[3]/div[2]/div/div/div/div[{}]/table/tr/td[2]/dl/dt/span/a/text()'.format(i))[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
        except:
            xm = '-'
        try:
            lb = etreeres.xpath('/html/body/div[2]/div[3]/div[2]/div/div/div/div[{}]/table/tr/td[2]/dl/dt/text()'.format(i))[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
        except:
            lb = '-'
        try:
            mail = etreeres.xpath('/html/body/div[2]/div[3]/div[2]/div/div/div/div[{}]/table/tr/td[2]/dl/dd[3]/a/@href'.format(i))[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")[7:]
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
