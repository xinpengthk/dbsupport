# -*- coding: UTF-8 -*- 

import math

from django.db.models.query_utils import Q
from django.shortcuts import render

from user.models import users


# from .aes_decryptor import Prpcrypt
# from .const import Const
# from .dao import Dao
# from .inception import InceptionDao
# from .models import users, master_config, workflow
# from .sendmail import MailSender
def login(request):
    return render(request, 'user/login.html')

def logout(request):
    if request.session.get('login_username', False):
        del request.session['login_username']
    return render(request, 'user/login.html')

def loginSuccessful(request):
    return render(request, 'base/main.html')

def changePasswd(request):
    return render(request, 'user/changePasswd.html')


def getUserList(request):

    search_keyword = request.GET.get('search_keyword')

    if search_keyword is None:
        search_keyword = ''
    
    search_keyword = search_keyword.strip()

    print("search_keyword:",search_keyword)

    PAGE_LIMIT = 15

    #参数检查
    if 'pageNo' in request.GET:
        pageNo = request.GET['pageNo']
    else:
        pageNo = '0'
        
    if not isinstance(pageNo, str):
        raise TypeError('pageNo页面传入参数不对')
    else:
        try:
            pageNo = int(pageNo)
            if pageNo < 0:
                pageNo = 0
        except ValueError as ve:
            print(ve)
            context = {'errMsg': 'pageNo参数不是int.'}
            return render(request, 'error/error.html', context)

    offset = pageNo * PAGE_LIMIT
    limit = offset + PAGE_LIMIT
   
    # 查询
    listUser = []
    listUserNum = 0
    pageNum = 0

    #服务器端参数验证
    if search_keyword == "":
        try:
            print("search_keyword is None:")
            listUser = users.objects.all().order_by('-date_joined')[offset:limit]
            listUserNum = users.objects.count()
            pageNum = math.ceil(listUserNum/PAGE_LIMIT)
        except Exception as e:
            print(e)
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)
    else:
        try:
            print("search_keyword is Not None:")
            listUser = users.objects.filter(Q(display__contains=search_keyword)|Q(role__contains=search_keyword)).order_by('-date_joined')[offset:limit]
            listUserNum = users.objects.filter(Q(display__contains=search_keyword)|Q(role__contains=search_keyword)).count()
            pageNum = math.ceil(listUserNum/PAGE_LIMIT)     
        except Exception as e:
            print(e)
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)

    
    context = {'listUser':listUser, 'listUserNum':listUserNum, 'pageNo':pageNo, 'pageNum':pageNum, 'PAGE_LIMIT':PAGE_LIMIT, "search_keyword":search_keyword}
    
    return render(request, 'user/getUserList.html', context)

def addUser(request):
    return render(request, 'user/addUserInfo.html')