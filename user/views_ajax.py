# -*- coding: UTF-8 -*- 

import datetime
import json

from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import users


login_failure_counter = {} #登录失败锁定计数器，给loginAuthenticate用的
sqlSHA1_cache = {} #存储SQL文本与SHA1值的对应关系，尽量减少与数据库的交互次数,提高效率。格式: {工单ID1:{SQL内容1:sqlSHA1值1, SQL内容2:sqlSHA1值2},}

#ajax接口，登录页面调用，用来验证用户名密码
@csrf_exempt
def loginAuthenticate(username, password):
    """登录认证，包含一个登录失败计数器，5分钟内连续失败5次的账号，会被锁定5分钟"""
    lockCntThreshold = 5
    lockTimeThreshold = 300

    #服务端二次验证参数
    strUsername = username
    strPassword = password
    if strUsername == "" or strPassword == "" or strUsername is None or strPassword is None:
        result = {'status':2, 'msg':'登录用户名或密码为空，请重新输入!', 'data':''}
    elif strUsername in login_failure_counter and login_failure_counter[strUsername]["cnt"] >= lockCntThreshold and (datetime.datetime.now() - login_failure_counter[strUsername]["last_failure_time"]).seconds <= lockTimeThreshold:
        result = {'status':3, 'msg':'登录失败超过5次，该账号已被锁定5分钟!', 'data':''}
    else:
        correct_users = users.objects.filter(username=strUsername,is_active=1)
        if len(correct_users) == 0:
            result = {'status':4, 'msg':'该用户不存在!', 'data':''}
        elif len(correct_users) == 1 and check_password(strPassword, correct_users[0].password) == True:
            #调用了django内置函数check_password函数检测输入的密码是否与django默认的算法相匹配
            if strUsername in login_failure_counter:
                #如果登录失败计数器中存在该用户名，则清除之
                login_failure_counter.pop(strUsername)
            result = {'status':0, 'msg':'ok', 'data':''}
        else:
            if strUsername not in login_failure_counter:
                #第一次登录失败，登录失败计数器中不存在该用户，则创建一个该用户的计数器
                login_failure_counter[strUsername] = {"cnt":1, "last_failure_time":datetime.datetime.now()}
            else:
                if (datetime.datetime.now() - login_failure_counter[strUsername]["last_failure_time"]).seconds <= lockTimeThreshold:
                    login_failure_counter[strUsername]["cnt"] += 1
                else:
                    #上一次登录失败时间早于5分钟前，则重新计数。以达到超过5分钟自动解锁的目的。
                    login_failure_counter[strUsername]["cnt"] = 1
                login_failure_counter[strUsername]["last_failure_time"] = datetime.datetime.now()
            result = {'status':1, 'msg':'用户名或密码错误，请重新输入！', 'data':''}
    return result

#ajax接口，登录页面调用，用来验证用户名密码
@csrf_exempt
def authenticateEntry(request):
    """接收http请求，然后把请求中的用户名密码传给loginAuthenticate去验证"""
    if request.is_ajax():
        strUsername = request.POST.get('username')
        strPassword = request.POST.get('password')
    else:
        strUsername = request.POST['username']
        strPassword = request.POST['password']
    result = loginAuthenticate(strUsername, strPassword)
    if result['status'] == 0:
        request.session['login_username'] = strUsername
    return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_exempt
def changePasswdCheck(loginUser, passwd1, pssswd2):
    password = passwd1
    confirmPassword = pssswd2
    userName = loginUser
    
    userObj = users.objects.get(username=userName)
    
    if password == "" or password is None or confirmPassword == "" or confirmPassword is None:
        result = {'status':2, 'msg':'密码不能为空，请重新输入!', 'data':''}
    elif password != confirmPassword:
        result = {'status':3, 'msg':'密码不一致，请重新输入!', 'data':''}
    else:
        userObj.password = make_password(password)
        userObj.save()
        result = {'status':1, 'msg':'修改密码成功!', 'data':''}
    return result

