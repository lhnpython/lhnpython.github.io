print('在线版本, 最后更新于2022/3/21')
slp = float(input('请输入间隔时间,太短可能需要手动进行验证: '))
driver = webdriver.Chrome()


def visit(name, url):
    driver.get(url)
    res = driver.page_source
    if '填充拼图' in res:
        input('请手动验证, 回车键继续采集#######################')
    etreeres = etree.HTML(res)
    try:
        phone = re.findall('电话号码：(\d{11})，', res)[0]
    except:
        phone = 'None'
    try:
        cop = etreeres.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/a/text()')[0].strip()
    except:
        cop = 'None'
    try:
        n = etreeres.xpath('//*[@id="__layout"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/h1/text()')[0].strip()
    except:
        n = 'None'
    f1 = open('info-{}.csv'.format(name), 'a')
    f1.write(n + ',' + cop + ',' + phone + '\n')
    f1.close()
    print(n, cop, phone)


f0 = open('a.txt', 'r')
lines0 = f0.readlines()
for line0 in lines0[int(input('请输入开始序号: '))-1:]:
    name = line0.split('/')[-2]
    f = open('{}.txt'.format(name), 'r')
    lines = f.readlines()
    for line in lines:
        url = line[:-1]
        visit(name, url)
        print(url)
        time.sleep(slp)
    f.close()
