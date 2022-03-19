import time

from selenium import webdriver
import re

cityl = ['南宁市/450100', '柳州市/450200', '桂林市/450300', '梧州市/450400', '北海市/450500', '防城港市/450600', '钦州市/450700', '贵港市/450800', '玉林市/450900', '百色市/451000', '贺州市/451100', '河池市/451200', '来宾市/451300', '崇左市/451400']

driver = webdriver.Chrome()

def visit1(n,url):
    driver.get(url)
    res1 = driver.page_source.replace(' ', '').replace('\r', '').replace('\n', '')
    if '暂时没有业务数据哦' in res1:
        return False
    uids = re.findall('jspx\?btype=lvshi&amp;billid=(.*?)"',res1)
    for uid in uids:
        visit2(n, 'http://gx.12348.gov.cn/bill/goDetailPate.jspx?btype=lvshi&billid='+uid)
    return True


def visit2(n,endurl):
    driver.get(endurl)
    print(endurl)
    res2 = driver.page_source.replace(' ', '').replace('\r', '').replace('\n', '')
    try:
        xm = re.findall('<divclass="rowryjs-top-name"><h3>(.*?)</h3>',res2)
    except:
        xm = '-'
    try:
        phone = re.findall('<label>联系方式</label><span>(.*?)</span>',res2)
    except:
        phone = '-'
    try:
        jj = re.findall('<label>个人简介</label><span>(.*?)</span>', res2)
    except:
        jj = '-'
    f = open('{}.csv'.format(n),'a')
    for a,b,c in zip(xm,phone,jj):
        f.write(a.strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")+","+c.strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")+","+b.strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")+",-\n")
        print(a,c,b)
    f.close()



for city in cityl:
    n = city.split('/')[0]
    uid = city.split('/')[1]
    p = 1
    alive = True
    while alive == True:
        try:
            alive = visit1(n,'http://gx.12348.gov.cn/lssws/index_'+str(p)+'.jhtml?qkey=mscms.ms.getLSListGX&args_code='+str(uid))
        except:
            pass
        p += 1
