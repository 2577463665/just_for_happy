import requests,time,hashlib,json

#登录后搜索https://app.mixcapp.com/mixc/gateway域名随意一个 请求体里面的deviceParams，token 多账号填多个单引号里面 用英文逗号隔开(现在的格式是2个账号的 如果单账号 改成deviceParams=['deviceParams1'])
deviceParams=['deviceParams1','deviceParams2']
token =['token1','token2']

# 企业微信推送参数
corpid = ''
agentid = ''
corpsecret = ''
touser = ''
# 推送加 token
plustoken = ''

def Push(contents):
  # 微信推送
  if all([corpid, agentid, corpsecret, touser]):
    token = \
      requests.get(
        f'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}').json()[
        'access_token']
    json = {"touser": touser, "msgtype": "text", "agentid": agentid, "text": {"content": "一点万向签到\n" + contents}}
    resp = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={token}", json=json)
    print('微信推送成功' if resp.json()['errmsg'] == 'ok' else '微信推送失败')

  if plustoken:
    headers = {'Content-Type': 'application/json'}
    json = {"token": plustoken, 'title': '一点万向签到', 'content': contents.replace('\n', '<br>'), "template": "json"}
    resp = requests.post(f'http://www.pushplus.plus/send', json=json, headers=headers).json()
    print('push+推送成功' if resp['code'] == 200 else 'push+推送失败')



print(f'共配置了{len(deviceParams)}个账号')
for i in range(len(deviceParams)):
  print(f'*****第{str(i+1)}个账号*****')
  timestamp = str(int(round(time.time() * 1000)))
  md5 = hashlib.md5()
  sig = f'action=mixc.app.memberSign.sign&apiVersion=1.0&appId=68a91a5bac6a4f3e91bf4b42856785c6&appVersion=3.32.0&deviceParams={deviceParams[i]}&imei=2333&mallNo=20014&osVersion=12.0.1&params=eyJtYWxsTm8iOiIyMDAxNCJ9&platform=h5&timestamp={timestamp}&token={token[i]}&P@Gkbu0shTNHjhM!7F' # 创建md5加密对象
  md5.update(sig.encode('utf-8'))  	# 指定需要加密的字符串
  sign = md5.hexdigest()  			# 加密后的字符串
  url = 'https://app.mixcapp.com/mixc/gateway'
  headers=  {
    'Host': 'app.mixcapp.com',
    'Connection': 'keep-alive',
    'Content-Length': '564',
    'Accept': 'application/json, text/plain, */*',
    'Origin': 'https://app.mixcapp.com',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; PCAM00 Build/QKQ1.190918.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36/MIXCAPP/3.42.2/AnalysysAgent/Hybrid',
    'Sec-Fetch-Mode': 'cors',
    'Content-Type': 'application/x-www-form-urlencoded',
    'X-Requested-With': 'com.crland.mixc',
    'Sec-Fetch-Site': 'same-origin',
    'Referer': 'https://app.mixcapp.com/m/m-20014/signIn?showWebNavigation=true&timestamp=1676906528979&appVersion=3.42.2&mallNo=20014',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7'
  }
  data =f'mallNo=20014&appId=68a91a5bac6a4f3e91bf4b42856785c6&platform=h5&imei=2333&appVersion=3.32.0&osVersion=12.0.1&action=mixc.app.memberSign.sign&apiVersion=1.0&timestamp={timestamp}&deviceParams={deviceParams[i]}&token={token[i]}&params=eyJtYWxsTm8iOiIyMDAxNCJ9&sign={sign}'
  html = requests.post(url=url,headers=headers,data=data)
  result = json.loads(html.text)['message']
  print(result)
  Push(contents=result)
