#调用百度OCR  API接口
import  requests,json,os
import base64,hashlib
from django.shortcuts import render,HttpResponse
from django.http import JsonResponse  #引入json响应

def photo(request):
    # client_id 为官网获取的AK， client_secret 为官网获取的SK
    AK = 'xzCjEQIDQ9YFMCi7RYhDazvL'
    SK = '1KOtTkrRdxStoN1bmfhZVuMDSQvRdplj'
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + AK + '&client_secret=' + SK
    response = requests.get(host).json()
    access_token = response.get('access_token')

    '''post_data = request.body
    post_data = json.loads(post_data)  # 转化
    print(post_data.get('img_url'))
    '''

    files = request.FILES
    # 取出文件的 key 和 value
    for key, value in files.items():
        # 读取文件
        content = value.read()
        content=base64.b64encode(content)    #百度只能支持64位转码

    params = {"image": content}   #图片内容
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"+ "?access_token=" + access_token   #百度图像识别地址

    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        data=response.json()
        words_result=data.get('words_result')
        print(words_result)
        if words_result == []:  #为空，表示图片上根本没有文字，无法返回信息
            return HttpResponse('001')  # 返回识别的结果,识别不是24开头，结果不对
        else:
            words_result=words_result[0]
            words=words_result.get('words')    #得到第一个识别框的结果，对不准就不管了了

            if words[:2] =='24' or words[:2] =='25' :   #规定单号都是24开头
                return HttpResponse(words)      #返回识别的结果
            else:
                return HttpResponse('001')  # 返回识别的结果,识别不是24开头，结果不对
    else:
        return HttpResponse ('NOT OK')


