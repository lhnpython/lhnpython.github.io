import requests as req
import json

headersdata = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': '218.68.17.76:8082',
    'Origin': 'http://218.68.17.76:8087',
    'Referer': 'http://218.68.17.76:8087/home/lawyerlist',
    'tenant-id': '0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/99.0.4844.74 '
                  'Safari/537.36 '
}
url = 'http://218.68.17.76:8082/jeecg-boot/jeecg/lawyerInfo/findLawyerToForeign'

def visit(inid):
    datas1 = {"id":inid}
    res1 = req.post('http://218.68.17.76:8082/jeecg-boot/jeecg/lawyerInfo/findForeignLawInfo',data=json.dumps(datas1), headers=headersdata).text
    jsondata1 = json.loads(res1)
    try:
        xm = jsondata1["result"]["lawyerInfo"]["username"]
    except:
        xm = '-'
    try:
        zylb = jsondata1["result"]["lawyerInfo"]["lawyertype"]
        if zylb == '0':
            zylb = "兼职"
        if zylb == '1':
            zylb = "专职"
        if zylb == '2':
            zylb = "专职（派驻）"
        if zylb == '3':
            zylb = "法援"
        if zylb == '4':
            zylb = "公司"
        if zylb == '5':
            zylb = "公职"
        if zylb == '6':
            zylb = "专职基层法律工作者"
        if zylb == '7':
            zylb = "兼职基层法律工作者"
        if zylb == '8':
            zylb = "非律师"
    except:
        zylb = '-'
    try:
        phone = jsondata1["result"]["lawyerInfo"]["tel"]
    except:
        phone = '-'
    f = open("天津市.csv",'a')
    f.write(xm+","+zylb+","+phone+",-"+"\n")
    print(xm,zylb,phone)
    f.close()

p = 1
alive = True
while alive == True:
    datas = {"pageNo": p, "pageSize": 200, "lawofficename": "", "username": "", "workcardnumber": ""}
    res = req.post(url, data=json.dumps(datas), headers=headersdata).text
    jsondata = json.loads(res)
    infol = jsondata["result"]["list"]
    for info in infol:
        inid = info['id']
        visit(inid)
    p += 1
