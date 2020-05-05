from django.shortcuts import render,HttpResponse
from django.http import JsonResponse  #引入json响应
from cysystem.models import User_CY ,PURMA,PURTC,saomiao,yundan,SKU,YUN_ORDER,YUN_YI#先引入模型
import json,requests
import os,django,time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")# project_name 项目名称   #出现报错
django.setup()
from mian.settings import WX_APP_SECRET  #微信钥匙
from cysystem.sql import pysql,pysql_update
import hashlib

def add_select(request):    #初始化加载所有地址信息
    add = pysql("select CA008 FROM RDMCA ")

    return JsonResponse(data=add, safe=False)

def saomiao_1(request):    #司机扫描签到return HttpResponse('OK')
    openid = request.session.get('openid')  # 先找到司机信息
    iphone_all = PURMA.objects.filter(MA009=openid).values()  ## @查询
    iphone = iphone_all[0].get('MA001')  # 获取得到电话号码

    post_data = request.body
    post_data = json.loads(post_data)  # 转化
    cat_detial = post_data.get('result')[0]   #得到地址名称
    if pysql("select CA006 FROM RDMCA WHERE CA008='{}'".format(cat_detial))==[]:  #地址为空
        return HttpResponse('NOT OK')
    else:
        del_sao = saomiao.objects.filter(TA001=iphone)  # 删除已有签到,只删除本司机
        del_sao.delete()
        add = pysql("select REPLACE(CA001+CA002+CA003+CA004,' ','') FROM RDMCA WHERE CA008='{}'".format(cat_detial))[0][0]
        add_i = pysql("select CA006 FROM RDMCA WHERE CA008='{}'".format(cat_detial))[0][0]
        date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))  # 获取当前时间
        dada_sql = saomiao.objects.create(TA001=iphone, TA002=cat_detial, TA003=date, TA004=add_i)
        dada_sql.save()

        add_state = pysql("select replace(CA007,' ','') FROM RDMCA WHERE CA008='{}'".format(cat_detial))  # 得到是否司机调度
        return HttpResponse(add_state[0])

def saomiao_2(request):    #司机扫描签到return HttpResponse('OK')
    openid = request.session.get('openid')  # 先找到司机信息
    iphone_all = PURMA.objects.filter(MA009=openid).values()  ## @查询
    iphone = iphone_all[0].get('MA001')  # 获取得到电话号码

    post_data = request.body
    post_data = json.loads(post_data)  # 转化
    cat_detial = post_data.get('result')[0]   #得到地址名称
    if pysql("select CA006 FROM RDMCA WHERE CA008='{}'".format(cat_detial))==[]:  #地址为空
        return HttpResponse('NOT OK')
    else:
        del_sao = saomiao.objects.filter(TA001=iphone)  # 删除已有签到,只删除本司机
        del_sao.delete()
        #add = pysql("select REPLACE(CA001+CA002+CA003+CA004,' ','') FROM RDMCA WHERE CA008='{}'".format(cat_detial))[0][0]
        add_i = pysql("select CA006 FROM RDMCA WHERE CA008='{}'".format(cat_detial))[0][0]
        date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))  # 获取当前时间
        dada_sql = saomiao.objects.create(TA001=iphone, TA002=cat_detial, TA003=date, TA004=add_i)
        dada_sql.save()

        add_state = pysql("select replace(CA007,' ','') FROM RDMCA WHERE CA008='{}'".format(cat_detial))  # 得到是否司机调度
        return HttpResponse('OK')


def diaod_add(request):  #初始化签到信息\
    openid=request.session.get('openid')   #先找到司机信息
    iphone_all=PURMA.objects.filter(MA009=openid).values() ## @查询
    iphone=iphone_all[0].get('MA001')       #获取得到电话号码

    qiandao_mx=saomiao.objects.filter(TA001=iphone)   #获取签到信息
    data = qiandao_mx.values('TA002', 'TA003')  # 所有用户信息数据

    data_json = []
    for date_i in data:
        data_json.append(date_i)
    return JsonResponse(data=data_json, safe=False)

