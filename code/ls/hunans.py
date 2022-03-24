import time

from selenium import webdriver
import re
from selenium.webdriver.common.by import By
from lxml import etree
import requests as req

cityl = ['长沙市/1','株洲市/2','湘潭市/3','衡阳市/4','邵阳市/5','岳阳市/6','常德市/7','张家界市/8','益州市/9','郴州市/10','永州市/11','娄底市/12','怀化市/13','湘西土家族苗族自治州/14']
driver = webdriver.Chrome()


def visit1(n):
    res = driver.page_source
    etreeres = etree.HTML(res)
    idurls = etreeres.xpath('//*[@id="app"]/div/section/main/div/div[9]/div/div[1]/div/div/a/@href')
    while idurls == []:
        res = driver.page_source
        etreeres = etree.HTML(res)
        idurls = etreeres.xpath('//*[@id="app"]/div/section/main/div/div[9]/div/div[1]/div/div/a/@href')
    for idurl in idurls:
        visit2(n,idurl.split('?')[-1])
    try:
        driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/section/main/div/div[9]/div/div[2]/button[2]').click()
    except:
        return False
    res2 = driver.page_source
    etreeres2 = etree.HTML(res2)
    idurls2 = etreeres2.xpath('//*[@id="app"]/div/section/main/div/div[9]/div/div[1]/div/div/a/@href')
    while idurls2 == idurls:
        res2 = driver.page_source
        etreeres2 = etree.HTML(res2)
        idurls2 = etreeres2.xpath('//*[@id="app"]/div/section/main/div/div[9]/div/div[1]/div/div/a/@href')
    return True

def visit2(n,url):
    resi = req.get('http://hn.12348.gov.cn/rufamain/lawoffice/queryLawyer?'+url).text.replace(' ', '').replace('\r', '').replace('\n', '')
    try:
        xm = re.findall('"name":"(.*?)"',resi)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        xm = '-'
    try:
        sf = re.findall('"practiceType":"(.*?)"',resi)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        sf = '-'
    try:
        mail = re.findall('"email":"(.*?)"',resi)[0].strip().replace(",", ";").encode("gbk","ignore").decode("gbk","ignore")
    except:
        mail = '-'
    f = open('{}.csv'.format(n),'a')
    f.write(xm+","+sf+",-,"+mail+"\n")
    print(xm,mail)

for c in cityl[int(input("输入开始城市号码: "))-1:]:
    n = c.split('/')[0]
    i = int(c.split('/')[1])
    driver.get('http://hn.12348.gov.cn/#/search')
    driver.find_element(by=By.XPATH, value='//*[@id="tab-1"]').click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/section/main/div/div[6]/div[2]/button[{}]'.format(i)).click()
    time.sleep(1)
    driver.find_element(by=By.XPATH, value='//*[@id="pane-1"]/div/div/button').click()
    alive = True
    while alive == True:
        alive = visit1(n)
