# -*- coding: UTF-8 -*- 

from collections import OrderedDict
import json
import math
import re
import time

from django.conf import settings
from django.db import connection
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from inception.const import Const
from inception.dao import Dao
from inception.inception import InceptionDao
from inception.models import sql_order, main_config
from user.models import users
from utils.pagination import getPageLimitOffset
from utils.sendmail import MailSender


# from utils.aesDecryptor import Prpcrypt
# from .aes_decryptor import Prpcrypt
# from .const import Const
# from .dao import Dao
# from .inception import InceptionDao
# from .models import users, main_config, workflow
# from .sendmail import MailSender
dao = Dao()
inceptionDao = InceptionDao()
mailSender = MailSender()
# prpCryptor = Prpcrypt()

#首页，也是查看所有SQL工单页面，具备翻页功能
def allworkflow(request):

    #一个页面展示
    PAGE_LIMIT = 15

    pageNo = 0
    navStatus = ''

    #参数检查
    if 'pageNo' in request.GET:
        pageNo = request.GET['pageNo']
    else:
        pageNo = '0'
    
    if 'navStatus' in request.GET:
        navStatus = request.GET['navStatus']
    else:
        navStatus = 'all'
    if not isinstance(pageNo, str) or not isinstance(navStatus, str):
        raise TypeError('pageNo或navStatus页面传入参数不对')
    else:
        try:
            pageNo = int(pageNo)
            if pageNo < 0:
                pageNo = 0
        except ValueError as ve:
            print(ve)
            context = {'errMsg': 'pageNo参数不是int.'}
            return render(request, 'error/error.html', context)

    loginUser = request.session.get('login_username', False)
    #查询workflow model，根据pageNo和navStatus获取对应的内容
    offset = pageNo * PAGE_LIMIT
    limit = offset + PAGE_LIMIT

    #修改全部工单、审核不通过、已执行完毕界面工程师只能看到自己发起的工单，审核人可以看到全部
    listWorkflow = []
    listWorkflowNum = 0
    #查询全部流程
    loginUserOb = users.objects.get(username=loginUser)
    role = loginUserOb.role
    if navStatus == 'all' and role == '审核人':
        #这句话等同于select * from sql_workflow order by create_time desc limit {offset, limit};
        listWorkflow = sql_order.objects.exclude(status=Const.workflowStatus['autoreviewwrong']).order_by('-create_time')[offset:limit]
        listWorkflowNum = sql_order.objects.exclude(status=Const.workflowStatus['autoreviewwrong']).count()
    elif navStatus == 'all' and role == '工程师':
        listWorkflow = sql_order.objects.filter(Q(engineer=loginUser) | Q(status=Const.workflowStatus['autoreviewwrong']), engineer=loginUser).order_by('-create_time')[offset:limit]
        listWorkflowNum = sql_order.objects.filter(Q(engineer=loginUser) | Q(status=Const.workflowStatus['autoreviewwrong']), engineer=loginUser).count()
    elif navStatus == 'waitingforme':
        listWorkflow = sql_order.objects.filter(Q(status=Const.workflowStatus['manreviewing'], review_man=loginUser) | Q(status=Const.workflowStatus['manreviewing'], review_man__contains='"' + loginUser + '"')).order_by('-create_time')[offset:limit]
        listWorkflowNum = sql_order.objects.filter(Q(status=Const.workflowStatus['manreviewing'], review_man=loginUser) | Q(status=Const.workflowStatus['manreviewing'], review_man__contains='"' + loginUser + '"')).count()
    elif navStatus == 'finish' and role == '审核人':
        listWorkflow = sql_order.objects.filter(status=Const.workflowStatus['finish']).order_by('-create_time')[offset:limit]
        listWorkflowNum = sql_order.objects.filter(status=Const.workflowStatus['finish']).count()
    elif navStatus == 'finish' and role == '工程师':
        listWorkflow = sql_order.objects.filter(status=Const.workflowStatus['finish'], engineer=loginUser).order_by('-create_time')[offset:limit]
        listWorkflowNum = sql_order.objects.filter(status=Const.workflowStatus['finish'], engineer=loginUser).count()
    elif navStatus == 'executing' and role == '审核人':
        listWorkflow = sql_order.objects.filter(status=Const.workflowStatus['executing']).order_by('-create_time')[offset:limit]
        listWorkflowNum = sql_order.objects.filter(status=Const.workflowStatus['executing']).count()
    elif navStatus == 'executing' and role == '工程师':
        listWorkflow = sql_order.objects.filter(status=Const.workflowStatus['executing'], engineer=loginUser).order_by('-create_time')[offset:limit]
        listWorkflowNum = sql_order.objects.filter(status=Const.workflowStatus['executing'], engineer=loginUser).count()
    elif navStatus == 'abort' and role == '审核人':
        listWorkflow = sql_order.objects.filter(status=Const.workflowStatus['abort']).order_by('-create_time')[offset:limit]
        listWorkflowNum = sql_order.objects.filter(status=Const.workflowStatus['abort']).count()
    elif navStatus == 'abort' and role == '工程师':
        listWorkflow = sql_order.objects.filter(status=Const.workflowStatus['abort'], engineer=loginUser).order_by('-create_time')[offset:limit]
        listWorkflowNum = sql_order.objects.filter(status=Const.workflowStatus['abort'], engineer=loginUser).count()
    elif navStatus == 'autoreviewwrong' and role == '审核人':
        listWorkflow = sql_order.objects.filter(status=Const.workflowStatus['autoreviewwrong']).order_by('-create_time')[offset:limit]
        listWorkflowNum = sql_order.objects.filter(status=Const.workflowStatus['autoreviewwrong']).count()
    elif navStatus == 'autoreviewwrong' and role == '工程师':
        listWorkflow = sql_order.objects.filter(status=Const.workflowStatus['autoreviewwrong'], engineer=loginUser).order_by('-create_time')[offset:limit]
        listWorkflowNum = sql_order.objects.filter(status=Const.workflowStatus['autoreviewwrong'], engineer=loginUser).count()
    else:
        context = {'errMsg': '传入的navStatus参数有误！'}
        return render(request, 'error/error.html', context)


    context = {'currentMenu':'allworkflow', 'listWorkflow':listWorkflow, 'listWorkflowNum':listWorkflowNum, 'pageNo':pageNo, 'navStatus':navStatus, 'PAGE_LIMIT':PAGE_LIMIT, 'role':role}
    
    return render(request, 'inception/allWorkflow.html', context)

