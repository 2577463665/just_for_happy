#!/usr/bin/python3
# -- coding: utf-8 --
# @Time : 2023/05/03 10:23
# -------------------------------
# cron "1,30 9 * * *" script-path=xxx.py,tag=匹配cron用
# const $ = new Env('小茅预约');

import datetime #line:1
import os #line:2
import random #line:3
import time #line:4
import re #line:5
import requests #line:6
import base64 #line:7
import json #line:8

#原创 微信公众号@爱上羊毛侠 

# 青龙面板加入环境变量MTTokenD
# MTTokenD是茅台预约参数，多个请换行，格式'省份,城市,经度,维度,设备id,token,MT-Token-Wap(抓包小茅运)'

p_c_map ={}#line:17
mt_r ='clips_OlU6TmFRag5rCXwbNAQ/Tz1SKlN8THcecBp/'#line:18
res_map ={'10213':'贵州茅台酒（癸卯兔年）','2476':'贵州茅台酒（壬寅虎年）','10214':'贵州茅台酒（癸卯兔年）x2'}#line:23
def mt_add (O0OO00OO0OOOO0000 ,O0OOOO0O00OO00O00 ,O0OOO0O0O000OOOOO ,OOOO000O0OOOOOOO0 ,OO00OO0000O000O00 ,O00OO000OOO0O0O0O ):#line:26
    OOOOO0OOOO00O0O00 =f'{int(time.time() * 1000)}'#line:27
    OO0OO0000O00O0000 =requests .get (f'http://82.157.10.108:8086/get_mtv?DeviceID={O00OO000OOO0O0O0O}&MTk={OOOOO0OOOO00O0O00}&version={mt_version}&key=yaohuo')#line:29
    O0OO0OO0OOOO0OO00 ={'User-Agent':'iPhone 14','MT-Token':OO00OO0000O000O00 ,'MT-Network-Type':'WIFI','MT-User-Tag':'0','MT-R':mt_r ,'MT-Lat':'','MT-K':OOOOO0OOOO00O0O00 ,'MT-Lng':'','MT-Info':'028e7f96f6369cafe1d105579c5b9377','MT-APP-Version':mt_version ,'MT-Request-ID':f'{int(time.time() * 1000)}','Accept-Language':'zh-Hans-CN;q=1','MT-Device-ID':O00OO000OOO0O0O0O ,'MT-V':OO0OO0000O00O0000 .text ,'MT-Bundle-ID':'com.moutai.mall','mt-lng':lng ,'mt-lat':lat }#line:39
    OOOOO0OOO00OOOO0O ={"itemInfoList":[{"count":1 ,"itemId":str (O0OO00OO0OOOO0000 )}],"sessionId":O0OOO0O0O000OOOOO ,"userId":str (OOOO000O0OOOOOOO0 ),"shopId":str (O0OOOO0O00OO00O00 )}#line:41
    OO0OO0000O00O0000 =requests .get ('http://82.157.10.108:8086/get_actParam?key=yaohuo&actParam='+base64 .b64encode (json .dumps (OOOOO0OOO00OOOO0O ).replace (' ','').encode ('utf8')).decode ())#line:43
    OOOOO0OOO00OOOO0O ['actParam']=OO0OO0000O00O0000 .text #line:44
    OOO00OO00000OO00O =OOOOO0OOO00OOOO0O #line:45
    OOOO00O0O00OOO0OO =requests .post ('https://app.moutai519.com.cn/xhr/front/mall/reservation/add',headers =O0OO0OO0OOOO0OO00 ,json =OOO00OO00000OO00O )#line:47
    O00O000O0O0O0OO00 =OOOO00O0O00OOO0OO .json ().get ('code',0 )#line:48
    if O00O000O0O0O0OO00 ==2000 :#line:49
        return OOOO00O0O00OOO0OO .json ().get ('data',{}).get ('successDesc',"未知")#line:50
    return '申购失败:'+OOOO00O0O00OOO0OO .json ().get ('message',"未知原因")#line:51
def tongzhi (OO0O00OOO00000OO0 ):#line:54
    O000O0OO0OOOO0OOO =os .getenv ('mtec_user','').split (',')#line:55
    for OO00OOOO00OO00OOO in O000O0OO0OOOO0OOO :#line:56
        OO00O0OOO00O00O0O ='http://wxpusher.zjiecode.com/api/send/message/?appToken=&content={}&uid={}'.format (OO0O00OOO00000OO0 ,OO00OOOO00OO00OOO )#line:58
        OOO000OOO00OOO000 =requests .get (OO00O0OOO00O00O0O )#line:59
        print (OOO000OOO00OOO000 .text )#line:60
