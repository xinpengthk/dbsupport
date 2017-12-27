import math

from django.db.models.query_utils import Q
from django.shortcuts import render, get_object_or_404

from cmdb.models import host, dbInstance, dbGroup
from utils.logUtil import getLogger
from utils.pagination import getPageLimitOffset


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
            pageLeave = pageNum-pageNo
        except Exception as e:
            print(e)
            logger.error(str(e))
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)
    else:
        try:
            print("search_keyword is Not None:")
            listHost = host.objects.filter(Q(businessName__contains=search_keyword)|Q(serviceEnv__iexact=search_keyword)|Q(hostName__contains=search_keyword)|Q(intranetIpAddr__contains=search_keyword)|Q(publicIpAddr__contains=search_keyword)).order_by('-createdTime')[offset:limit]
            listHostNum = host.objects.filter(Q(businessName__contains=search_keyword)|Q(serviceEnv__iexact=search_keyword)|Q(hostName__contains=search_keyword)|Q(intranetIpAddr__contains=search_keyword)|Q(publicIpAddr__contains=search_keyword)).count()
            pageNum = math.ceil(listHostNum/PAGE_LIMIT)
            pageLeave = pageNum-pageNo
        except Exception as e:
            print(e)
            logger.error(str(e))
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)

    
    context = {'listHost':listHost, 'listHostNum':listHostNum, 'pageNo':pageNo, 'pageNum':pageNum, 'pageLeave':pageLeave, 'PAGE_LIMIT':PAGE_LIMIT, "search_keyword":search_keyword}
    
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

def getDbInstanceList(request):

    paginationList = getPageLimitOffset(request)
    search_keyword = paginationList.get('search_keyword')
    offset = paginationList.get('offset')
    limit = paginationList.get('limit')
    pageNo = paginationList.get('pageNo')
    PAGE_LIMIT = paginationList.get('PAGE_LIMIT')
   
    # 查询
    listInstance = []
    listInstanceNum = 0
    pageNum = 0

    #查询结果
    if search_keyword == "":
        try:
            print("search_keyword is None:")
            listInstance = dbInstance.objects.all().order_by('-createdTime')[offset:limit]
            listInstanceNum = dbInstance.objects.count()
            pageNum = math.ceil(listInstanceNum/PAGE_LIMIT)
            pageLeave = pageNum-pageNo
        except Exception as e:
            print(e)
            logger.error(str(e))
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)
    else:
        try:
            print("search_keyword is Not None:")
            listInstance = dbInstance.objects.filter(Q(host__contains=search_keyword)|Q(instanceType__iexact=search_keyword)|Q(groupName__contains=search_keyword)|Q(instanceName__contains=search_keyword)).order_by('-createdTime')[offset:limit]
            listInstanceNum = dbInstance.objects.filter(Q(host__contains=search_keyword)|Q(instanceType__iexact=search_keyword)|Q(groupName__contains=search_keyword)|Q(instanceName__contains=search_keyword)).count()
            pageNum = math.ceil(listInstanceNum/PAGE_LIMIT)
            pageLeave = pageNum-pageNo
        except Exception as e:
            print(e)
            logger.error(str(e))
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)

    context = {'listInstance':listInstance, 'listInstanceNum':listInstanceNum, 'pageNo':pageNo, 'pageNum':pageNum, 'pageLeave':pageLeave, 'PAGE_LIMIT':PAGE_LIMIT, "search_keyword":search_keyword}
    
    return render(request, 'cmdb/getDbInstanceList.html', context)

# def getDbClusterList(request):
# 
#     paginationList = getPageLimitOffset(request)
#     search_keyword = paginationList.get('search_keyword')
#     offset = paginationList.get('offset')
#     limit = paginationList.get('limit')
#     pageNo = paginationList.get('pageNo')
#     PAGE_LIMIT = paginationList.get('PAGE_LIMIT')
#    
#     # 查询
#     listDbCluster = []
#     listDbClusterNum = 0
#     pageNum = 0
# 
#     #查询结果
#     if search_keyword == "":
#         try:
#             print("search_keyword is None:")
#             listDbCluster = dbCluster.objects.all().order_by('-createdTime')[offset:limit]
#             listDbClusterNum = dbCluster.objects.count()
#             pageNum = math.ceil(listDbClusterNum/PAGE_LIMIT)
#             pageLeave = pageNum-pageNo
#         except Exception as e:
#             print(e)
#             logger.error(str(e))
#             context = {'errMsg': '内部错误！'}
#             return render(request, 'error/error.html', context)
#     else:
#         try:
#             print("search_keyword is Not None:")
#             listDbCluster = dbCluster.objects.filter(Q(clusterName__contains=search_keyword)|Q(clusterStatus__iexact=search_keyword)).order_by('-createdTime')[offset:limit]
#             listDbClusterNum = dbCluster.objects.filter(Q(clusterName__contains=search_keyword)|Q(clusterStatus__iexact=search_keyword)).count()
#             pageNum = math.ceil(listDbClusterNum/PAGE_LIMIT)
#             pageLeave = pageNum-pageNo
#         except Exception as e:
#             print(e)
#             logger.error(str(e))
#             context = {'errMsg': '内部错误！'}
#             return render(request, 'error/error.html', context)
# 
#     context = {'listDbCluster':listDbCluster, 'listDbClusterNum':listDbClusterNum, 'pageNo':pageNo, 'pageNum':pageNum, 'pageLeave':pageLeave, 'PAGE_LIMIT':PAGE_LIMIT, "search_keyword":search_keyword}
#     
#     return render(request, 'cmdb/getdbClusterList.html', context)
# 
# def addDbClusterForm(request):
#     return render(request, 'cmdb/addDbCluster.html')
# 
# def getDbClusterDetail(request, clusterId):
# 
#     if clusterId is not None and clusterId != '': 
#         try:
#             dbClusterObj = dbCluster.objects.get(id=clusterId)
#             dbGroupList = dbClusterObj.dbgroup_set.all()
#             context = {'dbClusterObj':dbClusterObj, 'dbGroupList':dbGroupList}
#         except Exception as e:
#             logger.error(str(e))
#             context = {'errMsg': '内部错误！'}
#             return render(request, 'error/error.html', context)                
# 
#     return render(request, 'cmdb/dbClusterDetail.html', context) 

