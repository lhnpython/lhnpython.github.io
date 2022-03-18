import requests as req
import re

url = 'https://he.12348.gov.cn/skywcm/webpage/search/search_do.jsp'

cityl = ['石家庄市/1301', '承德市/1308', '张家口市/1307', '秦皇岛市/1303', '唐山市/1302', '廊坊市/1310', '保定市/1306', '沧州市/1309', '衡水市/1311',
         '邢台市/1305', '邯郸市/1304', '定州市/1391', '辛集市/1390']


def data(cid, p):
    datas = {
        '0': 0,
        'pageSize': 6,
        'pageNum': p,
        'type': 2,
        'businessType': 1,
        'minPoints': '',
        'maxPoints': '',
        'districtcode': cid,
        'keyword': '',
        'pkid': 0,
        't': '',
    }
    return datas


for c in cityl:
    n = c.split('/')[0]
    cid = c.split('/')[1]
    alive = True
    p = 1
    while alive == True:
        try:
            datas = data(int(cid), p)
            res = req.post(url, data=datas).text
            f = open('{}.csv'.format(n), 'a')
            for i in range(0, 1):
                try:
                    xm = re.findall('"user_name":"(.*?)"',res)
                except:
                    xm =[]
                try:
                    sf = '-'
                except:
                    sf = '-'
                try:
                    mail = re.findall('"cell_phone":"(.*?)"',res)
                except:
                    mail = []
                if xm == [] and mail == []:
                    alive = False
                for a,b in zip(xm,mail):
                    f.write(a + ",-," + b + ",-\n")
                    print(a, b)
            f.close()
        except:
            alive = False
        p += 1