#调度获取本地址司机签到信息
def qiandao_list(request):  #
    openid=request.session.get('openid')   #先找到调度信息
    iphone_all=PURMA.objects.filter(MA009=openid).values() ## @查询
    iphone=iphone_all[0].get('MA001')       #获取得到电话号码

    qiandao_mx=saomiao.objects.filter(TA001=iphone)   #获取签到信息
    data_add = qiandao_mx.values('TA004')[0].get('TA004')  # 得到了具体得调度地址代号
    add_name=pysql("SELECT CA008 FROM RDMCA WHERE CA006='{}'".format(data_add))[0][0]   #得到地址名称
    qiandao_sj=saomiao.objects.filter(TA004=data_add).exclude(TA001=iphone)
    qianda_sj_mx=qiandao_sj.values('TA001','TA002','TA003')

    qianda_sj_mx=pysql("SELECT MA001,MA002,TD002,TD003,TA003,'{}' FROM cysystem_purma INNER JOIN PURTD ON TD001=MA001 inner join cysystem_saomiao ON TA001=MA001 WHERE TD006='Y' AND  TA004='{}' AND TA006='N' and MA010=0 order by TA003"
                       .format(add_name,data_add))

    return JsonResponse(data=qianda_sj_mx, safe=False)
#获取叉车信息
def chache(request):   #前台请求车型下拉列表
    aa = pysql("select replace(CC001,' ','') from RDMCC")
    bb = pysql("select replace(CD001,' ',''),replace(CD002,' ','') from RDMCD")
    AA = []
    BB = []
    BB_G = []
    for a in aa:
        AA.append(a[0])
        for b in bb:
            if b[0] == a[0]:
                BB_G.append(b[1])  # 加入过度
        BB.append(BB_G)
        BB_G = []
    #print(AA, BB)
    chache_data=[]
    chache_data.append(AA)
    chache_data.append(BB)
    return JsonResponse(data=chache_data, safe=False)
#获取装卸队伍信息
def zhuangxie(request):   #前台请求车型下拉列表
    chache=pysql("select replace(CB001,' ','') from RDMCB order by CB004 desc ")
    return JsonResponse(data=chache, safe=False)

def zhuangxie_state(request):   #前台请求车型下拉列表
    chache=pysql("select replace(CE001,' ','') from RDMCE")
    return JsonResponse(data=chache, safe=False)
#抓取运单号
def yundan_order(request):
    chache=pysql("exec PROC_NumIndent ")
    pysql_update("insert into  number VALUES ('{}')".format(chache[0][0]))    #单号插入记录表
    return JsonResponse(data=chache, safe=False)
#调度提交运单
def yundan_tj(request):    #司机扫描签到return HttpResponse('OK')
    openid = request.session.get('openid')  # 先找到司机信息
    iphone_all = PURMA.objects.filter(MA009=openid).values()  ## @查询
    iphone = iphone_all[0].get('MA001')  # 获取得到电话号码
    post_data = request.body
    post_data = json.loads(post_data)  # 转化S
    qiandao_time=post_data.get('model_4')
    if post_data.get('model_4') is None:
        qiandao_mx = saomiao.objects.filter(TA001=iphone).values()  # 获取签到信息
        qiandao_time = qiandao_mx[0].get('TA003')
    if post_data.get('biaozhi') == 1 :  #表示返厂运单
        yun_data=yundan(YUN01=post_data.get('yundan')[0][0],YUN02=iphone,YUN021=post_data.get('model_1'),YUN03=post_data.get('model_0'),YUN04=post_data.get('model_2'),YUN05=post_data.get('model_3')
                        ,YUN06=post_data.get('time'),YUN07=post_data.get('chache'),YUN08=post_data.get('zhuangxie')[0],YUN010=post_data.get('model_4'),YUN016=post_data.get('zhuangxie_state'),YUN018='返厂运单')
        yun_data.save()    #保存新增运单信息
    else:
        if post_data.get('chache') !=[] or post_data.get('chache') !='':
            chache = ''
            for data in post_data.get('chache'):
                chache = chache + data.get('zu') + ':' + data.get('mx') + ','
        yun_data = yundan(YUN01=post_data.get('yundan')[0][0], YUN02=iphone, YUN021=post_data.get('model_1'),YUN03=post_data.get('model_0'),
                      YUN04=post_data.get('model_2'), YUN05=post_data.get('model_3')
                      , YUN06=post_data.get('time'), YUN07=chache, YUN08=post_data.get('zhuangxie')[0],
                      YUN010=qiandao_time, YUN016=post_data.get('zhuangxie_state'),YUN018='常规运单',YUN022=post_data.get('add'))
        yun_data.save()  # 保存新增运单信息
    print('插入运单:'+post_data.get('yundan')[0][0])
    update_saomiao=saomiao.objects.filter(TA001=post_data.get('model_0')).update(TA006='Y')   #更新签到信息已经用过了
    return  HttpResponse('OK')