def getDbGroupList(request):

    paginationList = getPageLimitOffset(request)
    search_keyword = paginationList.get('search_keyword')
    offset = paginationList.get('offset')
    limit = paginationList.get('limit')
    pageNo = paginationList.get('pageNo')
    PAGE_LIMIT = paginationList.get('PAGE_LIMIT')
   
    # 查询
    listDbGroup = []
    listDbGroupNum = 0
    pageNum = 0

    #查询结果
    if search_keyword == "":
        try:
            print("search_keyword is None:")
            listDbGroup = dbGroup.objects.all().order_by('-createdTime')[offset:limit]
            listDbGroupNum = dbGroup.objects.count()
            pageNum = math.ceil(listDbGroupNum/PAGE_LIMIT)
            pageLeave = pageNum-pageNo
        except Exception as e:
            print(e)
            logger.error(str(e))
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)
    else:
        try:
            print("search_keyword is Not None:")
            listDbGroup = dbGroup.objects.filter(Q(groupEnv__iexact=search_keyword)|Q(clusterName__contains=search_keyword)|Q(groupName__contains=search_keyword)|Q(groupStatus__iexact=search_keyword)).order_by('-createdTime')[offset:limit]
            listDbGroupNum = dbGroup.objects.filter(Q(groupEnv__iexact=search_keyword)|Q(clusterName__contains=search_keyword)|Q(groupName__contains=search_keyword)|Q(groupStatus__iexact=search_keyword)).count()
            pageNum = math.ceil(listDbGroupNum/PAGE_LIMIT)
            pageLeave = pageNum-pageNo
        except Exception as e:
            print(e)
            logger.error(str(e))
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)

    context = {'listDbGroup':listDbGroup, 'listDbGroupNum':listDbGroupNum, 'pageNo':pageNo, 'pageNum':pageNum, 'pageLeave':pageLeave, 'PAGE_LIMIT':PAGE_LIMIT, "search_keyword":search_keyword}
    
    return render(request, 'cmdb/getdbGroupList.html', context)

def addDbGroupForm(request):
    return render(request, 'cmdb/addDbGroup.html')

def getInstanceDetail(request, groupId):

    print("get instance begin: groupid is ", groupId)
    if groupId is not None and groupId != '': 
        try:
            dbGroupObj = dbGroup.objects.get(id=groupId)
            dbInstanceList = dbGroupObj.dbinstance_set.all().order_by('instanceName')
            context = {'dbGroupObj':dbGroupObj, 'dbInstanceList':dbInstanceList}
        except Exception as e:
            print(e)
            logger.error(str(e))
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)                

    return render(request, 'cmdb/getDbInstanceList.html', context) 

def addDbInstanceForm(request, groupId):
    if groupId is not None and groupId != '': 
        try:
            dbGroupObj = dbGroup.objects.get(id=groupId)
            print(11111, dbGroupObj.businessName, dbGroupObj.groupEnv)
            listHost = host.objects.filter(businessName=dbGroupObj.businessName.strip(), serviceEnv=dbGroupObj.groupEnv.strip(), hostType__in = ['DB', 'REDIS'])
            if len(listHost) >= 1:
                context = {'dbGroupObj':dbGroupObj, 'listHost':listHost}
            else:
                context = {'errMsg': '没有匹配'+dbGroupObj.businessName+'业务线下的'+dbGroupObj.groupEnv+'环境下的DB 或者 REDIS 主机，请添加主机！'}
                return render(request, 'error/error.html', context)                    
        except Exception as e:
            print(e)
            logger.error(str(e))
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)                
    
    return render(request, 'cmdb/addDbInstance.html', context)

def changDbInstanceForm(request):            
    return render(request, 'cmdb/addDbInstance.html')
