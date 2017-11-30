# -*- coding: UTF-8 -*- 
from user.models import users
# leftMenuBtnsCommon = (
#                     {'key':'allworkflow',
#                      'name':'工单查询',
#                      'url':'/workflow/allworkflow/',
#                      'class':'glyphicon glyphicon-home'
#                     },
#                     {'key':'submitsql',
#                      'name':'发起SQL上线',
#                      'url':'/workflow/submitsql/',
#                      'class':'glyphicon glyphicon-asterisk'
#                     },
#                )
# 
# leftMenuBtnsSuper = (
#                    {'key':'masterconfig',
#                     'name':'主库地址配置',
#                     'url':'/admin/workflow/master_config/',
#                     'class':'glyphicon glyphicon-user'
#                     },
#                    {'key':'userconfig',
#                     'name':'用户权限配置',
#                     'url':'/admin/workflow/users/',
#                     'class':'glyphicon glyphicon-th-large'
#                     },
#                    {'key':'workflowconfig',
#                     'name':'所有工单管理',
#                     'url':'/admin/workflow/workflow/',
#                     'class':'glyphicon glyphicon-list-alt'
#                     },
#                      
# )
# leftMenuBtnsDoc = (
#                    {'key':'dbaprinciples',
#                     'name':'SQL审核必读',
#                     'url':'/workflow/dbaprinciples/',
#                     'class':'glyphicon glyphicon-book'},
#                    {'key':'charts',
#                     'name':'数据库变更统计',
#                     'url':'/workflow/charts/',
#                     'class':'glyphicon glyphicon-file'
#                     },
# )
# 
# def global_info1(request):
#     """存放用户，会话信息等."""
#     loginUser = request.session.get('login_username', None)
#     if loginUser is not None:
#         user = users.objects.get(username=loginUser)
#         if user.is_superuser:
#             leftMenuBtns = leftMenuBtnsCommon + leftMenuBtnsSuper + leftMenuBtnsDoc
#         else:
#             leftMenuBtns = leftMenuBtnsCommon + leftMenuBtnsDoc
#     else:
#         leftMenuBtns = ()
# 
#     return {
#         'loginUser':loginUser,
#         'leftMenuBtns':leftMenuBtns,
#     }

"""
Created on 2017-11-20
@author: xinpeng
@Description: 定义二级菜单
dic = {'name': 'xinpeng', 'age':28, 'job':'Engineer'， 'ex_list':['a', 'b']}
"""
leftMenusGeneral = {
    '数据库变更管理':[
            {'key':'allworkflow',
            'name':'工单管理',
            'url':'/inception/allworkflow/',
            },
#             {'key':'submitsql',
#             'name':'发起SQL上线',
#             'url':'/inception/submitsql/',
#             },
#             {'key':'dbaprinciples',
#             'name':'SQL审核规范',
#             'url':'/inception/dbaprinciples/',
#             },
            {'key':'charts',
            'name':'数据库变更统计',
            'url':'/inception/charts/',
            },
        ],
    '线上REDI查询':[
            {'key':'allworkflow',
             'name':'查询键值',
             'url':'/redis/getkey/',
             },        
        ],
}

leftMenusSuper = {
    '后台管理':[
            {'key':'masterconfig',
            'name':'主库地址配置',
            'url':'/admin/inception/master_config/',
            'sort':3,
            'role':'super'
            },
            {'key':'userconfig',
            'name':'用户权限配置',
            'url':'/admin/inception/users/',
            'sort':4,
            'role':'super'
            },
            {'key':'workflowconfig',
            'name':'所有工单管理',
            'url':'/admin/inception/sql_order/',
            'sort':5,
            'role':'super'
            },
        ],
}

def global_info(request):
    """存放用户，会话信息等."""
    loginUser = request.session.get('login_username', None)
    UserRole = '超级管理员'
    if loginUser is not None:
        user = users.objects.get(username=loginUser)
        UserRole = user.role
        if user.is_superuser:
            leftMenuBtns = dict(leftMenusSuper, **leftMenusGeneral)
        else:
            leftMenuBtns = leftMenusGeneral
    else:
        leftMenuBtns = ()

    return {
        'UserRole':UserRole,
        'loginUser':loginUser,
        'leftMenuBtns':leftMenuBtns,
    }


# if __name__ == '__main__':
#     print(dict(leftMenusSuper, **leftMenusGeneral))
#      for menuLevel1,menuLevel2List in leftMenus.items():
#          print('##:%s', menuLevel1)
#          for menuLevel2 in menuLevel2List:
#              print('####:%s', menuLevel2.get('name'))