def get_session_id (O0OO000OOOOO0OOO0 ,O0O00OOO0000O0OOO ):#line:63
    O0O000000000O00OO ={'mt-device-id':O0OO000OOOOO0OOO0 ,'mt-user-tag':'0','accept':'*/*','mt-network-type':'WIFI','mt-token':O0O00OOO0000O0OOO ,'mt-bundle-id':'com.moutai.mall','accept-language':'zh-Hans-CN;q=1','mt-request-id':f'{int(time.time() * 1000)}','mt-app-version':mt_version ,'user-agent':'iPhone 14','mt-r':mt_r ,'mt-lng':lng ,'mt-lat':lat }#line:78
    OO000O0O0O0OOOOO0 =requests .get ('https://static.moutai519.com.cn/mt-backend/xhr/front/mall/index/session/get/'+time_keys ,headers =O0O000000000O00OO )#line:81
    OOOO00000OOOOOO00 =OO000O0O0O0OOOOO0 .json ().get ('data',{}).get ('sessionId')#line:82
    OO0O00OOOOOO0O00O =OO000O0O0O0OOOOO0 .json ().get ('data',{}).get ('itemList',[])#line:83
    O0O000OO0OOOO0O0O =[OOO000O0OOOOO00OO .get ('itemCode')for OOO000O0OOOOO00OO in OO0O00OOOOOO0O00O ]#line:84
    return OOOO00000OOOOOO00 ,O0O000OO0OOOO0O0O #line:85
def get_shop_item (O00O0OOO000O000O0 ,O0O0OOOOO00000OOO ,OOOO00OO0OO0OO0OO ,OO00000O0000O0OO0 ,O00OO00OOO000OOOO ,O0000OOOO00OOO0O0 ):#line:88
    OOOO00O0O000O00OO ={'mt-device-id':OOOO00OO0OO0OO0OO ,'mt-user-tag':'0','mt-lat':'','accept':'*/*','mt-network-type':'WIFI','mt-token':OO00000O0000O0OO0 ,'mt-bundle-id':'com.moutai.mall','accept-language':'zh-Hans-CN;q=1','mt-request-id':f'{int(time.time() * 1000)}','mt-r':mt_r ,'mt-app-version':mt_version ,'user-agent':'iPhone 14','mt-lng':lng ,'mt-lat':lat }#line:104
    O0OOOOOOOOOOO0OO0 =requests .get ('https://static.moutai519.com.cn/mt-backend/xhr/front/mall/shop/list/slim/v3/'+str (O00O0OOO000O000O0 )+'/'+O00OO00OOO000OOOO +'/'+str (O0O0OOOOO00000OOO )+'/'+time_keys ,headers =OOOO00O0O000O00OO )#line:109
    OOO000O00000OOO0O =O0OOOOOOOOOOO0OO0 .json ().get ('data',{})#line:110
    OOO000O0000O00O00 =OOO000O00000OOO0O .get ('shops',[])#line:111
    O00O0OO0O00OOO0O0 =p_c_map [O00OO00OOO000OOOO ][O0000OOOO00OOO0O0 ]#line:112
    for O0O0OO000O0OOO0O0 in OOO000O0000O00O00 :#line:113
        if not O0O0OO000O0OOO0O0 .get ('shopId')in O00O0OO0O00OOO0O0 :#line:114
            continue #line:115
        if O0O0OOOOO00000OOO in str (O0O0OO000O0OOO0O0 ):#line:116
            return O0O0OO000O0OOO0O0 .get ('shopId')#line:117
def get_user_id (O0O0OOOOO00O00OOO ,O00000O00O0O00000 ):#line:120
    OOO0O0OOO000O0O0O ={'MT-User-Tag':'0','Accept':'*/*','MT-Network-Type':'WIFI','MT-Token':O0O0OOOOO00O00OOO ,'MT-Bundle-ID':'com.moutai.mall','Accept-Language':'zh-Hans-CN;q=1, en-CN;q=0.9','MT-Request-ID':f'{int(time.time() * 1000)}','MT-APP-Version':mt_version ,'User-Agent':'iOS;16.0.1;Apple;iPhone 14 ProMax','MT-R':mt_r ,'MT-Device-ID':O00000O00O0O00000 ,'mt-lng':lng ,'mt-lat':lat }#line:135
    O0O0O0O00OO0O0000 =requests .get ('https://app.moutai519.com.cn/xhr/front/user/info',headers =OOO0O0OOO000O0O0O )#line:138
    OO000OO00OO0OOOOO =O0O0O0O00OO0O0000 .json ().get ('data',{}).get ('userName')#line:139
    O000OO0OO0000OO00 =O0O0O0O00OO0O0000 .json ().get ('data',{}).get ('userId')#line:140
    O0OOO00OOOO0O00OO =O0O0O0O00OO0O0000 .json ().get ('data',{}).get ('mobile')#line:141
    return OO000OO00OO0OOOOO ,O000OO0OO0000OO00 ,O0OOO00OOOO0O00OO #line:142