#y运单作业,抓取已经生成运单的报表
def yundan_list_beifen(request):  #
    openid=request.session.get('openid')   #先找到调度信息
    iphone_all=PURMA.objects.filter(MA009=openid).values() ## @查询
    iphone=iphone_all[0].get('MA001')       #获取得到电话号码
    post_data = request.body
    post_data = json.loads(post_data)  # 转化S
    page=post_data.get('page')
    date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))  # 获取当前时间
    date=date.timedelta(days=-3)+'001'

    yundan_mx=yundan.objects.filter(Q(YUN02=iphone),Q(YUN01__gte=date)).exclude(YUN017='Y')   #获取本调度的所有运单明细,且是未关闭的
    siji = yundan_mx.values('YUN01','YUN03','YUN04','YUN05','YUN011','YUN015','YUN013','YUN017','YUN018').order_by("-YUN01") # 司机,车辆,车型,装货完成
    data_json = []
    for date_i in siji:
        data_json.append(date_i)
    return JsonResponse(data=data_json, safe=False)
def yundan_list(request):  #
    openid=request.session.get('openid')   #先找到调度信息
    iphone_all=PURMA.objects.filter(MA009=openid).values() ## @查询
    iphone=iphone_all[0].get('MA001')       #获取得到电话号码

    yundan_mx=yundan.objects.filter(YUN02=iphone).exclude(YUN017='Y')   #获取本调度的所有运单明细,且是未关闭的
    siji = yundan_mx.values('YUN01','YUN03','YUN04','YUN05','YUN011','YUN015','YUN013','YUN017','YUN018').order_by("-YUN01") # 司机,车辆,车型,装货完成
    data_json = []
    for date_i in siji:
        data_json.append(date_i)
    data_json=data_json[:15]      #限制显示前30条
    return JsonResponse(data=data_json, safe=False)
def yundan_zhuangxie(request):    #司机扫描签到return HttpResponse('OK')
    post_data = request.body
    yundan_or = json.loads(post_data).get('yundan_order')  # 单号
    yundan_time=json.loads(post_data).get('time')
    if json.loads(post_data).get('biaozhi') == '0':   #装卸时间
        yundan.objects.filter(YUN01=yundan_or).update(YUN011='Y',YUN012=yundan_time)
        return HttpResponse('OK')
    elif json.loads(post_data).get('biaozhi') == '1':   #提交离场时间
        yundan.objects.filter(YUN01=yundan_or).update(YUN013='Y', YUN014=yundan_time)
        return  HttpResponse('OK')
    elif json.loads(post_data).get('biaozhi') == '2':   #运单关闭
        yundan.objects.filter(YUN01=yundan_or).update(YUN017='Y')
        return  HttpResponse('OK')

def sku(request):   #前台请求商品信息下拉列表
    sku_mx = pysql("select replace(SKU01,' ',''),replace(SKU02,' ','') from cysystem_sku WHERE SKU05='Y'")
    return JsonResponse(data=sku_mx, safe=False)
#初始化加载地址信息
def add(request):   #前台请求商品信息下拉列表
    add_mx = pysql("select replace(CA008,' ','') from RDMCA WHERE CA005='启用'")
    return JsonResponse(data=add_mx, safe=False)

def order_tj(request):    #司机扫描签到return HttpResponse('OK')
    post_data = request.body
    post_data = json.loads(post_data)  # 转化
    yundan_num=post_data.get('model_1')     #运单号
    order_num=post_data.get('order')        #订单号
    add=post_data.get('add')            #地址信息
    sku_list=post_data.get('sku_list')  #商品列表
    print(post_data,sku_list)
    for sku in sku_list:
        order_data=YUN_ORDER(OR001=yundan_num,OR002=order_num,OR003=add,OR004=sku['name'][0],OR006=sku['name'][1],OR008=sku['ban'],OR009=sku['dun'])
        order_data.save()
    #update_YUNDAN=yundan.objects.filter(YUN01=post_data.get('model_1')).update(YUN015='Y')   #更新签到信息已经用过了
    return  HttpResponse('OK')

