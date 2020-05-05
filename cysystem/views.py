from django.shortcuts import render,HttpResponse
from django.http import JsonResponse,FileResponse  #引入json响应
from cysystem.models import User_CY ,PURMA,PURTC,saomiao#先引入模型
import json,requests
import os,django,time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")# project_name 项目名称   #出现报错
django.setup()
from mian.settings import WX_APP_SECRET  #微信钥匙
from cysystem.sql import pysql,pysql_update
import  hashlib

class ReturnCode:
    SUCCESS = 0
    FAILED = -100
    UNAUTHORIZED = -500
    BROKEN_AUTHORIZED_DATA = -501
    WRONG_PARMAS = -101
    RESOURCES_NOT_EXISTS = -102
    SESSION_EXPIRED = -502

    @classmethod
    def message(cls, code):
        if code == cls.SUCCESS:
            return "success"
        elif code == cls.FAILED:
            return 'failed'
        elif code == cls.UNAUTHORIZED:
            return 'unauthorized'
        elif code == cls.WRONG_PARMAS:
            return 'wrong params'
        elif code == cls.RESOURCES_NOT_EXISTS:
            return 'this file not exists'
        elif code == cls.BROKEN_AUTHORIZED_DATA:
            return 'broken authorized data'
        elif code == cls.SESSION_EXPIRED:
            return 'session expired'

def wrap_json_response(data=None, code=None, message=None):
    response = {}
    if not code:
        code = ReturnCode.SUCCESS
    if not message:
        message = ReturnCode.message(code)
    if data:
        response['data'] = data
    response['result_code'] = code
    response["message"] = message
    return response

# Create your views here.
def login(request):
    return render(request, 'login.html')
def login_check(request):
    name=request.GET['html_name']
    password=request.GET['html_password']  #网页获取内容
    print(name,password)
    try:
        user=User_CY.objects.get(name=name)
        result=0
    except:
        result=1000
    if result== 0 :   #表示用户名存在
        try:
            user = User_CY.objects.get(name=name,password=password)
            result=0
        except:
            result=2000
    print(result)
    return HttpResponse(json.dumps({'result': result}))
def HelloWorld(request):    #微信小程序响应测试
    print('request.method:',request.method)
    print('request.META:',request.META)     #请求数据
    print('request.COOKIES:',request.COOKIES)
    print('request.QueryDict:',request.GET)   #GET请求的参数信息

    #return HttpResponse(content='一定要完成',status=201)
    m={"caobi":"shijincao","干":"使劲干"}
    return JsonResponse(data=m,safe=False,status=200)
def mythree(request):
    data=User_CY.objects.values()   #所有用户信息数据
    data_json=[]
    for date_i in data:
        data_json.append(date_i)
    print(data_json)
    return JsonResponse(data=data_json,safe=False)
def login(request):
    post_data=request.body
    post_data=json.loads(post_data)
    data=post_data.get('dianhua')
    #判断登录号是否存在:
    if not data :   #传值手机号为空
        return HttpResponse('NOT OK')
    if not PURMA.objects.filter(MA001=data):  #手机号不存在
        return HttpResponse('NOT OK')
    iphone_state=PURMA.objects.filter(MA001=data).values()
    if iphone_state[0].get('MA008') =='停用':
        return HttpResponse('NOT OK')

    return HttpResponse('OK')
def openid(request):
    post_data=request.body
    post_data=json.loads(post_data)       #转化
    code=post_data.get('code').strip()   #得到并去空格
    appid=post_data.get('appId').strip()   #得到并去空格
    iphone=post_data.get('iphone').strip()   #电话
    print(code,appid)
    if not  code or not appid or not iphone:
        return HttpResponse('NOT OK')
    #调用微信API
    API = 'https://api.weixin.qq.com/sns/jscode2session'
    params = 'appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % \
             (appid, WX_APP_SECRET, code)
    url = API + '?' + params
    response = requests.get(url=url)
    data = json.loads(response.text)
    openid=data.get('openid')      #取值微信授权码


    if iphone !='test':   #我定义test为验证是否授权状态:也是用户初次登录
        if not PURMA.objects.filter(MA001=iphone,MA009=openid):
            shouquan=PURMA.objects.get(MA001=iphone)
            shouquan.MA009=openid
            shouquan.save()      #保存数据库
            request.session['openid'] = openid
            request.session['iphone'] = iphone
            return HttpResponse(202)  # 返回微信状态201
    elif iphone =='test':
        if PURMA.objects.filter(MA009=openid):
            #定义cookie
            iphone_all = PURMA.objects.filter(MA009=openid).values()  ## @查询
            if iphone_all[0].get('MA008') == '停用':
                return HttpResponse('NOT OK')
            else:
                iphone = iphone_all[0].get('MA001')  # 获取得到电话号码
                request.session['openid']=openid
                request.session['iphone']=iphone
                return HttpResponse(201)    #返回微信状态201
    print(data)
    return  HttpResponse('OK')

