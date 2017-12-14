import math

from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404
from cmdb.models import host, hostUser
from utils.pagination import getPageLimitOffset
from utils.logUtil import getLogger


logger = getLogger()

# Create your views here.
def getHostList(request):

    paginationList = getPageLimitOffset(request)
    search_keyword = paginationList.get('search_keyword')
    offset = paginationList.get('offset')
    limit = paginationList.get('limit')
    pageNo = paginationList.get('pageNo')
    PAGE_LIMIT = paginationList.get('PAGE_LIMIT')
   
    # 查询
    listHost = []
    listHostNum = 0
    pageNum = 0

    #服务器端参数验证
    if search_keyword == "":
        try:
            print("search_keyword is None:")
            listHost = host.objects.all().order_by('-createdTime')[offset:limit]
            listHostNum = host.objects.count()
            pageNum = math.ceil(listHostNum/PAGE_LIMIT)
        except Exception as e:
            print(e)
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)
    else:
        try:
            print("search_keyword is Not None:")
            listHost = host.objects.filter(Q(hostName__contains=search_keyword)|Q(intranetIpAddr__contains=search_keyword)|Q(publicIpAddr__contains=search_keyword)).order_by('-createdTime')[offset:limit]
            listHostNum = host.objects.filter(Q(hostName__contains=search_keyword)|Q(intranetIpAddr__contains=search_keyword)|Q(publicIpAddr__contains=search_keyword)).count()
            pageNum = math.ceil(listHostNum/PAGE_LIMIT)     
        except Exception as e:
            print(e)
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)

    
    context = {'listHost':listHost, 'listHostNum':listHostNum, 'pageNo':pageNo, 'pageNum':pageNum, 'PAGE_LIMIT':PAGE_LIMIT, "search_keyword":search_keyword}
    
    return render(request, 'cmdb/getHostList.html', context)

def addHostForm(request):
    return render(request, 'cmdb/addHost.html')

def addHostUserForm(request):
    return render(request, 'cmdb/addHostUser.html')

def getHostDetail(request, hostId):

    if hostId is not None and hostId != '': 
        try:
            hostObj = host.objects.get(id=hostId)
            hostUserList = hostObj.hostuser_set.all()
            context = {'hostObj':hostObj, 'hostUserList':hostUserList}
        except Exception as e:
            logger.error(str(e))
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)                

    return render(request, 'cmdb/hostDetail.html', context) 