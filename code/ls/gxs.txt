from selenium import webdriver
import re

cityl = ['南宁市/450100', '柳州市/450200', '桂林市/450300', '梧州市/450400', '北海市/450500', '防城港市/450600', '钦州市/450700', '贵港市/450800', '玉林市/450900', '百色市/451000', '贺州市/451100', '河池市/451200', '来宾市/451300', '崇左市/451400']

driver = webdriver.Chrome()

def visit1(n,endurl):
    driver.get(endurl)
    print(endurl)
    res2 = driver.page_source.replace(' ', '').replace('\r', '').replace('\n', '')
    if '暂时没有业务数据哦' in res2:
        return False
    try:
        xm = re.findall('<h3class="panel-title">(.*?)</h3>',res2)
    except:
        xm = '-'
    try:
        phone = re.findall('联系方式：(.*?)<',res2)
    except:
        phone = '-'
    f = open('{}.csv'.format(n),'a')
    for a,b in zip(xm,phone):
        f.write(a.strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")+","+b.strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")+"\n")
        print(a,b)
    f.close()
    return True


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