def cookie(request):    #测试session
    print( '结果是'+request.session.get('openid'))   #输出
    return HttpResponse('ok')

'''def cat_type(request):   #前台请求车型下拉列表
    data = PURTC.objects.values('TC001','TC002')  # 所有用户信息数据
    data_json = []
    for date_i in data:
        data_json.append(date_i)
    return JsonResponse(data=data_json, safe=False)    '''
def cat_type(request):   #前台请求车型下拉列表
    openid = request.session.get('openid')  # 先找到司机信息
    iphone_all = PURMA.objects.filter(MA009=openid).values()  ## @查询
    iphone = iphone_all[0].get('MA001')  # 获取得到电话号码

    data=pysql("SELECT TD002,TD003 FROM PURTD WHERE TD001='{}'".format(iphone))
    list = []
    dict = {}
    for data_i in data:
        dict['TC001'] = data_i[0]
        dict['TC002'] = data_i[1]
        list.append(dict)
        dict = {}

    return JsonResponse(data=list, safe=False)
def cat_now(request):   #前台请求车型下拉列表
    openid = request.session.get('openid')  # 先找到司机信息
    iphone_all = PURMA.objects.filter(MA009=openid).values()  ## @查询
    iphone = iphone_all[0].get('MA001')  # 获取得到电话号码
    cat_new=pysql("SELECT MA002,replace(TD001,' ',''),replace(TD002,' ',''),replace(TD003,' ','') FROM PURTD inner join cysystem_purma on MA001=TD001 WHERE TD001='{}' AND TD006='Y'".format(iphone))  #得到目前的默认车型
    print(cat_new)
    return JsonResponse(data=cat_new, safe=False)

def cat_sure(request):  #车型绑定确认\
    openid=request.session.get('openid')   #先找到司机信息
    iphone_all=PURMA.objects.filter(MA009=openid).values() ## @查询
    iphone=iphone_all[0].get('MA001')       #获取得到电话号码

    post_data = request.body
    post_data = json.loads(post_data)  # 转化
    cat_detial = post_data.get('pic_array')
    cat=cat_detial.get('TC001')
    cat_ty=cat_detial.get('TC002')
    if not pysql("select * from PURTD where TD001='{}' AND TD002='{}'".format(iphone,cat)):  #如果不存在司机绑定
        pysql_update("insert into PURTD (TD001,TD002,TD003,TD006) VALUES ('{}','{}','{}','Y')".format(iphone,cat,cat_ty))
    else:  #已经存在了
        pysql_update("update PURTD SET TD006='N' where TD001='{}' ".format(iphone))  #先清空状态
        pysql_update("update PURTD SET TD006='Y' where TD001='{}' AND TD002='{}'".format(iphone,cat))
    print(post_data,cat_detial,cat)
    return HttpResponse('ok')

def saomiao_1(request):    #司机扫描签到return HttpResponse('OK')
    openid = request.session.get('openid')  # 先找到司机信息
    iphone_all = PURMA.objects.filter(MA009=openid).values()  ## @查询
    iphone = iphone_all[0].get('MA001')  # 获取得到电话号码
    post_data = request.body
    post_data = json.loads(post_data)  # 转化
    cat_detial = post_data.get('result')   #得到地址标识
    if pysql("select CA006 FROM RDMCA WHERE CA006='{}'".format(cat_detial))==[]:  #地址为空
        return HttpResponse('NOT OK')
    else:
        del_sao=saomiao.objects.filter(TA001=iphone)    #删除已有签到,只删除本司机
        del_sao.delete()
        add=pysql("select REPLACE(CA008,' ','') FROM RDMCA WHERE CA006='{}'".format(cat_detial))[0][0]
        date=time.strftime('%Y-%m-%d %H:%M',time.localtime(time.time()))  #获取当前时间
        dada_sql=saomiao.objects.create(TA001=iphone,TA002=add,TA003=date,TA004=cat_detial)
        dada_sql.save()
        add_state=pysql("select replace(CA007,' ','') FROM RDMCA WHERE CA006='{}'".format(cat_detial))  #得到是否司机调度
        return  HttpResponse(add_state[0])

def qiandao(request):  #初始化签到信息\
    openid=request.session.get('openid')   #先找到司机信息
    iphone_all=PURMA.objects.filter(MA009=openid).values() ## @查询
    iphone=iphone_all[0].get('MA001')       #获取得到电话号码

    qiandao_mx=saomiao.objects.filter(TA001=iphone)   #获取签到信息
    data = qiandao_mx.values('TA002', 'TA003')  # 所有用户信息数据

    data_json = []
    for date_i in data:
        data_json.append(date_i)
    print(data,data_json)
    return JsonResponse(data=data_json, safe=False)
