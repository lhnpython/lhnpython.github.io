import requests as req
import json

cityl = ['哈尔滨市/2301', '齐齐哈尔市/2302', '牡丹江市/2310', '佳木斯市/2308', '大庆市/2306','鸡西市/2303', '双鸭山市/2305', '伊春市/2307', '七台河市/2309', '鹤岗市/2304', '黑河市/2311', '绥化市/2312', '大兴安岭地区/2327']

for c in cityl:
    n = c.split('/')[0]
    cid = c.split('/')[1]
    res1 = req.get('http://hl.12348.gov.cn/gfpt/public/gfpt/ggflfw/wsbs/ls/listlsry?type=1&countSize=1&startSize=1&dqPage=1&dqbm='+str(cid)).text
    jsondata1 = json.loads(res1)
    tol = jsondata1['count']
    res2 = req.get('http://hl.12348.gov.cn/gfpt/public/gfpt/ggflfw/wsbs/ls/listlsry?type=1&countSize='+str(tol)+'&startSize=1&dqPage=1&dqbm=' + str(cid)).text
    jsondata2 = json.loads(res2)
    infolist = jsondata2["lsrylist"]
    f = open("{}.csv".format(n),'a')
    for info in infolist:
        f.write(info[2]+","+info[1]+"\n")
        print(info)
    f.close()