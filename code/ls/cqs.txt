from selenium import webdriver
import re


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
    endurl = 'http://cq.12348.gov.cn/lsfw/getLsPeopleInfo?pkid='+pkid
    driver.get(endurl)
    print(endurl)
    res2 = driver.page_source
    try:
        xm = re.findall('"xm":"(.*?)"',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        xm = '-'
    try:
        zylb = re.findall('"zylb":"(.*?)"',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        zylb = '-'
    try:
        phone = re.findall('"dzyx":"(.*?)"',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        phone = '-'
    print(xm,zylb,phone)
    f = open('{}.csv'.format(n),'a')
    f.write(xm+","+zylb+","+phone+"\n")
    f.close()



p = 1
alive = True
n = '重庆市'
while alive == True:
    try:
        alive = visit1(n,'http://cq.12348.gov.cn/lsfw/getLsPeopleList?page={}&pageSize=500&pkid='.format(str(p)))
    except:
        pass
    p += 1
