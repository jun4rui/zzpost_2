from django.core import serializers
from django.shortcuts import render


# Create your views here.

from django.http import HttpResponse
from json import loads, dumps

from weixinpost.models import *


def test(request):
    return render(request, 'test.html', {'str1': '111111111', 'str2': '222222two'})


def order(request):
    return render(request, 'order.html')


def order_list(request):
    return render(request, 'order-list.html')


# 用户查询订单记录处理
def order_list_ajax(request):
    username = request.GET['username']
    phone = request.GET['phone']

    # 定义默认返回用的json
    return_json = {
        'order': '',
        'error_message': '',
        'status': -1
    }

    errMsg = '';
    if username=='':
        errMsg += '用户姓名不存在\n'
    if phone=='':
        errMsg += '用户电话不存在\n'
    # 出错的返回处理
    if errMsg!='':
        return_json['error_message'] = errMsg
    # 查询结果并显
    else:
        orderInfoList = OrderInfo.objects.filter(senderName=username, phoneNumber=phone)
        return_json['order'] = serializers.serialize('json', list(orderInfoList))
        return_json['status'] = 0
    return HttpResponse(dumps(return_json), content_type='application/json')


# 用户订单信息提交处理
def order_ajax(request):
    # print(request.GET)
    print('username='+request.GET['username'])
    print('phone='+request.GET['phone'])
    print('fromaddress='+request.GET['fromaddress'])

    # 定义默认返回用的json
    return_json = {
        'order': {},
        'error_message': '',
        'status': -1
    }

    # 检查传入信息
    errMsg = ''
    if request.GET['username']=='':
        errMsg += '没有用户名\n'
    if request.GET['phone']=='':
        errMsg += '没有联系电话\n'
    if request.GET['fromaddress']=='':
        errMsg += '没有寄件地址'
    # 传入参数出错, 则修改返回json
    if errMsg!='':
        return_json['error_message'] = errMsg
    else:
        # 如果参数OK，则将订单记录到订单表中，并返回订单

        new_orderInfo = OrderInfo.objects.create(
            senderName=request.GET['username'],
            phoneNumber=request.GET['phone'],
            fromAddress=request.GET['fromaddress']
        )
        # print(new_orderInfo)
        return_json['status'] = 0

    return HttpResponse(dumps(return_json), content_type='application/json')
