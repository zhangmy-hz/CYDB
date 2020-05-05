from django.db import models

class User_CY(models.Model):
    name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

class PURMA(models.Model):   #司机信息表
    MA001=models.CharField(max_length=11,primary_key=True)
    MA002=models.CharField(max_length=30)
    MA003=models.CharField(max_length=50)
    MA004=models.CharField(max_length=30)
    MA005=models.CharField(max_length=300)
    MA006=models.CharField(max_length=10)
    MA007=models.CharField(max_length=20)
    MA008=models.CharField(max_length=10)
    MA009=models.CharField(max_length=32,null=True)   #默认为空
    MA010=models.IntegerField(default=0)      ##标记司机或者调度.0==司机;1==调度
class PURTC(models.Model):   #车型信息表
    TC001=models.CharField(max_length=20,primary_key=True)
    TC002 = models.CharField(max_length=20, null=True)  # 默认为空
    TC003 = models.CharField(max_length=10, null=True)  # 默认为空
    TC004 = models.CharField(max_length=10, null=True)  # 默认为空
    TC005 = models.CharField(max_length=10, null=True)  # 默认为空
    TC006 = models.CharField(max_length=255, null=True)  # 默认为空
    TC007 = models.CharField(max_length=10, null=True)  # 默认为空
    TC008 = models.CharField(max_length=60, null=True)  # 默认为空
    TC009 = models.CharField(max_length=255, null=True)  # 默认为空
#class PURTD(models.Model):   #司机绑定车身
    #TD001=models.CharField(max_length=120,primary_key=True)
    #TD002=models.CharField(max_length=20,primary_key=True)
    #TD003=models.CharField(max_length=20,null=True)
    #TD004=models.CharField(max_length=20,null=True)
    #TD005=models.CharField(max_length=20,null=True)
    #TD006=models.CharField(max_length=10,null=True)
class saomiao(models.Model):
    TA001=models.CharField(max_length=20)
    TA002=models.CharField(max_length=255)
    TA003=models.CharField(max_length=50)
    TA004=models.IntegerField(default=0)
    TA006=models.CharField(max_length=5,default='N')
#记录运单信息
class yundan(models.Model):
    YUN01=models.CharField(max_length=20,primary_key=True)
    YUN02=models.CharField(max_length=20)
    YUN03=models.CharField(max_length=20)
    YUN04=models.CharField(max_length=20)
    YUN05=models.CharField(max_length=20)
    YUN06=models.CharField(max_length=20)
    YUN07=models.CharField(max_length=200)
    YUN08=models.CharField(max_length=20)
    YUN010=models.CharField(max_length=20,null=True)
    YUN011=models.CharField(max_length=20,default='N')
    YUN012=models.CharField(max_length=20,default='00-00-00')
    YUN013=models.CharField(max_length=20,default='N')
    YUN014 = models.CharField(max_length=20, default='00-00-00')
    YUN015 = models.CharField(max_length=20, default='N')
    YUN016 = models.CharField(max_length=20,null=True)
    YUN017 = models.CharField(max_length=4, default='N')
    YUN018 = models.CharField(max_length=10, null=True)
    YUN019 = models.CharField(max_length=80, null=True)
    YUN020 = models.CharField(max_length=40, null=True)
    YUN021 = models.CharField(max_length=20, null=True)   #司机姓名
    YUN022 = models.CharField(max_length=50, null=True)
    YUN023 = models.CharField(max_length=200, null=True)
#记录SKU信息表
class SKU(models.Model):
    SKU01=models.CharField(max_length=20,primary_key=True)
    SKU02=models.CharField(max_length=40,null=True)
    SKU03=models.FloatField(default=0)
    SKU04=models.FloatField(default=0)
    SKU05=models.CharField(max_length=2,default='Y')
#运单对应得订单明细
class YUN_ORDER (models.Model):
    OR001=models.CharField(max_length=20,null=True)
    OR002=models.CharField(max_length=100,null=True)
    OR003=models.CharField(max_length=40,null=True)
    OR004=models.CharField(max_length=20,null=True)
    OR005=models.IntegerField(default=0)
    OR006 = models.CharField(max_length=20, null=True)
    OR007 = models.CharField(max_length=20, null=True)
    OR008 = models.FloatField(default=0,max_length=10)
    OR009 = models.FloatField(default=0,max_length=10)
    OR010 = models.CharField(max_length=20, default='N')
    OR011 = models.CharField(max_length=20,default='N')
    OR012 = models.CharField(max_length=20,null=True)
    OR013 = models.CharField(max_length=20,default='N')
    OR014 = models.CharField(max_length=30, null=True)
    OR015 = models.CharField(max_length=30, null=True)
    OR016 = models.CharField(max_length=200, null=True)
    OR017 = models.CharField(max_length=100, null=True)

class YUN_YI (models.Model):   #运单异常
    YI001=models.CharField(max_length=20,null=True)
    YI002=models.CharField(max_length=255,null=True)