def getUserEnergyAward (O0OOO000O0OOOO0O0 ,OO00OOO0OO0000OO0 ):#line:145
    ""#line:149
    O000OOOO0OO0000O0 ={'MT-Device-ID-Wap':O0OOO000O0OOOO0O0 ,'MT-Token-Wap':OO00OOO0OO0000OO0 ,'YX_SUPPORT_WEBP':'1',}#line:155
    OO0O00OO0OO000OOO ={'X-Requested-With':'XMLHttpRequest','User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 15_2_1 like Mac OS X)','Referer':'https://h5.moutai519.com.cn/gux/game/main?appConfig=2_1_2','Client-User-Agent':'iOS;15.0.1;Apple;iPhone 12 ProMax','MT-R':mt_r ,'Origin':'https://h5.moutai519.com.cn','MT-APP-Version':mt_version ,'MT-Request-ID':f'{int(time.time() * 1000)}','Accept-Language':'zh-CN,zh-Hans;q=0.9','MT-Device-ID':O0OOO000O0OOOO0O0 ,'Accept':'application/json, text/javascript, */*; q=0.01','mt-lng':lng ,'mt-lat':lat }#line:171
    O0OOO0O0O00000OO0 =requests .post ('https://h5.moutai519.com.cn/game/isolationPage/getUserEnergyAward',cookies =O000OOOO0OO0000O0 ,headers =OO0O00OO0OO000OOO ,json ={})#line:173
    return O0OOO0O0O00000OO0 .json ().get ('message')if '无法领取奖励'in O0OOO0O0O00000OO0 .text else "领取奖励成功"#line:174
def get_map ():#line:177
    global p_c_map #line:178
    OOOOOOO000O000000 ='https://static.moutai519.com.cn/mt-backend/xhr/front/mall/resource/get'#line:179
    O00O0OOOOO0O00O0O ={'X-Requested-With':'XMLHttpRequest','User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0_1 like Mac OS X)','Referer':'https://h5.moutai519.com.cn/gux/game/main?appConfig=2_1_2','Client-User-Agent':'iOS;16.0.1;Apple;iPhone 14 ProMax','MT-R':mt_r ,'Origin':'https://h5.moutai519.com.cn','MT-APP-Version':mt_version ,'MT-Request-ID':f'{int(time.time() * 1000)}{random.randint(1111111, 999999999)}{int(time.time() * 1000)}','Accept-Language':'zh-CN,zh-Hans;q=1','MT-Device-ID':f'{int(time.time() * 1000)}{random.randint(1111111, 999999999)}{int(time.time() * 1000)}','Accept':'application/json, text/javascript, */*; q=0.01','mt-lng':lng ,'mt-lat':lat }#line:194
    OO000O000O00OOO0O =requests .get (OOOOOOO000O000000 ,headers =O00O0OOOOO0O00O0O ,)#line:195
    O0OO0O0O0000OOOO0 =OO000O000O00OOO0O .json ().get ('data',{}).get ('mtshops_pc',{})#line:196
    O00OOO00OOOOOO00O =O0OO0O0O0000OOOO0 .get ('url')#line:197
    O0O00OO000000OO00 =requests .get (O00OOO00OOOOOO00O )#line:198
    for O00O0000OO000O00O ,O0OOOOOO0O0O000OO in dict (O0O00OO000000OO00 .json ()).items ():#line:199
        OOOO00O0OOOO0000O =O0OOOOOO0O0O000OO .get ('provinceName')#line:200
        OOOOO00O0000O00O0 =O0OOOOOO0O0O000OO .get ('cityName')#line:201
        if not p_c_map .get (OOOO00O0OOOO0000O ):#line:202
            p_c_map [OOOO00O0OOOO0000O ]={}#line:203
        if not p_c_map [OOOO00O0OOOO0000O ].get (OOOOO00O0000O00O0 ,None ):#line:204
            p_c_map [OOOO00O0OOOO0000O ][OOOOO00O0000O00O0 ]=[O00O0000OO000O00O ]#line:205
        else :#line:206
            p_c_map [OOOO00O0OOOO0000O ][OOOOO00O0000O00O0 ].append (O00O0000OO000O00O )#line:207
    return p_c_map #line:208