def getWorkOrderList(request):  
    # 为前端用户提供
    
#     search_keyword = request.GET.get('search_keyword')
# 
#     if search_keyword is None:
#         search_keyword = ''
#     
#     search_keyword = search_keyword.strip()
# 
#     print("search_keyword:",search_keyword)
#         
#     #一个页面展示
#     PAGE_LIMIT = 15
#     pageNo = 0
# 
#     #参数检查
#     if 'pageNo' in request.GET:
#         pageNo = request.GET['pageNo']
#     else:
#         pageNo = '0'
#     
#     if not isinstance(pageNo, str):
#         raise TypeError('pageNo或navStatus页面传入参数不对')
#     else:
#         try:
#             pageNo = int(pageNo)
#             if pageNo < 0:
#                 pageNo = 0
#         except ValueError as ve:
#             print(ve)
#             context = {'errMsg': 'pageNo参数不是int.'+str(ve)}
#             return render(request, 'error/error.html', context)
# 
#     loginUser = request.session.get('login_username', False)
#     #查询workflow model，根据pageNo和navStatus获取对应的内容
#     offset = pageNo * PAGE_LIMIT
#     limit = offset + PAGE_LIMIT

    paginationList = getPageLimitOffset(request)
    search_keyword = paginationList.get('search_keyword')
    offset = paginationList.get('offset')
    limit = paginationList.get('limit')
    pageNo = paginationList.get('pageNo')
    PAGE_LIMIT = paginationList.get('PAGE_LIMIT')
    
    loginUser = request.session.get('login_username', False)

    #修改全部工单、审核不通过、已执行完毕界面工程师只能看到自己发起的工单，审核人可以看到全部
    listWorkflow = []
    listWorkflowNum = 0
    #查询全部流程
    loginUserOb = users.objects.get(username=loginUser)
    role = loginUserOb.role
    

    if search_keyword == "":
        if role == '审核人':
            listWorkflow = sql_order.objects.all().order_by('-create_time')[offset:limit]
            listWorkflowNum = sql_order.objects.all().count()
        elif role == '工程师':
            listWorkflow = sql_order.objects.filter(engineer=loginUser).order_by('-create_time')[offset:limit]
            listWorkflowNum = sql_order.objects.filter(engineer=loginUser).count() 
            print("listWorkflow Type:", type(listWorkflow))     
    else:
        if role == '审核人':
            listWorkflow = sql_order.objects.filter(Q(workflow_name__contains=search_keyword)|Q(sql_content__contains=search_keyword)|Q(status__contains=search_keyword)).order_by('-create_time')[offset:limit]
            listWorkflowNum = sql_order.objects.filter(Q(workflow_name__contains=search_keyword)|Q(sql_content__contains=search_keyword)|Q(status__contains=search_keyword)).count()
        elif role == '工程师':
            listWorkflow = sql_order.objects.filter(Q(workflow_name__contains=search_keyword)|Q(sql_content__contains=search_keyword)|Q(status__contains=search_keyword), engineer=loginUser).order_by('-create_time')[offset:limit]
            listWorkflowNum = sql_order.objects.filter(Q(workflow_name__contains=search_keyword)|Q(sql_content__contains=search_keyword)|Q(status__contains=search_keyword), engineer=loginUser).count()
      
            print('listWorkflow:', listWorkflow)
            print("listWorkflowNum:", listWorkflowNum)
            
    context = {'currentMenu':'allworkflow', 'listWorkflow':listWorkflow, 'listWorkflowNum':listWorkflowNum, 'pageNo':pageNo, 'search_keyword':search_keyword, 'PAGE_LIMIT':PAGE_LIMIT, 'role':role}
    
    return render(request, 'inception/allWorkflow.html', context)

