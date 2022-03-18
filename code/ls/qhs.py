from selenium import webdriver
import re

cityl = ['西宁市/6301','海东市/6302','海北藏族自治州/6322','黄南藏族自治州/6323','海南藏族自治州/6325','果洛藏族自治州/6326','玉树藏族自治州/6327','海西蒙古族藏族自治州/6328']

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
    endurl = 'https://qh.12348.gov.cn/lawyer/getLawyerInfo?lsbs='+pkid
    driver.get(endurl)
    print(endurl)
    res2 = driver.page_source
    try:
        xm = re.findall('"xm":"(.*?)"',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        xm = '-'
    try:
        zylb = re.findall('"zylx":(.*?),',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        zylb = '-'
    try:
        phone = re.findall('"lxdh":"(.*?)"',res2)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        phone = '-'
    print(xm,zylb,phone)
    f = open('{}.csv'.format(n),'a')
    f.write(xm+","+zylb+",-,"+phone+"\n")
    f.close()


for city in cityl:
    n = city.split('/')[0]
    uid = city.split('/')[1]
    p = 1
    alive = True
    while alive == True:
        try:
            alive = visit1(n,'https://qh.12348.gov.cn/lawyer/getLawyerList?areacode='+str(uid)+'&page='+str(p)+'&pageSize=500&zyjg=')
        except:
            pass
        p += 1
