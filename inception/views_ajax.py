# -*- coding: UTF-8 -*- 

import json

from django.db.models.query_utils import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

from .const import Const
from .dao import Dao
from .inception import InceptionDao
from .models import main_config, sql_order


dao = Dao()
inceptionDao = InceptionDao()
login_failure_counter = {} #登录失败锁定计数器，给loginAuthenticate用的
sqlSHA1_cache = {} #存储SQL文本与SHA1值的对应关系，尽量减少与数据库的交互次数,提高效率。格式: {工单ID1:{SQL内容1:sqlSHA1值1, SQL内容2:sqlSHA1值2},}

#提交SQL给inception进行自动审核
@csrf_exempt
def simplecheck(request):
    if request.is_ajax():
        sqlContent = request.POST.get('sql_content')
        clusterName = request.POST.get('cluster_name')
    else:
        sqlContent = request.POST['sql_content']
        clusterName = request.POST['cluster_name']
     
    finalResult = {'status':0, 'msg':'ok', 'data':[]}
    #服务器端参数验证
    if sqlContent is None or clusterName is None:
        finalResult['status'] = 1
        finalResult['msg'] = '页面提交参数可能为空'
        return HttpResponse(json.dumps(finalResult), content_type='application/json')

    sqlContent = sqlContent.rstrip()
    if sqlContent[-1] != ";":
        finalResult['status'] = 1
        finalResult['msg'] = 'SQL语句结尾没有以;结尾，请重新修改并提交！'
        return HttpResponse(json.dumps(finalResult), content_type='application/json')
    #交给inception进行自动审核
    result = inceptionDao.sqlautoReview(sqlContent, clusterName)
    if result is None or len(result) == 0:
        finalResult['status'] = 1
        finalResult['msg'] = 'inception返回的结果集为空！可能是SQL语句有语法错误'
        return HttpResponse(json.dumps(finalResult), content_type='application/json')
    #要把result转成JSON存进数据库里，方便SQL单子详细信息展示
    finalResult['data'] = result
    return HttpResponse(json.dumps(finalResult), content_type='application/json')


#请求图表数据
@csrf_exempt
def getMonthCharts(request):
    result = dao.getWorkChartsByMonth()
    return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_exempt
def getPersonCharts(request):
    result = dao.getWorkChartsByPerson()
    return HttpResponse(json.dumps(result), content_type='application/json')

def getSqlSHA1(workflowId):
    """调用django ORM从数据库里查出review_content，从其中获取sqlSHA1值"""
    workflowDetail = get_object_or_404(sql_order, pk=workflowId)
    dictSHA1 = {}
    # 使用json.loads方法，把review_content从str转成list,
    listReCheckResult = json.loads(workflowDetail.review_content)

    for rownum in range(len(listReCheckResult)):
        id = rownum + 1
        sqlSHA1 = listReCheckResult[rownum][10]
        if sqlSHA1 != '':
            dictSHA1[id] = sqlSHA1

    if dictSHA1 != {}:
        # 如果找到有sqlSHA1值，说明是通过pt-OSC操作的，将其放入缓存。
        # 因为使用OSC执行的SQL占较少数，所以不设置缓存过期时间
        sqlSHA1_cache[workflowId] = dictSHA1
    return dictSHA1

@csrf_exempt
def getOscPercent(request):
    """获取该SQL的pt-OSC执行进度和剩余时间"""
    workflowId = request.POST['workflowid']
    sqlID = request.POST['sqlID']
    if workflowId == '' or workflowId is None or sqlID == '' or sqlID is None:
        context = {"status":-1 ,'msg': 'workflowId或sqlID参数为空.', "data":""}
        return HttpResponse(json.dumps(context), content_type='application/json')

    workflowId = int(workflowId)
    sqlID = int(sqlID)
    dictSHA1 = {}
    if workflowId in sqlSHA1_cache:
        dictSHA1 = sqlSHA1_cache[workflowId]
        # cachehit = "已命中"
    else:
        dictSHA1 = getSqlSHA1(workflowId)

    if dictSHA1 != {} and sqlID in dictSHA1:
        sqlSHA1 = dictSHA1[sqlID]
        result = inceptionDao.getOscPercent(sqlSHA1)  #成功获取到SHA1值，去inception里面查询进度
        if result["status"] == 0:
            # 获取到进度值
            pctResult = result
        else:
            # result["status"] == 1, 未获取到进度值,需要与workflow.execute_result对比，来判断是已经执行过了，还是还未执行
            execute_result = sql_order.objects.get(id=workflowId).execute_result
            try:
                listExecResult = json.loads(execute_result)
            except ValueError:
                listExecResult = execute_result
            if type(listExecResult) == list and len(listExecResult) >= sqlID-1:
                if dictSHA1[sqlID] in listExecResult[sqlID-1][10]:
                    # 已经执行完毕，进度值置为100
                    pctResult = {"status":0, "msg":"ok", "data":{"percent":100, "timeRemained":""}}
            else:
                # 可能因为前一条SQL是DML，正在执行中；或者还没执行到这一行。但是status返回的是4，而当前SQL实际上还未开始执行。这里建议前端进行重试
                pctResult = {"status":-3, "msg":"进度未知", "data":{"percent":-100, "timeRemained":""}}
    elif dictSHA1 != {} and sqlID not in dictSHA1:
        pctResult = {"status":4, "msg":"该行SQL不是由pt-OSC执行的", "data":""}
    else:
        pctResult = {"status":-2, "msg":"整个工单不由pt-OSC执行", "data":""}
    return HttpResponse(json.dumps(pctResult), content_type='application/json')

