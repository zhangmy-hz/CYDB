from django.shortcuts import render,HttpResponse
from django.http import JsonResponse  #引入json响应
from cysystem.models import User_CY ,PURMA,PURTC,saomiao,yundan,SKU,YUN_ORDER,YUN_YI#先引入模型
import json,requests
import os,django,time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")# project_name 项目名称   #出现报错
django.setup()
from mian.settings import WX_APP_SECRET,APPID  #微信钥匙
from cysystem.sql import pysql,pysql_update
import hashlib
#import django_crontab


siji=PURMA.objects.filter(MA001='13819136546')
siji_iphone=siji.values('MA009')
print(siji_iphone)
