keyw = str(input("Please Input KeyWord: "))
p = int(input("Please Input Begin PageNumber: "))-1
f = open('data.csv', 'a')
f.write('企业名称,国家地区,地址,邮编,企业网址,业务联系人,办公电话,手机,传真,邮箱,PageNumber\n')
f.close()
while True:
    url = "https://www.cantonfair.org.cn/b2bshop/api/themeRos/public/productShops/searchByVariables?productSearchable=true&industrySiteId=461110967833538560&unbox=true&lang=zh-CN%2Cen-US&categoryId=&q={}&page=".format(
        keyw) + str(p) + "&size=40&scoreStrategy=shop"
    res = req.get(url).text
    jdata = json.loads(res)
    for i in range(0, 40):
        try:
            i1 = str(jdata['_embedded']['b2b:shops'][i]['name']).replace(",", ";").replace("\n", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            i1 = ''
        try:
            i2 = str(jdata['_embedded']['b2b:shops'][i]['address']['province']['name']).replace(",", ";").replace("\n", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            i2 = ''
        try:
            i3 = str(jdata['_embedded']['b2b:shops'][i]['address']['detailAddress']).replace(",", ";").replace("\n", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            i3 = ''
        try:
            i4 = str(jdata['_embedded']['b2b:shops'][i]['udfs']['zipCode']).replace(",", ";").replace("\n", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            i4 = ''
        try:
            i5 = str(jdata['_embedded']['b2b:shops'][i]['udfs']['website']).replace(",", ";").replace("\n", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            i5 = ''
        try:
            i6 = str(jdata['_embedded']['b2b:shops'][i]['udfs']['contactPerson']).replace(",", ";").replace("\n", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            i6 = ''
        try:
            i7 = str(jdata['_embedded']['b2b:shops'][i]['udfs']['telephone']).replace(",", ";").replace("\n", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            i7 = ''
        try:
            i8 = str(jdata['_embedded']['b2b:shops'][i]['udfs']['mobilePhone']).replace(",", ";").replace("\n", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            i8 = ''
        try:
            i9 = str(jdata['_embedded']['b2b:shops'][i]['udfs']['fax']).replace(",", ";").replace("\n", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            i9 = ''
        try:
            i0 = str(jdata['_embedded']['b2b:shops'][i]['udfs']['email']).replace(",", ";").replace("\n", ";").encode("gbk", "ignore").decode("gbk", "ignore")
        except:
            i0 = ''
        f = open('data.csv', 'a')
        f.write(i1 + "," + i2 + "," + i3 + "," + i4 + "," + i5 + "," + i6 + ",'" + i7 + "," + i8 + ",'" + i9 + "," + i0 + "," + "PageNumber{}".format(str(p+1))+ "\n")
        f.close()
        print(i1 + "," + i2 + "," + i3 + "," + i4 + "," + i5 + "," + i6 + "," + i7 + "," + i8 + "," + i9 + "," + i0)
    p += 1