#提交SQL的页面
def submitSql(request):
    mains = main_config.objects.all().order_by('cluster_name')
    if len(mains) == 0:
        context = {'errMsg': '集群数为0，可能后端数据没有配置集群'}
        return render(request, 'error/error.html', context) 
    
    #获取所有集群名称
    listAllClusterName = [main.cluster_name for main in mains]

    dictAllClusterDb = OrderedDict()
    #每一个都首先获取主库地址在哪里
    for clusterName in listAllClusterName:
        listMains = main_config.objects.filter(cluster_name=clusterName)
        if len(listMains) != 1:
            context = {'errMsg': '存在两个集群名称一样的集群，请修改数据库'}
            return render(request, 'error/error.html', context)
        #取出该集群的名称以及连接方式，为了后面连进去获取所有databases
        mainHost = listMains[0].main_host
        mainPort = listMains[0].main_port
        mainUser = listMains[0].main_user
#         mainPassword = prpCryptor.decrypt(listMains[0].main_password)
        mainPassword = listMains[0].main_password

        listDb = dao.getAlldbByCluster(mainHost, mainPort, mainUser, mainPassword)
        dictAllClusterDb[clusterName] = listDb

    #获取所有审核人，当前登录用户不可以审核
    loginUser = request.session.get('login_username', False)
    reviewMen = users.objects.filter(role='审核人').exclude(username=loginUser)
#    listAllReviewMen = [user.display for user in reviewMen]
    if len(reviewMen) == 0:
        context = {'errMsg': '审核人为0，请配置审核人'}
        return render(request, 'error/error.html', context) 
    listAllReviewMen = [user.username for user in reviewMen]
  
    context = {'currentMenu':'submitsql', 'dictAllClusterDb':dictAllClusterDb, 'reviewMen':reviewMen}
    return render(request, 'inception/submitSql.html', context)

