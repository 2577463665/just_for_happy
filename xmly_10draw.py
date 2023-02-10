import requests, json,time

#写的是喜马拉雅每日十连抽 十连抽一次抓包https://m.ximalaya.com/x-web-activity/draw/activity/drawTenAction这个域名的cookie
cookie =''

for i in range(2):
    url = 'https://m.ximalaya.com/x-web-activity/draw/activity/drawTenAction'
    headers = {
        'Cookie': f'{cookie}',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 iting/9.1.3 kdtunion_iting/1.0 iting(main)/9.1.3/ios_1 ;xmly(main)/9.1.3/iOS_1',
    }
    data = {
        'activityId': '2'
    }
    html = requests.post(url=url, headers=headers, data=data)
    result = json.loads(html.text)
    print(result)
    time.sleep(5)
    url2 = 'https://m.ximalaya.com/x-web-activity/draw/activity/receivingPercentAward'
    html2 = requests.post(url=url2, headers=headers, data=data)
    result2 = json.loads(html2.text)
    print(result2)
    time.sleep(5)