@csrf_exempt
def getWorkflowStatus(request):
    """获取某个工单的当前状态"""
    workflowId = request.POST['workflowid']
    if workflowId == '' or workflowId is None :
        context = {"status":-1 ,'msg': 'workflowId参数为空.', "data":""}
        return HttpResponse(json.dumps(context), content_type='application/json')

    workflowId = int(workflowId)
    workflowDetail = get_object_or_404(sql_order, pk=workflowId)
    workflowStatus = workflowDetail.status
    result = {"status":workflowStatus, "msg":"", "data":""}
    return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_exempt
def stopOscProgress(request):
    """中止该SQL的pt-OSC进程"""
    workflowId = request.POST['workflowid']
    sqlID = request.POST['sqlID']
    if workflowId == '' or workflowId is None or sqlID == '' or sqlID is None:
        context = {"status":-1 ,'msg': 'workflowId或sqlID参数为空.', "data":""}
        return HttpResponse(json.dumps(context), content_type='application/json')

    loginUser = request.session.get('login_username', False)
    workflowDetail = sql_order.objects.get(id=workflowId)
    try:
        listAllReviewMen = json.loads(workflowDetail.review_man)
    except ValueError:
        listAllReviewMen = (workflowDetail.review_man, )
    #服务器端二次验证，当前工单状态必须为等待人工审核,正在执行人工审核动作的当前登录用户必须为审核人. 避免攻击或被接口测试工具强行绕过
    if workflowDetail.status != Const.workflowStatus['executing']:
        context = {"status":-1, "msg":'当前工单状态不是"执行中"，请刷新当前页面！', "data":""}
        return HttpResponse(json.dumps(context), content_type='application/json')
    if loginUser is None or loginUser not in listAllReviewMen:
        context = {"status":-1 ,'msg': '当前登录用户不是审核人，请重新登录.', "data":""}
        return HttpResponse(json.dumps(context), content_type='application/json')

    workflowId = int(workflowId)
    sqlID = int(sqlID)
    if workflowId in sqlSHA1_cache:
        dictSHA1 = sqlSHA1_cache[workflowId]
    else:
        dictSHA1 = getSqlSHA1(workflowId)
    if dictSHA1 != {} and sqlID in dictSHA1:
        sqlSHA1 = dictSHA1[sqlID]
        optResult = inceptionDao.stopOscProgress(sqlSHA1)
    else:
        optResult = {"status":4, "msg":"不是由pt-OSC执行的", "data":""}
    return HttpResponse(json.dumps(optResult), content_type='application/json')

@csrf_exempt
def addMainConfig(request):
    clusterId = request.POST['cluster_id']
    clusterName = request.POST['cluster_name']
    mainHost = request.POST['main_host']
    mainPort = request.POST['main_port']
    mainUser = request.POST['main_user']
    mainPassword = request.POST['main_password']
    
    if clusterId == "" or clusterId is None:
        # 新增
        try:        
            mainConfigObj = main_config(cluster_name=clusterName, main_host=mainHost, main_port=mainPort, main_user=mainUser, main_password=mainPassword)
            mainConfigObj.save()
            result = {'status':1, 'msg':'保存成功!', 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')
        except Exception as e:
            print(e)
            result = {'status':2, 'msg':'保存失败!'+str(e), 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        # 修改
        try:        
            mainConfigObj = main_config.objects.filter(id=clusterId)
            mainConfigObj.update(cluster_name=clusterName, main_host=mainHost, main_port=mainPort, main_user=mainUser, main_password=mainPassword)
#             mainConfigObj.save()
            result = {'status':1, 'msg':'修改成功!', 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')
        except Exception as e:
            print(e)
            result = {'status':2, 'msg':'修改失败!'+str(e), 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')        

@csrf_exempt
def delMainConfig(request):
    clusterId = request.POST['mainConfigId']
    
    if clusterId == "" or clusterId is None:
        result = {'status':3, 'msg':'未选中任何记录!', 'data':''}
        return HttpResponse(json.dumps(result), content_type='application/json')
    else:
        try:
            delResult = main_config.objects.filter(id=clusterId).delete()
            print(delResult)
            result = {'status':1, 'msg':'删除成功!', 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')            
        except Exception as e:
            print(e)
            result = {'status':2, 'msg':'删除失败!'+str(e), 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')                

@csrf_exempt    
def delsqlOrder(request):
    sqlOrderId = request.POST['sqlOrderId']

    if sqlOrderId == "" or sqlOrderId is None:
        result = {'status':3, 'msg':'未选中任何记录!', 'data':''}
        return HttpResponse(json.dumps(result), content_type='application/json')
    else:    
        try:
            delResult = sql_order.objects.filter(id=sqlOrderId).delete()
            print(delResult)
            result = {'status':1, 'msg':'删除成功!', 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')            
        except Exception as e:
            print(e)
            result = {'status':2, 'msg':'删除失败!'+str(e), 'data':''}
            return HttpResponse(json.dumps(result), content_type='application/json')

@csrf_exempt
def getMainConfigDetailInfo(request):
    configId = request.POST['configId']
    
    try:
        mainConfigObj = main_config.objects.get(id=configId)
        mainConfigJson = mainConfigObj.toJSON()
        
        result = {'status':1, 'msg':'请求成功', 'obj':mainConfigJson}
        print(result)
        return HttpResponse(json.dumps(result), content_type='application/json')
    except Exception as e:
        print(e)
        result = {'status':2, 'msg':'请求失败!'+str(e), 'data':''}
        return HttpResponse(json.dumps(result), content_type='application/json')
            