#提交SQL给inception进行解析
def autoreview(request):
    workflowid = request.POST.get('workflowid')
    sqlContent = request.POST['sql_content']
    workflowName = request.POST['workflow_name']
    clusterName = request.POST['cluster_name']
    isBackup = request.POST['is_backup']
    reviewMan = request.POST['review_man']
    subReviewMen = request.POST.get('sub_review_man', '')
    listAllReviewMen = (reviewMan, subReviewMen)
   
    #服务器端参数验证
    if sqlContent is None or workflowName is None or clusterName is None or isBackup is None or reviewMan is None:
        context = {'errMsg': '页面提交参数可能为空'}
        return render(request, 'error/error.html', context)
    sqlContent = sqlContent.rstrip()
    if sqlContent[-1] != ";":
        context = {'errMsg': "SQL语句结尾没有以;结尾，请后退重新修改并提交！"}
        return render(request, 'error/error.html', context)
 
    #交给inception进行自动审核
    result = inceptionDao.sqlautoReview(sqlContent, clusterName)
    if result is None or len(result) == 0:
        context = {'errMsg': 'inception返回的结果集为空！可能是SQL语句有语法错误'}
        return render(request, 'error/error.html', context)
    #要把result转成JSON存进数据库里，方便SQL单子详细信息展示
    jsonResult = json.dumps(result)

    #遍历result，看是否有任何自动审核不通过的地方，一旦有，则为自动审核不通过；没有的话，则为等待人工审核状态
    workflowStatus = Const.workflowStatus['manreviewing']
    for row in result:
        if row[2] == 2:
            #状态为2表示严重错误，必须修改
            workflowStatus = Const.workflowStatus['autoreviewwrong']
            break
        elif re.match(r"\w*comments\w*", row[4]):
            workflowStatus = Const.workflowStatus['autoreviewwrong']
            break

    #存进数据库里
    engineer = request.session.get('login_username', False)
    if not workflowid:
        Workflow = sql_order()
        Workflow.create_time = getNow()
    else:
        Workflow = sql_order.objects.get(id=int(workflowid))
    Workflow.workflow_name = workflowName
    Workflow.engineer = engineer
    Workflow.review_man = json.dumps(listAllReviewMen, ensure_ascii=False)
    Workflow.status = workflowStatus
    Workflow.is_backup = isBackup
    Workflow.review_content = jsonResult
    Workflow.cluster_name = clusterName
    Workflow.sql_content = sqlContent
    Workflow.execute_result = ''
    Workflow.save()
    workflowId = Workflow.id

    #自动审核通过了，才发邮件
    if workflowStatus == Const.workflowStatus['manreviewing']:
        #如果进入等待人工审核状态了，则根据settings.py里的配置决定是否给审核人发一封邮件提醒.
        if hasattr(settings, 'MAIL_ON_OFF') == True:
            if getattr(settings, 'MAIL_ON_OFF') == "on":
                url = _getDetailUrl(request) + str(workflowId) + '/'

                #发一封邮件
                strTitle = "新的SQL上线工单提醒 # " + str(workflowId)
                objEngineer = users.objects.get(username=engineer)
                for reviewMan in listAllReviewMen:
                    if reviewMan == "":
                        continue
                    strContent = "发起人：" + engineer + "\n审核人：" + str(listAllReviewMen)  + "\n工单地址：" + url + "\n工单名称： " + workflowName + "\n具体SQL：" + sqlContent
                    objReviewMan = users.objects.get(username=reviewMan)
                    mailSender.sendEmail(strTitle, strContent, [objReviewMan.email])
            else:
                #不发邮件
                pass
    
    return HttpResponseRedirect('/inception/detail/' + str(workflowId) + '/')
 