#订单提交完,系统自动更新抓取本运单最新订单信息
def order_list_get(request):  #
    post_data = request.body
    #print(post_data)
    post_data = json.loads(post_data)  # 转化
    yundan_num = post_data.get('yundan_num')  # 运单号

    order_mx=YUN_ORDER.objects.filter(OR001=yundan_num,).distinct()   #去重查询
    siji = order_mx.values('OR002') # 抓取单号
    data_json = []
    for date_i in siji:
        data_json.append(date_i)
    return JsonResponse(data=data_json, safe=False)

#删除订单
def delete_order(request):
    post_data = request.body
    #print(post_data)
    post_data = json.loads(post_data)  # 转化
    order_num = post_data.get('order_num')['OR002']   #订单号
    del_order = YUN_ORDER.objects.filter(OR002=order_num)
    del_order.delete()
    return HttpResponse('OK')

def yundan_order_tj(request):    #运单维护完全部订单信息,然后提交
    post_data = request.body
    post_data = json.loads(post_data)  # 转化
    xjak=post_data.get('yun_order')

    update_ORDER=YUN_ORDER.objects.filter(OR001=post_data.get('yun_order')).update(OR007='Y')   #订单明细已经提交
    update_saomiao = yundan.objects.filter(YUN01=post_data.get('yun_order')).update(YUN015='Y')  # 运单信息货物维护完成

    order_hz = pysql("select  OR002 FROM cysystem_yun_order where OR001='{}'".format(xjak))     #得到所有订单号汇总
    order = ''
    for data in order_hz:
        order = order + ' ' + data[0]
    update_hz = yundan.objects.filter(YUN01=post_data.get('yun_order')).update(YUN023=order)  # 运单信息货物维护完成
    print(order)
    return  HttpResponse('OK')
#司机到达获取运输列表
def yundan_task(request):  #
    openid=request.session.get('openid')   #先找到调度信息
    iphone_all=PURMA.objects.filter(MA009=openid).values() ## @查询
    iphone=iphone_all[0].get('MA001')       #获取得到电话号码

    task_mx=pysql("select distinct YUN01,OR002,OR003,OR010,OR011,OR013 from cysystem_yundan INNER JOIN cysystem_yun_order ON YUN01=OR001 WHERE YUN03='{}' and YUN013='Y' and OR013 !='Y'".format(iphone))
    print(iphone,task_mx)
    return JsonResponse(data=task_mx, safe=False)

#司机点击到达按钮
def sjji_arrival(request):    #运单维护完全部订单信息,然后提交
    post_data = request.body
    post_data = json.loads(post_data)  # 转化
    order=post_data.get('order')
    yundan=post_data.get('yundan')   #运单号
    print(order,yundan)
    date = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))  # 获取当前时间
    update_ORDER=YUN_ORDER.objects.filter(OR001=yundan,OR002=order).update(OR010='Y',OR015=date)   #订单明细已经提交

    return  HttpResponse('OK')

#司机开始卸货
def benning_xie(request):    #司机扫描签到return HttpResponse('OK')
    post_data = request.body
    year=time.strftime('%Y-%m-%d',time.localtime(time.time()))
    yundan_or = json.loads(post_data).get('yundan_order')  # 运单号
    order = json.loads(post_data).get('order')  # 订单号
    yundan_time=json.loads(post_data).get('time')
    if json.loads(post_data).get('biaozhi') == '0':   #开始装卸时间
        print(yundan_time)
        YUN_ORDER.objects.filter(OR001=yundan_or,OR002=order).update(OR011='Y',OR012=yundan_time)
        return HttpResponse('OK')
    elif json.loads(post_data).get('biaozhi') == '1':   #x卸货完成离场时间
        YUN_ORDER.objects.filter(OR001=yundan_or, OR002=order).update(OR013='Y', OR014=yundan_time)
        return  HttpResponse('OK')

  #登录界面判定显示权限!!
def tabbar(request):    #司机扫描签到return HttpResponse('OK')
    openid = request.session.get('openid')  # 先找到司机信息
    iphone_all = PURMA.objects.filter(MA009=openid).values()  ## @查询
    try:   #退出登录时,无法查询
        iphone_id = iphone_all[0].get('MA010')  # 得到司机或者调度标识
    except:
        return HttpResponse('4')  # 未登录
    if iphone_id==0:  #司机
        return HttpResponse('0')
    elif iphone_id == 1:
        return HttpResponse('1')
    elif pysql("select *  from ADMMF where MF010='{}'".format(openid)) :
        return HttpResponse('9')    #超级管理员
    else:
        return HttpResponse('3')   #无权限

