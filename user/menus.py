# -*- coding: UTF-8 -*- 
from user.models import users
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
            'sort':1,
            'role':'super'              
            },

#             {'key':'submitsql',
#             'name':'发起SQL上线',
#             'url':'/inception/submitsql/',
#             },
#             {'key':'dbaprinciples',
#             'name':'SQL审核规范',
#             'url':'/inception/dbaprinciples/',
#             },               
        ],
#     'REDIS管理':[
#             {'key':'allworkflow',
#              'name':'查询键值',
#              'url':'/redis/getkey/',
#              },        
#         ],
}

leftMenusSuper = {
    'INCEPTION 后台管理':[
            {'key':'masterconfig',
            'name':'主库地址配置',
#             'url':'/admin/inception/master_config/',
            'url':'/inception/masterConfigList/',
            'sort':1,
            'role':'super'
            },
            {'key':'workflowconfig',
            'name':'所有工单管理',
            'url':'/inception/getSqlWorkOrderList/',
            'sort':2,
            'role':'super'
            },
            {'key':'charts',
            'name':'工单统计',
            'url':'/inception/charts/',
            'sort':3,
            'role':'super'            
            },                      
        ],
    '用户管理':[
            {'key':'userconfig',
            'name':'用户权限配置',
            'url':'/user/getUserList/',
            'sort':1,
            'role':'super'
            },
        ], 
    '服务器资源管理':[
            {'key':'hostconfig',
            'name':'主机管理',
            'url':'/cmdb/getHostList/',
            'sort':1,
            'role':'super'
            },
#             {'key':'dbClusterconfig',
#             'name':'数据库集群配置',
#             'url':'/cmdb/getDbClusterList/',
#             'sort':2,
#             'role':'super'
#             }, 
            {'key':'dbGroupconfig',
            'name':'数据库管理',
            'url':'/cmdb/getDbGroupList/',
            'sort':3,
            'role':'super'
            }, 
        ],     
                     
}

def getMenus(request):
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