#!/usr/bin/env python
#-*-coding:utf-8-*-

'''
Created on 2017年12月12日

@Author: Xinpeng
@Description: 用来处理分页的类
'''
from django.shortcuts import render


def getPageLimitOffset(request):

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
    
    pageList = {'offset':offset, 'limit':limit, 'search_keyword':search_keyword, 'PAGE_LIMIT':PAGE_LIMIT, 'pageNo':pageNo}
    
    return pageList