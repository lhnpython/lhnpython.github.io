headersdata = {
    'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '53',
    'Content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'browserid=2578880608527072266; timezoneOffset=28800,0; _ga=GA1.2.1341622068.1648298034; recentapps=%7B%22105600%22%3A1653049033%2C%223590%22%3A1653049015%7D; _gid=GA1.2.1653337918.1653464471; steamMachineAuth76561199044924308=697B710F713AFE6D730A60007748FBCE796214DB; sessionid=2288cb51192781e2b78eeea5; steamCountry=HK%7C0de93e39672c6029764cf886a557311f; steamLoginSecure=76561199302964869%7C%7C350378B3E2DCF5D52827E6C7E5404620523E8303',
    'Host': 'store.steampowered.com',
    'Origin': 'https://store.steampowered.com',
    'Referer': 'https://store.steampowered.com/account/redeemwalletcode',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
    'X-Prototype-Version': '1.7',
    'X-Requested-With': 'XMLHttpRequest',
}

formdata = {
    'wallet_code': 'fdgfdg',
    'sessionid': 'f1e63cc81c9fb639edb21ac7',
}

url = "http://store.steampowered.com/account/ajaxredeemwalletcode/"

res = requests.post(url, headers=headersdata, data=formdata).content
print(res)
