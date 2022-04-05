def send_mail(mail_from, password, mail_to, subject, content, subtype=None):
    url = 'http://103.153.139.179:8888/mail_sys/send_mail_http.json'

    pdata = {}
    pdata['mail_from'] = mail_from
    pdata['password'] = password
    pdata['mail_to'] = mail_to
    pdata['subject'] = subject
    pdata['content'] = content
    pdata['subtype'] = subtype
    #proxies = {"http": "http://218.75.102.198:8000"}
    resp_data = post(url, pdata).json()
    print(resp_data, mail_to)


if __name__ == '__main__':
    print("请输入邮箱, 回车键执行")
    youxiang = str(input())
    txt = open('txt.txt', 'r', encoding='utf-8')
    lines = txt.readlines()
    zt = lines[0]
    nr = ''
    for a in lines[1:]:
        nr += a
    f = open('address.txt', 'r')
    lines = f.readlines()
    try:
        for line in lines:
            wc = open('finish.txt', 'a')
            wc.write(line)
            # 发件人邮箱地址，例如jack@bt.cn
            mail_from = youxiang
            # 发件人邮箱地址密码
            password = 'Mm123456'
            # 收件人地址，多个用英文逗号隔开，例如 jack@bt.cn,rose@bt.cn
            mail_to = str(line)
            # 邮件标题
            subject = zt
            # 邮件内容
            content = nr
            # 邮件类型，不传默认为plain，要发送html请传html
            subtype = ''
            try:
                send_mail(mail_from, password, mail_to, subject, content)
            except:
                print("Error Pass And Doing Next")
            wc.close()
    except:
        print("Error")
