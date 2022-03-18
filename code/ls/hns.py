from selenium import webdriver
import re

cityl = ['海口市/4601','三亚市/4602','三沙市/4603','儋州市/4604','五指山市/469001','琼海市/469002','文昌市/469005','万宁市/469006','东方市/469007','定安县/469021','屯昌县/469022','澄迈县/469023','临高县/469024','白沙黎族自治县/469025','昌江黎族自治县/469026','乐东黎族自治县/469027','陵水黎族自治县/469028','保亭黎族苗族自治县/469029','琼中黎族苗族自治县/469030','洋浦经济开发区/469031']

driver = webdriver.Chrome()
def visit1(n,url):
    driver.get(url)
    res = driver.page_source
    pkids = re.findall('"pkid":"(.*?)"',res)
    if pkids == []:
        return False
    for pkid in pkids:
        visit2(n,pkid)
    return True

def visit2(n,pkid):
    infourl = 'http://hi.12348.gov.cn/lsfw/getLsPeopleInfo?pkid='+pkid
    driver.get(infourl)
    res1 = driver.page_source
    sfzhs = re.findall('"sfzh":"(.*?)"',res1)
    for sfzh in sfzhs:
        visit3(n,sfzh)

def visit3(n,sfzh):
    endurl = 'http://36.101.208.235:8080/hnlawyer/fw/integrity/queryUserInfo?id_number='+sfzh
    driver.get(endurl)
    print(endurl)
    res2 = driver.page_source
    try:
        xm = re.findall('"XM":"(.*?)"',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        xm = '-'
    try:
        zylb = re.findall('"ZYLB":"(.*?)"',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        zylb = '-'
    try:
        phone = re.findall('"SJHM":"(.*?)"',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        phone = '-'
    print(xm,zylb,phone)
    f = open('{}.csv'.format(n),'a')
    f.write(xm+","+"-"+","+phone+",-\n")
    f.close()


for city in cityl:
    n = city.split('/')[0]
    uid = city.split('/')[1]
    p = 1
    alive = True
    while alive == True:
        try:
            alive = visit1(n,'https://hi.12348.gov.cn/lsfw/getLsPeopleList?areacode='+str(uid)+'&page='+str(p)+'&pageSize=500')
        except:
            pass
        p += 1