@csrf_exempt
def changePasswd(request):
    '''
    @author: XinPeng
    @date: 2017-11-30 20:01:05
    @description: 通过ajax接口，修改用户密码
    @returns: json
    '''
    if request.is_ajax():
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirm_password')
    else:
        password = request.POST['password']
        confirmPassword = request.POST['confirm_password']
    
    loginUser = request.session.get('login_username', False)
    
    try:
        result = changePasswdCheck(loginUser, password, confirmPassword)
        return HttpResponse(json.dumps(result), content_type='application/json')
    except Exception as e:
        print(e)
        return render(request, 'error/error.html')

@csrf_exempt    
def addChangeUserInfo(request):
    '''
    新增用户
    修改用户
    '''
    v_userId = request.POST.get('user_id')
    v_userName = request.POST.get('user_name').strip()
    v_display = request.POST.get('display').strip()
    v_role = request.POST.get('role').strip()
    v_email = request.POST.get('email').strip()
    v_password = request.POST.get('password').strip()
    v_is_active = request.POST.get('is_active')
    v_is_staff = request.POST.get('is_staff')
    
    print(request.POST.get('is_active'))
    print(request.POST.get('is_staff'))
    
    
    if v_is_active == 'true':
        v_is_active = 1
    else:
        v_is_active = 0
        
    if v_is_staff == 'true':
        v_is_staff = 1
    else:
        v_is_staff = 0
    
    v_password = make_password(v_password)
        
    print(v_userId, v_userName, v_display, v_role, v_email, v_password, v_is_active, v_is_staff)
        
    if v_userId == '' or v_userId is None:
        # 新增
        try:   
            userObj = users(username=v_userName, display=v_display, role=v_role, email=v_email, password=v_password, is_active=v_is_active, is_staff=v_is_staff, is_superuser=0, first_name='', last_name='', date_joined= datetime.datetime.now())
            userObj.save()
            result = {'status':1, 'msg':'保存成功!', 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')
        except Exception as e:
            result = {'status':2, 'msg':'保存失败!'+str(e), 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')        
    else:
        # 修改
        try:
            userObj = users.objects.filter(id=v_userId)
            userObj.update(username=v_userName, display=v_display, role=v_role, email=v_email, is_active=v_is_active, is_staff=v_is_staff)
#             mainConfigObj.save()
            result = {'status':1, 'msg':'修改成功!', 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')
        except Exception as e:
            result = {'status':2, 'msg':'修改失败!'+str(e), 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')      

@csrf_exempt    
def delUser(request):
    v_userId = request.POST['userId']

    if v_userId == "" or v_userId is None:
        result = {'status':3, 'msg':'未选中任何记录!', 'data':''}
        return HttpResponse(json.dumps(result), content_type='application/json')
    else:    
        try:
            delResult = users.objects.filter(id=v_userId).delete()
            print(delResult)
            result = {'status':1, 'msg':'删除成功!', 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')            
        except Exception as e:
            print(e)
            result = {'status':2, 'msg':'删除失败!'+str(e), 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')
        
@csrf_exempt
def getUserDetailInfo(request):
    userId = request.POST['userId']
    
    try:
        userObj = users.objects.get(id=userId)
        userJson = userObj.toJSON()
        
        result = {'status':1, 'msg':'请求成功', 'obj':userJson}
        print(result)
        return HttpResponse(json.dumps(result), content_type='application/json')
    except Exception as e:
        print(e)
        result = {'status':2, 'msg':'请求失败!'+str(e), 'data':''}
        return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_exempt    
def resetUserPasswd(request):
    v_userId = request.POST['userId']

    if v_userId == "" or v_userId is None:
        result = {'status':3, 'msg':'未选中任何记录!', 'data':''}
        return HttpResponse(json.dumps(result), content_type='application/json')
    else:    
        try:
            userObj = users.objects.filter(id=v_userId)
            userObj.update(password=make_password('111111'))
            result = {'status':1, 'msg':'重置密码成功!', 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')            
        except Exception as e:
            print(e)
            result = {'status':2, 'msg':'重置密码失败!'+str(e), 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')
