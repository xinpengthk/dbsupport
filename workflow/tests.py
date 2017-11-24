from django.test import TestCase

# Create your tests here.
leftMenusGeneral = {
    '数据库变更审核（MySQL）':[
            {'key':'allworkflow',
            'name':'查看历史工单',
            'url':'/workflow/allworkflow/',
            'sort':1,
            'role':'general'
            },
            {'key':'submitsql',
            'name':'发起SQL上线',
            'url':'/workflow/submitsql/',
            'sort':2,
            'role':'general'
            },
            {'key':'dbaprinciples',
            'name':'SQL审核必读',
            'url':'/workflow/dbaprinciples/',
            'sort':6,
            'role':'general'
            },
            {'key':'charts',
            'name':'统计图表展示',
            'url':'/workflow/charts/',
            'sort':7,
            'role':'general'
            },
        ],
    '线上REDI查询':[
            {'key':'allworkflow',
             'name':'查询键值',
             'url':'/workflow/allworkflow/',
            'sort':1,
            'role':'general'
             },        
        ],
}

leftMenusSuper = {
    '后台管理':[
            {'key':'masterconfig',
            'name':'主库地址配置',
            'url':'/admin/workflow/master_config/',
            'sort':3,
            'role':'super'
            },
            {'key':'userconfig',
            'name':'用户权限配置',
            'url':'/admin/workflow/users/',
            'sort':4,
            'role':'super'
            },
            {'key':'workflowconfig',
            'name':'所有工单管理',
            'url':'/admin/workflow/workflow/',
            'sort':5,
            'role':'super'
            },
        ],
}

# if __name__ == '__main__':
#     print(type(leftMenus))
#     print(leftMenus.get('数据库变更审核（MySQL）'))
#     print(type(leftMenus.get('数据库变更审核（MySQL）')))

#     for menuLevel1,menuLevel2List in leftMenus.items():
#         for menuLevel2 in menuLevel2List:
#             if menuLevel2.get('role') == 'super':
#                 print(menuLevel2)
#                 leftMenus.get(menuLevel1).remove(menuLevel2)
#     print(leftMenus)
            