def user_info(request):    #登录获取用户信息
    openid = request.session.get('openid')  # 先找到司机信息
    iphone_all = PURMA.objects.filter(MA009=openid).values()  ## @查询
    try:
        iphone_id = iphone_all[0].get('MA001')  # 得到电话
    except:
        return HttpResponse('欢迎首次登录')  # 返回电话号
    if iphone_id:  #存在用户
        return HttpResponse(iphone_id)    #返回电话号
    elif pysql("select *  from ADMMF where MF010='{}'".format(openid)) :
        return HttpResponse(iphone_id)    #超级管理员
#用户退出
def user_out(request):    #登录获取用户信息
    openid = request.session.get('openid')  # 先找到司机信息
    PURMA.objects.filter(MA009=openid).update(MA009='')  ## 清空登录信息
    pysql_update("update ADMMF SET MF010='' WHERE MF010='{}'".format(openid))  #清空超级管理员

    return HttpResponse('OK')    #超级管理员

def siji_select(request):    #司机报表信息查询
    openid = request.session.get('openid')  # 先找到司机信息
    iphone_all = PURMA.objects.filter(MA009=openid).values()  ## @查询
    iphone = iphone_all[0].get('MA001')  # 获取得到电话号码
    post_data = request.body
    post_data=json.loads(post_data)
    begin_date=post_data.get('begin_date')
    end_date=post_data.get('end_date')           #获取起止时间
    #查询数据
    data=pysql("select  YUN01,OR002,YUN022,OR003 FROM cysystem_yundan INNER JOIN cysystem_yun_order ON YUN01=OR001 WHERE OR013='Y' AND SUBSTRING (OR014,1,10)  >='{}' AND SUBSTRING (OR014,1,10) <='{}' and YUN03='{}'  ".format(begin_date,end_date,iphone))
    list = []
    dict = {}
    for data_i in data:
        dict['mon'] = data_i[0]
        dict['code'] = data_i[1]
        dict['text'] = data_i[2]
        dict['type'] = data_i[3]
        list.append(dict)
        dict = {}
    return JsonResponse(data=list, safe=False)
def diaodu_select(request):    #调度报表信息查询
    openid = request.session.get('openid')  # 先找到司机信息
    iphone_all = PURMA.objects.filter(MA009=openid).values()  ## @查询
    iphone = iphone_all[0].get('MA001')  # 获取得到电话号码
    post_data = request.body
    post_data=json.loads(post_data)
    begin_date=post_data.get('begin_date')
    end_date=post_data.get('end_date')           #获取起止时间
    #查询数据
    data=pysql("select YUN01,OR002,SUM(OR008),SUM(OR009),YUN04,YUN022,OR003 FROM cysystem_yundan INNER JOIN cysystem_yun_order ON YUN01=OR001 WHERE OR013='Y' AND SUBSTRING (OR014,1,10)  >='{}' AND SUBSTRING (OR014,1,10) <='{}' and YUN02='{}' GROUP BY YUN01,OR002,YUN04,OR003,YUN022 ".format(begin_date,end_date,iphone))
    list = []
    dict = {}
    for data_i in data:
        dict['mon'] = data_i[0]
        dict['code'] = data_i[1]
        dict['ban'] = data_i[2]
        dict['dun'] = data_i[3]
        dict['che'] = data_i[4]
        dict['add'] = data_i[5]
        dict['add_end'] = data_i[6]
        list.append(dict)
        dict = {}
    print(list)
    return JsonResponse(data=list, safe=False)
def gonggao(request):    #查询公告信息
    #查询数据
    data=pysql(" select TA002 FROM RDMTA")[0][0]
    print(data)
    return JsonResponse(data=data, safe=False)

def get_yundan_skulis(request):
    post_data = request.body
    post_data = json.loads(post_data)
    yundan_num = post_data.get('yun_order')
    sku_mx = pysql("select OR006,OR008,OR009 from cysystem_yun_order WHERE OR001='{}'".format(yundan_num))
    list = []
    dict = {}
    for data_i in sku_mx:
        dict['name'] = data_i[0]
        dict['ban'] = data_i[1]
        dict['dun'] = data_i[2]
        list.append(dict)
        dict = {}
    print(yundan_num,'装车明细:',list)
    return JsonResponse(data=list, safe=False)

def siji(request):   #前台请求所有司机信息
    chache = pysql("select MA001,MA002,TD002,TD003 from cysystem_purma INNER JOIN PURTD ON MA001=TD001 where MA010=0")
    print(chache)
    return JsonResponse(data=chache, safe=False)