#展示SQL工单详细内容，以及可以人工审核，审核通过即可执行
def detail(request, workflowId):
    workflowDetail = get_object_or_404(sql_order, pk=workflowId)
    if workflowDetail.status in (Const.workflowStatus['finish'], Const.workflowStatus['exception']):
        listContent = json.loads(workflowDetail.execute_result)
    else:
        listContent = json.loads(workflowDetail.review_content)
    try:
        listAllReviewMen = json.loads(workflowDetail.review_man)
    except ValueError:
        listAllReviewMen = (workflowDetail.review_man, )

    # 格式化detail界面sql语句和审核/执行结果 by 搬砖工
    for Content in listContent:
        Content[4] = Content[4].split('\n')     # 审核/执行结果
        Content[5] = Content[5].split('\r\n')   # sql语句
    context = {'currentMenu':'allworkflow', 'workflowDetail':workflowDetail, 'listContent':listContent,'listAllReviewMen':listAllReviewMen}
    return render(request, 'inception/workOrderDetail.html', context)

#人工审核也通过，执行SQL
def execute(request):
    workflowId = request.POST['workflowid']
    if workflowId == '' or workflowId is None:
        context = {'errMsg': 'workflowId参数为空.'}
        return render(request, 'error/error.html', context)
    
    workflowId = int(workflowId)
    workflowDetail = sql_order.objects.get(id=workflowId)
    clusterName = workflowDetail.cluster_name
    try:
        listAllReviewMen = json.loads(workflowDetail.review_man)
    except ValueError:
        listAllReviewMen = (workflowDetail.review_man, )

    #服务器端二次验证，正在执行人工审核动作的当前登录用户必须为审核人. 避免攻击或被接口测试工具强行绕过
    loginUser = request.session.get('login_username', False)
    if loginUser is None or loginUser not in listAllReviewMen:
        context = {'errMsg': '当前登录用户不是审核人，请重新登录.'}
        return render(request, 'error/error.html', context)

    #服务器端二次验证，当前工单状态必须为等待人工审核
    if workflowDetail.status != Const.workflowStatus['manreviewing']:
        context = {'errMsg': '当前工单状态不是等待人工审核中，请刷新当前页面！'}
        return render(request, 'error/error.html', context)

    dictConn = getMainConnStr(clusterName)

    #将流程状态修改为执行中，并更新reviewok_time字段
    workflowDetail.status = Const.workflowStatus['executing']
    workflowDetail.reviewok_time = getNow()
    #执行之前重新split并check一遍，更新SHA1缓存；因为如果在执行中，其他进程去做这一步操作的话，会导致inception core dump挂掉
    splitReviewResult = inceptionDao.sqlautoReview(workflowDetail.sql_content, workflowDetail.cluster_name, isSplit='yes')
    workflowDetail.review_content = json.dumps(splitReviewResult)
    workflowDetail.save()

    #交给inception先split，再执行
    (finalStatus, finalList) = inceptionDao.executeFinal(workflowDetail, dictConn)

    #封装成JSON格式存进数据库字段里
    strJsonResult = json.dumps(finalList)
    workflowDetail.execute_result = strJsonResult
    workflowDetail.finish_time = getNow()
    workflowDetail.status = finalStatus
    workflowDetail.save()

    #如果执行完毕了，则根据settings.py里的配置决定是否给提交者和DBA一封邮件提醒.DBA需要知晓审核并执行过的单子
    if hasattr(settings, 'MAIL_ON_OFF') == True:
        if getattr(settings, 'MAIL_ON_OFF') == "on":
            url = _getDetailUrl(request) + str(workflowId) + '/'

            #给主、副审核人，申请人，DBA各发一封邮件
            engineer = workflowDetail.engineer
            reviewMen = workflowDetail.review_man
            workflowStatus = workflowDetail.status
            workflowName = workflowDetail.workflow_name
            objEngineer = users.objects.get(username=engineer)
            strTitle = "SQL上线工单执行完毕 # " + str(workflowId)
            strContent = "发起人：" + engineer + "\n审核人：" + reviewMen + "\n工单地址：" + url + "\n工单名称： " + workflowName +"\n执行结果：" + workflowStatus
            mailSender.sendEmail(strTitle, strContent, [objEngineer.email])
            mailSender.sendEmail(strTitle, strContent, getattr(settings, 'MAIL_REVIEW_DBA_ADDR'))
            for reviewMan in listAllReviewMen:
                if reviewMan == "":
                    continue
                objReviewMan = users.objects.get(username=reviewMan)
                mailSender.sendEmail(strTitle, strContent, [objReviewMan.email])
        else:
            #不发邮件
            pass

    return HttpResponseRedirect('/inception/detail/' + str(workflowId) + '/') 

