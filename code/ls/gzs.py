import requests as req
import json

url = 'https://12348.guizhou.gov.cn/website/parse/rest.q4w'

cityl = ['贵阳市/520100','六盘水市/520200','遵义市/520300','安顺市/520400','毕节市/520500','铜仁市/520600','黔西南州/522300','黔东南州/522600','黔南州/522700']

def data(cid, p):
    datas = {
        'pageSize': 500,
        'pageNo': p,
        'name': '',
        'service': '',
        'business': '',
        'area': cid,
        'workTime': '',
        'isOnline': '',
        'cfg': 'com.lawyee.jalaw.parse.dto.LawyerDsoDTO@list'
    }
    return datas


for c in cityl:
    n = c.split('/')[0]
    cid = c.split('/')[1]
    alive = True
    p = 1
    while alive == True:
        try:
            datas = data(int(cid),p)
            res = req.post(url, data=datas).text
            jsondata1 = json.loads(res)
            f = open('{}.csv'.format(n),'a')
            for i in range(0,500):
                try:
                    xm = jsondata1['result']['result'][i]['name']
                except:
                    xm = '-'
                try:
                    sf = jsondata1['result']['result'][i]['inhouseIdentity']
                except:
                    sf = '-'
                try:
                    mail = jsondata1['result']['result'][i]['email']
                except:
                    mail = '-'
                if xm == '-' and sf == '-' and mail == '-':
                    alive = False
                f.write(xm+","+sf+",-,"+mail+"\n")
                print(xm,sf,mail)
            f.close()
        except:
            alive = False
        p += 1