def login (OO0OO0O0OO00000O0 ,OOO0OOO0OO0OO000O ,OOOOOOO000OO000OO ):#line:211
    ""#line:218
    O0O000000000O0000 =f'{int(time.time() * 1000)}'#line:219
    O00OOO0O0OO0OO0O0 =requests .get (f'http://82.157.10.108:8086/get_mtv?DeviceID={OOOOOOO000OO000OO}&MTk={O0O000000000O0000}&version={mt_version}&key=yaohuo')#line:221
    O0OO000000OOOO0O0 ={'MT-Device-ID':OOOOOOO000OO000OO ,'MT-User-Tag':'0','Accept':'*/*','MT-Network-Type':'WIFI','MT-Token':'','MT-K':O0O000000000O0000 ,'MT-Bundle-ID':'com.moutai.mall','MT-V':O00OOO0O0OO0OO0O0 .text ,'User-Agent':'iOS;16.0.1;Apple;iPhone 14 ProMax','Accept-Language':'zh-Hans-CN;q=1','MT-Request-ID':f'{int(time.time() * 1000)}18342','MT-R':mt_r ,'MT-APP-Version':mt_version ,}#line:236
    OOOOO00O0O0OO0OO0 ={'ydToken':'','mobile':f'{OO0OO0O0OO00000O0}','vCode':f'{OOO0OOO0OO0OO000O}','ydLogId':'',}#line:243
    O00OOO00OOO0O0OO0 =requests .post ('https://app.moutai519.com.cn/xhr/front/user/register/login',headers =O0OO000000OOOO0O0 ,json =OOOOO00O0O0OO0OO0 )#line:246
    O00000000OOO00OOO =O00OOO00OOO0O0OO0 .json ().get ('data',{})#line:247
    O0000O0OO000O0000 =O00000000OOO00OOO .get ('token')#line:248
    OOOO00O0O0O0O0000 =O00000000OOO00OOO .get ('cookie')#line:249
    print (OOOOOOO000OO000OO ,O0000O0OO000O0000 ,OOOO00O0O0O0O0000 )#line:250
    return OOOOOOO000OO000OO ,O0000O0OO000O0000 ,OOOO00O0O0O0O0000 #line:251
def Push (O0O00000OO00O0O00 ):#line:253
    OO00OO00OOO00O0O0 ={'Content-Type':'application/json'}#line:255
    OOOOO0000O00O0OOO ={"token":plustoken ,'title':'茅台预约推送','content':O0O00000OO00O0O00 .replace ('\n','<br>'),"template":"json"}#line:256
    O0O00O0000OOOOO00 =requests .post (f'http://www.pushplus.plus/send',json =OOOOO0000O00O0OOO ,headers =OO00OO00OOO00O0O0 ).json ()#line:257
    print ('push+推送成功'if O0O00O0000OOOOO00 ['code']==200 else 'push+推送失败')#line:258
if __name__ =='__main__':#line:261
    plustoken =os .getenv ("plustoken")#line:262
    mt_tokens =os .getenv ("MTTokenD")#line:263
    mt_version ="".join (re .findall ('new__latest__version">(.*?)</p>',requests .get ('https://apps.apple.com/cn/app/i%E8%8C%85%E5%8F%B0/id1600482450').text ,re .S )).replace ('版本 ','')#line:264
    print ('当前最新版本为:'+mt_version )#line:265
    if not mt_tokens :#line:266
        print ('MTToken is null')#line:267
        exit ()#line:268
    mt_token_list =mt_tokens .split ('&')#line:269
    s ="-------------------总共"+str (int (len (mt_token_list )))+"个用户-------------------"+'\n'#line:272
    userCount =0 #line:273
    if len (mt_token_list )>0 :#line:274
        for mt_token in mt_token_list :#line:275
            userCount +=1 #line:276
            province ,city ,lng ,lat ,device_id ,token ,ck =mt_token .split (',')#line:278
            time_keys =str (int (time .mktime (datetime .date .today ().timetuple ()))*1000 )#line:280
            get_map ()#line:281
            try :#line:283
                sessionId ,itemCodes =get_session_id (device_id ,token )#line:284
                userName ,user_id ,mobile =get_user_id (token ,device_id )#line:285
                if not user_id :#line:286
                    s +="第"+str (userCount )+"个用户token失效，请重新登录"+'\n'#line:287
                    continue #line:288
                s +="第"+str (userCount )+"个用户----------------"+userName +'_'+mobile +"开始任务"+"----------------"+'\n'#line:290
                for itemCode in itemCodes :#line:291
                    name =res_map .get (str (itemCode ))#line:292
                    if name :#line:293
                        shop_id =get_shop_item (sessionId ,itemCode ,device_id ,token ,province ,city )#line:295
                        res =mt_add (itemCode ,str (shop_id ),sessionId ,user_id ,token ,device_id )#line:297
                        s +=itemCode +'_'+name +'---------------'+res +'\n'#line:299
                if not ck :#line:300
                    r =getUserEnergyAward (device_id ,ck )#line:301
                    s +=userName +'_'+mobile +'---------------'+"小茅运:"+r +'\n'#line:303
                s +=userName +'_'+mobile +"正常结束任务"+'\n              \n'#line:304
            except Exception as e :#line:305
                s +=userName +'_'+mobile +"异常信息"+e #line:306
    print (s )#line:307
    Push (contents =s )#line:308
