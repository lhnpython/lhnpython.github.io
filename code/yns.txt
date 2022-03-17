from selenium import webdriver
import re

cityl = ['昆明市/530100', '曲靖市/530300', '玉溪市/530400', '保山市/530500', '昭通市/530600', '丽江市/530700', '普洱市/530800', '临沧市/530900', '楚雄州/532300', '红河州/5323500', '文山州/5323600', '西双版纳州/5323800', '大理州/5323900', '德宏州/533100', '怒江州/533300', '迪庆州/533400']

driver = webdriver.Chrome()

def visit1(n,endurl):
    driver.get(endurl)
    print(endurl)
    res2 = driver.page_source
    if '无效页面' in res2:
        return False
    try:
        xm = re.findall('"xm":"(.*?)"',res2)
    except:
        xm = []
    try:
        zylb = re.findall('"zylb":"(.*?)"',res2)
    except:
        zylb = []
    try:
        phone = re.findall('"lxfs":"(.*?)"',res2)
    except:
        phone = []
    f = open('{}.csv'.format(n),'a')
    for a,b,c in zip(xm,zylb,phone):
        f.write(a.strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")+","+b.strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")+","+c.strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")+"\n")
        print(a,b,c)
    f.close()
    return True


for city in cityl:
    n = city.split('/')[0]
    uid = city.split('/')[1]
    p = 1
    alive = True
    while alive == True:
        try:
            alive = visit1(n,'https://yn.12348.laway.cn/gfy/api/ls/lawyer/?code='+str(uid)+'&page='+str(p))
        except:
            pass
        p += 1
