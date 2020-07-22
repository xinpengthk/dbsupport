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
            {'key':'submitsql',
            'name':'发起SQL上线',
            'url':'/inception/submitsql/',
            },
            {'key':'dbaprinciples',
            'name':'SQL审核规范',
            'url':'/inception/dbaprinciples/',
            },
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
            {'key':'mainconfig',
            'name':'主库地址配置',
            'url':'/admin/inception/main_config/',
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



if __name__ == '__main__':
   
    print(dict(leftMenusSuper, **leftMenusGeneral))
#     for menuLevel1,menuLevel2List in leftMenus.items():
#          print('##:%s', menuLevel1)
#          for menuLevel2 in menuLevel2List:
#              print('####:%s', menuLevel2.get('name'))