#终止流程
def cancel(request):
    workflowId = request.POST['workflowid']
    if workflowId == '' or workflowId is None:
        context = {'errMsg': 'workflowId参数为空.'}
        return render(request, 'error/error.html', context)

    workflowId = int(workflowId)
    workflowDetail = sql_order.objects.get(id=workflowId)
    reviewMan = workflowDetail.review_man
    try:
        listAllReviewMen = json.loads(reviewMan)
    except ValueError:
        listAllReviewMen = (reviewMan, )

    #服务器端二次验证，如果正在执行终止动作的当前登录用户，不是发起人也不是审核人，则异常.
    loginUser = request.session.get('login_username', False)
    if loginUser is None or (loginUser not in listAllReviewMen and loginUser != workflowDetail.engineer):
        context = {'errMsg': '当前登录用户不是审核人也不是发起人，请重新登录.'}
        return render(request, 'error/error.html', context)

    #服务器端二次验证，如果当前单子状态是结束状态，则不能发起终止
    if workflowDetail.status in (Const.workflowStatus['abort'], Const.workflowStatus['finish'], Const.workflowStatus['autoreviewwrong'], Const.workflowStatus['exception']):
        return HttpResponseRedirect('/inception/detail/' + str(workflowId) + '/')

    workflowDetail.status = Const.workflowStatus['abort']
    workflowDetail.save()
    
    #如果人工终止了，则根据settings.py里的配置决定是否给提交者和审核人发邮件提醒。如果是发起人终止流程，则给主、副审核人各发一封；如果是审核人终止流程，则给发起人发一封邮件，并附带说明此单子被拒绝掉了，需要重新修改.
    if hasattr(settings, 'MAIL_ON_OFF') == True:
        if getattr(settings, 'MAIL_ON_OFF') == "on":
            url = _getDetailUrl(request) + str(workflowId) + '/'

            engineer = workflowDetail.engineer
            workflowStatus = workflowDetail.status
            workflowName = workflowDetail.workflow_name
            if loginUser == engineer:
                strTitle = "发起人主动终止SQL上线工单流程 # " + str(workflowId)
                strContent = "发起人：" + engineer + "\n审核人：" + reviewMan + "\n工单地址：" + url + "\n工单名称： " + workflowName +"\n执行结果：" + workflowStatus +"\n提醒：发起人主动终止流程"
                for reviewMan in listAllReviewMen:
                    if reviewMan == "":
                        continue
                    objReviewMan = users.objects.get(username=reviewMan)
                    mailSender.sendEmail(strTitle, strContent, [objReviewMan.email])
            else:
                objEngineer = users.objects.get(username=engineer)
                strTitle = "SQL上线工单被拒绝执行 # " + str(workflowId)
                strContent = "发起人：" + engineer + "\n审核人：" + reviewMan + "\n工单地址：" + url + "\n工单名称： " + workflowName +"\n执行结果：" + workflowStatus +"\n提醒：此工单被拒绝执行，请登陆重新提交或修改工单"
                mailSender.sendEmail(strTitle, strContent, [objEngineer.email])
        else:
            #不发邮件
            pass

    return HttpResponseRedirect('/inception/detail/' + str(workflowId) + '/')
#     return HttpResponseRedirect('/workflow/submitsql/')

