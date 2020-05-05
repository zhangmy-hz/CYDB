
from django.contrib import admin
from django.urls import path
from cysystem import views as myviews
from cysystem import OCR as OCR
from cysystem import view_diaodu as diaoduviews
from cysystem import  message

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/',myviews.login_check),
    path('cs/',myviews.HelloWorld),  #引入响应测试
    path('mytest/',myviews.mythree),  #引入响应测试
    path('login/',myviews.login),  #引入响应测试
    path('open_api/',myviews.openid),  #引入响应测试
    path('cookie/',myviews.cookie),  #测试session
    path('cat_type/',myviews.cat_type),  #测试session
    path('cat_sure/',myviews.cat_sure),  #绑定车型,提交返回
    path('cat_now/',myviews.cat_now),  #请求默认的司机和车型,系统初次加载
    path('saomiao/',myviews.saomiao_1),  #司机扫描签到
    path('saomiao_diaodu/',diaoduviews.saomiao_1),  #调度扫描默认地址
    path('saomiao_diaodu_sj/',diaoduviews.saomiao_2),  #调度扫描默认地址
    path('qiandao/',myviews.qiandao),  #初始化获取签到信息
    path('diaod_add/',diaoduviews.diaod_add),  #\初始化调度默认地址
    path('qiandao_list/',diaoduviews.qiandao_list),  #调度获取签到列表
    path('chache/',diaoduviews.chache),  #调度初始化调取叉车信息
    path('zhuangxie/',diaoduviews.zhuangxie),  #调度初始化调取装卸信息
    path('zhuangxie_state/',diaoduviews.zhuangxie_state),  #调度初始化调取装卸货物类型信息
    path('yundan_order/',diaoduviews.yundan_order),  #调度初始化抓取运单号
    path('yundan_tj/',diaoduviews.yundan_tj),  #调度提交完整运单信息
    path('order_tj/',diaoduviews.order_tj),  #订单信息填写
    path('yundan_list/',diaoduviews.yundan_list),  #运单作业,抓取运单明细
    path('yundan_list_beifen/',diaoduviews.yundan_list_beifen),  #运单作业,抓取运单明细
    path('order_list_get/',diaoduviews.order_list_get),  #运单作业,抓取运单明细
    path('yundan_zhuangxie/',diaoduviews.yundan_zhuangxie),  #运单装货结束
    path('sku/',diaoduviews.sku),  #请求SKU列表信息
    path('add/',diaoduviews.add),  #请求SKU列表信息
    path('delete_order/',diaoduviews.delete_order),  #删除订单
    path('yundan_order_tj/',diaoduviews.yundan_order_tj),  #运单维护完具体的订单信息提交
    path('yundan_task/',diaoduviews.yundan_task),  #司机到达运输任务
    path('sjji_arrival/',diaoduviews.sjji_arrival),  #司机送货提交到达按钮
    path('benning_xie/',diaoduviews.benning_xie),  #司机送货卸货开始
    path('tabbar/',diaoduviews.tabbar),  #登录判断显示不同得tabbar
    path('user_info/',diaoduviews.user_info),  #登录判断用户信息
    path('user_out/',diaoduviews.user_out),  #用户退出
    path('siji_select/',diaoduviews.siji_select),  #司机查看运输报表
    path('diaodu_select/',diaoduviews.diaodu_select),  #diaodu查看运输报表
    path('add_select/',diaoduviews.add_select),  #调度初始化加载所有地址信息
    path('gonggao/',diaoduviews.gonggao),  #获取公告信息
    path('get_yundan_skulis/',diaoduviews.get_yundan_skulis),  #获取公告信息
    path('siji/',diaoduviews.siji),  #默认加载所有司机信息
    path('yichang/',diaoduviews.yichang),  #默认加载所有司机信息
    path('token/',diaoduviews.token),  #微信令牌验证
    path('message/',message.notifications),  #订阅消息
    path('yundan_close/',diaoduviews.yundan_close),  #运单关闭
    path('arrival_list/',diaoduviews.arrival_list),  #司机送货到达列表
    path('fan_list/',diaoduviews.fan_list),  #司机返厂到达列表
    path('xiehuo_chache/',diaoduviews.xiehuo_chache),  #司机返厂到达列表,选择叉车组和备注
    #path('media/', myviews.media),  # 记录微信id
    path('photo/', OCR.photo),  # 记录微信id
]
