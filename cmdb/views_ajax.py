# -*- coding: UTF-8 -*- 

import datetime
import json

from django.contrib.auth.hashers import check_password, make_password
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from cmdb.models import host


@csrf_exempt    
def addChangeHostInfo(request):
    '''
    新增主机
    修改主机
    '''
    v_hostId = request.POST.get('host_id')
    v_businessName = request.POST.get('business_name')
    v_serviceEnv = request.POST.get('service_env')
    v_hostName = request.POST.get('host_name')
    v_intranetIpAddr = request.POST.get('intranet_ipaddr')
    v_publicIpAddr = request.POST.get('public_ipaddr')
    v_sshPort = request.POST.get('ssh_port')
    v_hostType = request.POST.get('host_type')
    v_hostRole = request.POST.get('host_role')
    v_hostDesc = request.POST.get('host_desc')
    
    print(v_hostId, v_businessName, v_serviceEnv, v_hostName, v_intranetIpAddr, v_publicIpAddr, v_sshPort, v_hostType, v_hostRole, v_hostDesc)
        
    if v_hostId == '' or v_hostId is None:
        # 新增
        try:   
            hostObj = host(businessName=v_businessName, serviceEnv=v_serviceEnv, hostName=v_hostName, intranetIpAddr=v_intranetIpAddr, publicIpAddr=v_publicIpAddr, sshPort=v_sshPort, hostType=v_hostType, hostRole=v_hostRole, hostDesc=v_hostDesc)
            hostObj.save()
            result = {'status':1, 'msg':'保存成功!', 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')
        except Exception as e:
            result = {'status':2, 'msg':'保存失败!'+str(e), 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')        
    else:
        # 修改
        try:
            hostObj = host.objects.filter(id=v_hostId)
            hostObj.update(businessName=v_businessName, serviceEnv=v_serviceEnv, hostName=v_hostName, intranetIpAddr=v_intranetIpAddr, publicIpAddr=v_publicIpAddr, sshPort=v_sshPort, hostType=v_hostType, hostRole=v_hostRole, hostDesc=v_hostDesc)
#             masterConfigObj.save()
            result = {'status':1, 'msg':'修改成功!', 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')
        except Exception as e:
            result = {'status':2, 'msg':'修改失败!'+str(e), 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')      


@csrf_exempt
def getHostDetailInfo(request):
    hostId = request.POST['hostId']
    
    try:
        hostObj = host.objects.get(id=hostId)
        hostJson = hostObj.toJSON()
        
        result = {'status':1, 'msg':'请求成功', 'obj':hostJson}
        print(result)
        return HttpResponse(json.dumps(result), content_type='application/json')
    except Exception as e:
        print(e)
        result = {'status':2, 'msg':'请求失败!'+str(e), 'data':''}
        return HttpResponse(json.dumps(result), content_type='application/json')
  
        
# @csrf_exempt    
# def delUser(request):
#     v_userId = request.POST['userId']
# 
#     if v_userId == "" or v_userId is None:
#         result = {'status':3, 'msg':'未选中任何记录!', 'data':''}
#         return HttpResponse(json.dumps(result), content_type='application/json')
#     else:    
#         try:
#             delResult = users.objects.filter(id=v_userId).delete()
#             print(delResult)
#             result = {'status':1, 'msg':'删除成功!', 'data':''}
#             return HttpResponse(json.dumps(result), content_type='application/json')            
#         except Exception as e:
#             print(e)
#             result = {'status':2, 'msg':'删除失败!'+str(e), 'data':''}
#             return HttpResponse(json.dumps(result), content_type='application/json')
#         
# @csrf_exempt    
# def resetUserPasswd(request):
#     v_userId = request.POST['userId']
# 
#     if v_userId == "" or v_userId is None:
#         result = {'status':3, 'msg':'未选中任何记录!', 'data':''}
#         return HttpResponse(json.dumps(result), content_type='application/json')
#     else:    
#         try:
#             userObj = users.objects.filter(id=v_userId)
#             userObj.update(password=make_password('111111'))
#             result = {'status':1, 'msg':'重置密码成功!', 'data':''}
#             return HttpResponse(json.dumps(result), content_type='application/json')            
#         except Exception as e:
#             print(e)
#             result = {'status':2, 'msg':'重置密码失败!'+str(e), 'data':''}
#             return HttpResponse(json.dumps(result), content_type='application/json')