#展示回滚的SQL
def rollback(request):
    workflowId = request.GET['workflowid']
    if workflowId == '' or workflowId is None:
        context = {'errMsg': 'workflowId参数为空.'}
        return render(request, 'error/error.html', context)
    workflowId = int(workflowId)
    listBackupSql = inceptionDao.getRollbackSqlList(workflowId)
    workflowDetail = sql_order.objects.get(id=workflowId)
    workflowName = workflowDetail.workflow_name
    rollbackWorkflowName = "【回滚工单】原工单Id:%s ,%s" % (workflowId, workflowName)
    cluster_name = workflowDetail.cluster_name
    try:
        listAllReviewMen = json.loads(workflowDetail.review_man)
        review_man = listAllReviewMen[0]
        sub_review_man = listAllReviewMen[1]
    except ValueError:
        review_man = workflowDetail.review_man
        sub_review_man = ''

    context = {'listBackupSql':listBackupSql, 'rollbackWorkflowName':rollbackWorkflowName, 'cluster_name':cluster_name, 'review_man':review_man, 'sub_review_man':sub_review_man}
    return render(request, 'inception/workOrderRollback.html', context)

#SQL审核必读
def dbaprinciples(request):
#     context = {'currentMenu':'dbaprinciples'}
    return render(request, 'inception/dbaprinciples.html')

#图表展示
def charts(request):
    context = {'currentMenu':'charts'}
    return render(request, 'inception/charts.html', context)

#数据库集群展示
def mainConfigList(request):

#     search_keyword = request.GET.get('search_keyword')
# 
#     if search_keyword is None:
#         search_keyword = ''
#     
#     search_keyword = search_keyword.strip()
# 
#     print("search_keyword:",search_keyword)
# 
#     PAGE_LIMIT = 15
# 
#     #参数检查
#     if 'pageNo' in request.GET:
#         pageNo = request.GET['pageNo']
#     else:
#         pageNo = '0'
# 
#     if not isinstance(pageNo, str):
#         raise TypeError('pageNo页面传入参数不对')
#     else:
#         try:
#             pageNo = int(pageNo)
#             if pageNo < 0:
#                 pageNo = 0
#         except ValueError as ve:
#             print(ve)
#             context = {'errMsg': 'pageNo参数不是int.'}
#             return render(request, 'error/error.html', context)
# 
#     offset = pageNo * PAGE_LIMIT
#     limit = offset + PAGE_LIMIT

    paginationList = getPageLimitOffset(request)
    search_keyword = paginationList.get('search_keyword')
    offset = paginationList.get('offset')
    limit = paginationList.get('limit')
    pageNo = paginationList.get('pageNo')
    PAGE_LIMIT = paginationList.get('PAGE_LIMIT')
   
    # 查询
    listMainConfig = []
    listMainConfigNum = 0

    #服务器端参数验证
    if search_keyword == "":
        try:
            listMainConfig = main_config.objects.all().order_by('-create_time')[offset:limit]
            listMainConfigNum = main_config.objects.count()        
        except Exception as e:
            print(e)
            context = {'errMsg': '内部错误！'+str(e)}
            return render(request, 'error/error.html', context)
    else:
        try:
            print("search_keyword is Not None:")
            listMainConfig = main_config.objects.filter(Q(cluster_name__contains=search_keyword)|Q(main_host__contains=search_keyword)).order_by('-create_time')[offset:limit]
            listMainConfigNum = main_config.objects.filter(Q(cluster_name__contains=search_keyword)|Q(main_host__contains=search_keyword)).count()
        except Exception as e:
            print(e)
            context = {'errMsg': '内部错误！'+str(e)}
            return render(request, 'error/error.html', context)
        
    context = {'listMainConfig':listMainConfig, 'listMainConfigNum':listMainConfigNum, 'pageNo':pageNo, 'PAGE_LIMIT':PAGE_LIMIT, 'search_keyword':search_keyword}    
    return render(request, 'inception/mainConfigList.html', context)