def yichang(request):    #司机扫描签到return HttpResponse('OK')
    post_data = request.body
    post_data = json.loads(post_data)  # 转化

    dada_sql = YUN_YI.objects.create(YI001=post_data.get('yundan_order'), YI002=post_data.get('yi'))
    dada_sql.save()
    return HttpResponse('OK')

def token(request):    #微信签名
    try:
        # 请求无参数，即非 token 验证

        signature = request.GET.get('signature')
        nonce = request.GET.get('nonce')
        timestamp = request.GET.get('timestamp')
        echostr = request.GET.get('echostr')
        token = "zmy518518"  # 基本配置的 token 填写一样的值
        # 对 token timestamp nonce 进行排序后进行摘要
        sha1_list = [token, timestamp, nonce]
        sha1_list.sort()
        sha1 = hashlib.sha1()
        list(map(lambda s: sha1.update(s.encode('utf-8')), sha1_list))
        hashcode = sha1.hexdigest()
        print('func: hashcode, signature: {}  {}'.format(hashcode, signature))
        if hashcode == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("")
    except Exception as e:
        return HttpResponse(e.reason)

def yundan_close(request):    #返厂运单关闭，并提交运单信息
    post_data = request.body
    yundan_or = json.loads(post_data).get('yundan_order')  # 单号
    note= json.loads(post_data).get('note')  # 备注
    zhuangxie= json.loads(post_data).get('zhuangxie')  # 装卸队

    yundan.objects.filter(YUN01=yundan_or).update(YUN019=note,YUN020=zhuangxie,YUN017='Y')
    return HttpResponse('OK')

def arrival_list(request):  #  司机到达。通知调度
    openid=request.session.get('openid')   #先找到调度信息
    iphone_all=PURMA.objects.filter(MA009=openid).values() ## @查询
    iphone=iphone_all[0].get('MA001')       #获取得到电话号码

    qiandao_mx=saomiao.objects.filter(TA001=iphone)   #获取签到信息
    data_add = qiandao_mx.values('TA004')[0].get('TA004')  # 得到了具体得调度地址代号
    add_name=pysql("select CA008 FROM RDMCA WHERE CA006='{}'".format(data_add))   #得到了调度的默认地址
    add_name=add_name[0][0] #转换格式

    qianda_sj_mx=pysql("SELECT OR001,OR002,YUN03,YUN04,YUN05,YUN021,OR015 FROM cysystem_yun_order INNER JOIN cysystem_yundan ON YUN01=OR001  WHERE OR010='Y' AND  OR003='{}' AND OR013='N' and YUN018='常规运单' "
                       .format(add_name))

    return JsonResponse(data=qianda_sj_mx, safe=False)

def fan_list(request):  #  司机到达。返厂列表
    openid=request.session.get('openid')   #先找到调度信息
    iphone_all=PURMA.objects.filter(MA009=openid).values() ## @查询
    iphone=iphone_all[0].get('MA001')       #获取得到电话号码

    qiandao_mx=saomiao.objects.filter(TA001=iphone)   #获取签到信息
    data_add = qiandao_mx.values('TA004')[0].get('TA004')  # 得到了具体得调度地址代号
    add_name=pysql("select CA008 FROM RDMCA WHERE CA006='{}'".format(data_add))   #得到了调度的默认地址
    add_name=add_name[0][0] #转换格式

    qianda_sj_mx=pysql("SELECT OR001,OR002,YUN03,YUN04,YUN05,YUN021,OR015 FROM cysystem_yun_order INNER JOIN cysystem_yundan ON YUN01=OR001  WHERE OR010='Y' AND  OR003='{}' and YUN017='N' and YUN018='返厂运单' "
                       .format(add_name))

    return JsonResponse(data=qianda_sj_mx, safe=False)
def xiehuo_chache(request):    #司机扫描签到return HttpResponse('OK')

    post_data = request.body
    post_data = json.loads(post_data)  # 转化
    yundan_order=post_data.get('yundan_order')   #运单号
    order=post_data.get('order')         #订单号
    chache=post_data.get('chache')         #叉车组
    note=post_data.get('note')         #备注
    chache_ji = ''
    for data in chache:
        chache_ji =chache_ji + data.get('zu') + ':' + data.get('mx') + ','

    YUN_ORDER.objects.filter(OR001=yundan_order,OR002=order).update(OR016=chache_ji, OR017=note)
    return  HttpResponse('OK')