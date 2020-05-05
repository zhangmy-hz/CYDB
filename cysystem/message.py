from django.shortcuts import render, HttpResponse
from django.http import JsonResponse  # 引入json响应
from cysystem.models import User_CY, PURMA, PURTC, saomiao, yundan, SKU, YUN_ORDER, YUN_YI  # 先引入模型
import json, requests
import os, django, time

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")  # project_name 项目名称   #出现报错
django.setup()
from mian.settings import WX_APP_SECRET, APPID,MEDIA_ROOT  # 微信钥匙
from cysystem.sql import pysql, pysql_update
import hashlib


# import django_crontab

def notifications(request):
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={APPID}&secret={WX_APP_SECRET}'
    response = requests.get(url)

    response = response.json()
    if response.get('access_token', ''):
        cache = response['access_token']

    if request.method == 'POST':
        post_data = request.body
        post_data = json.loads(post_data)  # 转化
        siji = PURMA.objects.filter(MA001=post_data.get('siji_iphone')).values()
        siji_iphone = siji[0].get('MA009')
        date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))  # 获取当前时间
        #print('电话号码'+siji_iphone)
        #siji_iphone='oVJt85ZsG5oLQA6eURNm1APzTRVE'    #测试用
        access_token = cache

        template_id = 'rPrsQBrgveaUD5PXxgznwzoq6ZXZCftMVrSjwGA3ue8'
        push_data = {
            "thing1": {
                "value": '新的运单生成'
            },
            "time2": {
                "value": date
            },
            "thing3": {
                "value": '请前往签到地址装车'
            },
        }
        if access_token:
            # 如果存在accesstoken
            payload = {
                'touser': siji_iphone,  # 这里为用户的openid
                'template_id': template_id,  # 模板id
                'page': 'pages/login/login',  # 表单id或者prepay_id
                'data': push_data  # 模板填充的数据
            }
            response = requests.post(
                f'https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token={access_token}',
                json=payload)
            print(response,access_token)
            # 直接返回res结果
            return HttpResponse(payload)
        else:
            return JsonResponse({
                'err': 'access_token missing'
            })