# 新增数据库集群配置
def addMainConfigForm(request):
    return render(request, 'inception/addMainConfig.html')

# 查询工单（admin用户）（搜索问题）
def getSqlWorkOrderList(request):

    paginationList = getPageLimitOffset(request)
    search_keyword = paginationList.get('search_keyword')
    offset = paginationList.get('offset')
    limit = paginationList.get('limit')
    pageNo = paginationList.get('pageNo')
    PAGE_LIMIT = paginationList.get('PAGE_LIMIT')
   
    # 查询
    listSqlOrder = []
    listSqlOrderNum = 0

    #服务器端参数验证
    if search_keyword == "":
        try:
            print("search_keyword is None:")
            listSqlOrder = sql_order.objects.all().order_by('-create_time')[offset:limit]
            listSqlOrderNum = sql_order.objects.count()
            pageNum = math.ceil(listSqlOrderNum/PAGE_LIMIT)
            pageLeave = pageNum-pageNo
        except Exception as e:
            print(e)
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)
    else:
        try:
            print("search_keyword is Not None:")
            listSqlOrder = sql_order.objects.filter(Q(workflow_name__contains=search_keyword)|Q(sql_content__contains=search_keyword)).order_by('-create_time')[offset:limit]
            listSqlOrderNum = sql_order.objects.filter(Q(workflow_name__contains=search_keyword)|Q(sql_content__contains=search_keyword)).count()
            pageNum = math.ceil(listSqlOrderNum/PAGE_LIMIT)
            pageLeave = pageNum-pageNo  
        except Exception as e:
            print(e)
            context = {'errMsg': '内部错误！'}
            return render(request, 'error/error.html', context)
        
    

    
    context = {'listSqlOrder':listSqlOrder, 'listSqlOrderNum':listSqlOrderNum, 'pageNo':pageNo, 'pageNum':pageNum, 'pageLeave':pageLeave, 'PAGE_LIMIT':PAGE_LIMIT, "search_keyword":search_keyword}
    
    return render(request, 'inception/sqlWorkOrderlist.html', context)
    
def getSqlWorkOrderDetail(request, sqlOrderId):
    print("begin: 1111")
    sqlOrderDetail = get_object_or_404(sql_order, pk=sqlOrderId)
    if sqlOrderDetail.status in (Const.workflowStatus['finish'], Const.workflowStatus['exception']):
        listContent = json.loads(sqlOrderDetail.execute_result)
    else:
        listContent = json.loads(sqlOrderDetail.review_content)
        
    try:
        listAllReviewMen = json.loads(sqlOrderDetail.review_man)
    except ValueError:
        listAllReviewMen = (sqlOrderDetail.review_man, )

    # 格式化detail界面sql语句和审核/执行结果 by 搬砖工
    for Content in listContent:
        Content[4] = Content[4].split('\n')     # 审核/执行结果
        Content[5] = Content[5].split('\r\n')   # sql语句

    context = {'sqlOrderDetail':sqlOrderDetail, 'listContent':listContent,'listAllReviewMen':listAllReviewMen}
    return render(request, 'inception/sqlWorkOrderDetail.html', context) 

#根据集群名获取主库连接字符串，并封装成一个dict
def getMainConnStr(clusterName):
    listMains = main_config.objects.filter(cluster_name=clusterName)
    
    mainHost = listMains[0].main_host
    mainPort = listMains[0].main_port
    mainUser = listMains[0].main_user
#     mainPassword = prpCryptor.decrypt(listMains[0].main_password)
    mainPassword = listMains[0].main_password
    dictConn = {'mainHost':mainHost, 'mainPort':mainPort, 'mainUser':mainUser, 'mainPassword':mainPassword}
    return dictConn

#获取当前时间
def getNow():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

#获取当前请求url
def _getDetailUrl(request):
    scheme = request.scheme
    host = request.META['HTTP_HOST']
    return "%s://%s/detail/" % (scheme, host)
