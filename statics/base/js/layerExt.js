// 用户类
$('.changePasswd').on('click', function () {
    $("#password").val('');
    $("#confirm_password").val('');
    open_handle = layer.open({
        type: 2,
        title: '修改密码',
        maxmin: true,
        area: ['600px', '430px'], //宽高
        content: '/user/changepasswdpost/'
    });
});

// 普通用户 SQL 工单类
function showWorkOrderDetail(workflowid) {
	parent.layer.open({
        type: 2,
        title: '工单详情',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/inception/detail/' + workflowid  + '/',
        end: function () {
        	location.reload();
        }
    });
}

function addWorkOrder() {
	parent.layer.open({
		type : 2,
		title : '新增工单',
		shade : false,
		shadeClose : false,
		maxmin : true,
		area : [ '1200px', '600px' ], // 宽高
		content : '/inception/submitsql/',
		end : function() {
			location.reload();
		}
	});
}

function rollbackWorkOrder(workflowid) {
	parent.layer.open({
        type: 2,
        title: '回滚请求',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
//        area: ['80%', '80%'], //宽高
        content: '/inception/rollback/?workflowid=' + workflowid,
        end: function () {
            location.reload();
        }
    });
}

// 主库配置类
function addMasterConfig() {
	 open_handle = parent.layer.open({
        type: 2,
        title: '新增主库配置',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/inception/addMasterConfigForm/',
        end: function () {
            location.reload();
        }
    });
}


function changeMasterConfig(configid) {
	parent.layer.open({
        type: 2,
        title: '修改主库配置',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/inception/addMasterConfigForm/',
        success: function(layero, index){
        	var url = '/inception/getMasterConfigDetailInfo/'
                $.ajax({
                    type: "POST",
                    url: url,
                    data: {configId: configid,},                
        	        success: function (data) {
        	            if (data.status == '1') {
        	            	var masterConfigObj = JSON.parse(data.obj);
        	            	var body = parent.layer.getChildFrame('body', index);
        	                body.find("#masterConfigId").val(masterConfigObj.id);
        	                body.find("#clusterName").val(masterConfigObj.cluster_name);
        	                body.find("#masterIpaddr").val(masterConfigObj.master_host);
        	                body.find("#masterPort").val(masterConfigObj.master_port);
        	                body.find("#masterUser").val(masterConfigObj.master_user);
        	                body.find("#masterPasswd").val(masterConfigObj.master_password);
        	            } else {
        	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
        	            }
        	        }
                });
        },
        end: function () {
            location.reload();
        }
    });
}

function delMasterConfig(id) {
    url = '/inception/delMasterConfig/';
    layer.confirm('你确定要删除吗？', {
        btn: ['确定', '取消'] //按钮
    }, function () {
        $.ajax({
            type: "POST",
            url: url,
            data: {masterConfigId:id},
	        success: function (data) {
	            if (data.status == '1') {
	            	layer.msg(data.msg, {icon: 1, time: 1000},function(){location.reload()});
	            } else {
	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
	            }
	        }
        });
    });
}

// admin 工单类
function getSqlOrderDetail(sqlOrderId) {
	parent.layer.open({
        type: 2,
        title: '工单详情',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/inception/getSqlWorkOrderDetail/' + sqlOrderId  + '/',
        end: function () {
        	location.reload();
        }
    });
}

function delSqlOrder(id) {
    url = '/inception/delsqlOrder/';
    layer.confirm('你确定要删除吗？', {
        btn: ['确定', '取消'] // 按钮
    }, function () {
        $.ajax({
            type: "POST",
            url: url,
            data: {sqlOrderId:id},
	        success: function (data) {
	            if (data.status == '1') {
	            	layer.msg(data.msg, {icon: 1, time: 1000},function(){location.reload()});
	            } else {
	                layer.msg(data.msg + data.data, {icon:2, time: 1000},function(){location.reload()});
	            }
	        }
        });
    });
}

function addUser() {
	open_handle = parent.layer.open({
       type: 2,
       title: '新增用户',
 	   shade: false,
 	   shadeClose: false,
       maxmin: true,
       area: ['1200px', '600px'], //宽高
       content: '/user/addUserForm/',
       end: function () {
           location.reload();
       }
   });
}


function delUser(id) {
    url = '/user/delUser/';
    layer.confirm('你确定要删除吗？', {
        btn: ['确定', '取消'] //按钮
    }, function () {
        $.ajax({
            type: "POST",
            url: url,
            data: {userId:id},
	        success: function (data) {
	            if (data.status == '1') {
	            	layer.msg(data.msg, {icon: 1, time: 1000},function(){location.reload()});
	            } else {
	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
	            }
	        }
        });
    });
}


function resetUserPasswd(id) {
    url = '/user/resetUserPasswd/';
    layer.confirm('你确定要重置该用户密码吗？', {
        btn: ['确定', '取消'] //按钮
    }, function () {
        $.ajax({
            type: "POST",
            url: url,
            data: {userId:id},
	        success: function (data) {
	            if (data.status == '1') {
	            	layer.msg(data.msg, {icon: 1, time: 1000},function(){location.reload()});
	            } else {
	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
	            }
	        }
        });
    });
}

function changeUserInfo(userId) {
	parent.layer.open({
        type: 2,
        title: '修改用户信息',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/user/addUserForm/',
        success: function(layero, index){
        	var url = '/user/getUserDetailInfo/'
                $.ajax({
                    type: "POST",
                    url: url,
                    data: {userId: userId,},                
        	        success: function (data) {
        	            if (data.status == '1') {
        	            	var userObj = JSON.parse(data.obj);
        	            	var body = parent.layer.getChildFrame('body', index);
        	            	
        	                body.find("#userId").val(userObj.id);
        	                body.find('#password').val(userObj.password)
        	                body.find("#userName").val(userObj.username);
        	                body.find("#display").val(userObj.display);
        	                body.find("#role").val(userObj.role);
        	                body.find("#email").val(userObj.email);
        	                if (userObj.is_active){
        	                	body.find("#is_active").attr('checked', 'checked');
        	                } else {
        	                	body.find("#is_active").removeAttr('checked');
        	                }
        	                
        	                if (userObj.is_staff){
        	                	body.find("#is_staff").attr('checked', 'checked');
        	                } else {
        	                	body.find("#is_staff").removeAttr('checked');
        	                }
        	                
        	                
//        	                if (userObj.is_active == 'True') {
//        	                	body.find("#is_active").attr('checked', 'checked');
//        	                } else {
//        	                	body.find("#is_active").removeAttr('checked');
//        	                }
//        	                if (userObj.is_staff == 'True'){
//        	                	body.find("#is_staff").attr('checked', 'checked');
//        	                } else {
//        	                	body.find("#is_staff").removeAttr('checked');
//        	                }

        	            } else {
        	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
        	            }
        	        }
                });

        },
        end: function () {
            location.reload();
        }
    });
}

// cmdb 类
function addHost() {
	open_handle = parent.layer.open({
       type: 2,
       title: '新增主机信息',
 	   shade: false,
 	   shadeClose: false,
       maxmin: true,
       area: ['1200px', '600px'], //宽高
       content: '/cmdb/addHostForm/',
       end: function () {
           location.reload();
       }
   });
}

function changeHostInfo(hostId) {
	parent.layer.open({
        type: 2,
        title: '修改主机信息',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/cmdb/addHostForm/',
        success: function(layero, index){
        	var url = '/cmdb/getHostDetailInfo/'
            $.ajax({
                type: "POST",
                url: url,
                data: {hostId: hostId,},                
    	        success: function (data) {
    	            if (data.status == '1') {
    	            	var hostObj = JSON.parse(data.obj);
    	            	var body = parent.layer.getChildFrame('body', index);
    	                body.find("#hostId").val(hostObj.id);
    	                body.find("#businessName").val(hostObj.businessName);
    	                body.find("#serviceEnv").val(hostObj.serviceEnv);
    	                body.find("#hostName").val(hostObj.hostName);
    	                body.find("#intranetIpAddr").val(hostObj.intranetIpAddr);
    	                body.find("#publicIpAddr").val(hostObj.publicIpAddr);
    	                body.find("#sshPort").val(hostObj.sshPort);
    	                body.find("#hostType").val(hostObj.hostType);
    	                body.find("#hostRole").val(hostObj.hostRole);
    	                body.find("#hostDesc").val(hostObj.hostDesc);              
    	            } else {
    	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
    	            }
    	        }
            });     
        },
        end: function () {
            location.reload();
        }
    });
}

function delHost(id) {
    url = '/cmdb/delHost/';
    layer.confirm('你确定要删除吗？', {
        btn: ['确定', '取消'] //按钮
    }, function () {
        $.ajax({
            type: "POST",
            url: url,
            data: {hostId:id},
	        success: function (data) {
	            if (data.status == '1') {
	            	layer.msg(data.msg, {icon: 1, time: 1000},function(){location.reload()});
	            } else {
	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
	            }
	        }
        });
    });
}


function addHostUser(hostId) {
	 open_handle = parent.layer.open({
      type: 2,
      title: '新增主机用户信息',
	  shade: false,
	  shadeClose: false,
      maxmin: true,
      area: ['1200px', '600px'], //宽高
      content: '/cmdb/addHostUserForm/',
      success: function(layero, index){
      	var body = parent.layer.getChildFrame('body', index);
        body.find("#hostId").val(hostId);
      },
      end: function () {
          location.reload();
      }
  });
}

//
function getHostDetail(hostId) {
	parent.layer.open({
        type: 2,
        title: '主机详情',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/cmdb/getHostDetail/' + hostId  + '/',
//        end: function () {
//        	location.reload();
//        }
    });
}

function changeHostUserInfo(hostUserId) {
	parent.layer.open({
        type: 2,
        title: '修改主机用户信息',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/cmdb/addHostUserForm/',
        success: function(layero, index){
        	var url = '/cmdb/getHostUserDetailInfo/'
                $.ajax({
                    type: "POST",
                    url: url,
                    data: {hostUserId: hostUserId,},                
        	        success: function (data) {
        	            if (data.status == '1') {
        	            	var hostUserObj = JSON.parse(data.hostUserJson);
        	            	var body = parent.layer.getChildFrame('body', index);
        	            	
            	            body.find("#hostId").val(hostUserObj[0].fields.host[0]);
            	            body.find("#hostUserId").val(hostUserObj[0].pk);
            	            body.find("#hostUser").val(hostUserObj[0].fields.hostUser);
            	            body.find("#hostPasswd").val(hostUserObj[0].fields.hostPasswd);
            	            body.find("#userDesc").val(hostUserObj[0].fields.userDesc);

        	            } else {
        	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
        	            }
        	        }
                });
        },
        end: function () {
            location.reload();
        }
    });
}

function delHostUser(v_hostUserId) {
    url = '/cmdb/delHostUser/';
    layer.confirm('你确定要删除吗？', {
        btn: ['确定', '取消'] //按钮
    }, function () {
        $.ajax({
            type: "POST",
            url: url,
            data: {hostUserId:v_hostUserId},
	        success: function (data) {
	            if (data.status == '1') {
	            	layer.msg(data.msg, {icon: 1, time: 1000},function(){location.reload()});
	            } else {
	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
	            }
	        }
        });
    });
}

function addDBCluster() {
	 open_handle = parent.layer.open({
      type: 2,
      title: '新增数据库集群信息',
	  shade: false,
	  shadeClose: false,
      maxmin: true,
      area: ['1200px', '600px'], //宽高
      content: '/cmdb/addDbClusterForm/',
      end: function () {
          location.reload();
      }
  });
}

function changeDBClusterInfo(clusterId) {
	parent.layer.open({
        type: 2,
        title: '修改数据库集群信息',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/cmdb/addDbClusterForm/',
        success: function(layero, index){
        	
        	var url = '/cmdb/getDbClusterDetailInfo/'
                $.ajax({
                    type: "POST",
                    url: url,
                    data: {clusterId: clusterId,},                
        	        success: function (data) {
        	            if (data.status == '1') {
        	            	var dbClusterObj = JSON.parse(data.obj);
        	            	var body = parent.layer.getChildFrame('body', index);
        	            	
            	            body.find("#clusterId").val(dbClusterObj.clusterId);
            	            body.find("#clusterName").val(dbClusterObj.clusterName);
            	            body.find("#clusterStatus").val(dbClusterObj.clusterStatus);
            	            body.find("#clusterDesc").val(dbClusterObj.clusterDesc);

        	            } else {
        	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
        	            }
        	        }
                });
//    	            var body = layer.getChildFrame('body', index);
//    	            body.find("#clusterId").val(clusterId);
//    	            body.find("#clusterName").val(clusterName);
//    	            body.find("#clusterStatus").val(clusterStatus);
//    	            body.find("#clusterDesc").val(clusterDesc);
        },
        end: function () {
            location.reload();
        }
    });
}

function delDBCluster(v_Cluster_id) {
    url = '/cmdb/delDbCluster/';
    layer.confirm('你确定要删除吗？', {
        btn: ['确定', '取消'] //按钮
    }, function () {
        $.ajax({
            type: "POST",
            url: url,
            data: {cluster_id:v_Cluster_id},
	        success: function (data) {
	            if (data.status == '1') {
	            	layer.msg(data.msg, {icon: 1, time: 1000},function(){location.reload()});
	            } else {
	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
	            }
	        }
        });
    });
}

function getDBClusterDetail(ClusterId) {
	parent.layer.open({
        type: 2,
        title: '集群详情',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/cmdb/getDbClusterDetail/' + ClusterId  + '/',
//        end: function () {
//        	location.reload();
//        }
    });
}


function addDBGroup() {
	 open_handle = parent.layer.open({
     type: 2,
     title: '新增数据库组',
	 shade: false,
	 shadeClose: false,
     maxmin: true,
     area: ['1200px', '600px'], //宽高
     content: '/cmdb/addDbGroupForm/',
     end: function () {
         location.reload();
     }
 });
}

function changeDBGroupInfo(groupId) {
	parent.layer.open({
        type: 2,
        title: '修改数据库组信息',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/cmdb/addDbGroupForm/',
        success: function(layero, index){
        	var url = '/cmdb/getDbGroupDetailInfo/'
                $.ajax({
                    type: "POST",
                    url: url,
                    data: {groupId: groupId,},                
        	        success: function (data) {
        	            if (data.status == '1') {
        	            	var dbGroupObj = JSON.parse(data.obj);
        	            	var body = parent.layer.getChildFrame('body', index);
        	            	
        	        	    body.find("#groupId").val(dbGroupObj.groupId);
        	        	    body.find("#businessName").val(dbGroupObj.businessName);
        	        	    body.find("#groupName").val(dbGroupObj.groupName);
        	        	    body.find("#groupEnv").val(dbGroupObj.groupEnv);
        	        	    body.find("#groupStatus").val(dbGroupObj.groupStatus);
        	        	    body.find("#groupDesc").val(dbGroupObj.groupDesc);

        	            } else {
        	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
        	            }
        	        }
                });
        },
        end: function () {
            location.reload();
        }
    });
}

function getInstanceDetail(groupId) {
	parent.layer.open({
        type: 2,
        title: '实例详情',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/cmdb/getInstanceDetail/' + groupId  + '/',
//        end: function () {
//        	location.reload();
//        }
    });
}

function addDBInstance(groupId) {
	open_handle = parent.layer.open({
    type: 2,
    title: '新增实例',
	shade: false,
	shadeClose: false,
    maxmin: true,
    area: ['1200px', '600px'], //宽高
    content: '/cmdb/addDbInstanceForm/' + groupId  + '/',
    end: function () {
        location.reload();
    }
});
}


//有问题，需要调试
function changeDbInstanceInfo(instanceId) {
	parent.layer.open({
        type: 2,
        title: '修改数据库实例信息',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '600px'], //宽高
        content: '/cmdb/changDbInstanceForm/',
        success: function(layero, index){
        	
        	var url = '/cmdb/getDbInstanceDetailInfo/'
                $.ajax({
                    type: "POST",
                    url: url,
                    data: {instanceId: instanceId,},                
        	        success: function (data) {
        	            if (data.status == '1') {
        	            	var dbInstanceObj = JSON.parse(data.dbInstanceJson);
        	            	var body = parent.layer.getChildFrame('body', index);
            	            body.find("#instanceId").val(dbInstanceObj[0].pk);
            	            body.find("#groupId").val(dbInstanceObj[0].fields.groupName[0]);
            	            body.find("#groupNameDisplay").val(dbInstanceObj[0].fields.groupName[1]);
            	            body.find("#hostId").append("<option value='" + dbInstanceObj[0].fields.host[0] + "' selected='selected'>" + dbInstanceObj[0].fields.host[1] + "-" + dbInstanceObj[0].fields.host[2] + "</option>");
            	            body.find("#instanceName").val(dbInstanceObj[0].fields.instanceName);
            	            body.find("#instanceType").val(dbInstanceObj[0].fields.instanceType);
            	            body.find("#portNum").val(dbInstanceObj[0].fields.portNum);
            	            body.find("#instanceRole").val(dbInstanceObj[0].fields.instanceRole);
            	            body.find("#instanceStatus").val(dbInstanceObj[0].fields.instanceStatus);
            	            body.find("#instanceDesc").val(dbInstanceObj[0].fields.instanceDesc);
            	            body.find("#instanceId").attr("readonly", "readonly")
            	            body.find("#hostIdDefault1").remove()
            	            body.find("#hostIdDefault2").remove()

        	            } else {
        	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
        	            }
        	        }
                });
        	

        },
        end: function () {
            location.reload();
        }
    });
}

function delDbInstance(instanceId) {
    url = '/cmdb/delDbInstance/';
    layer.confirm('你确定要删除吗？', {
        btn: ['确定', '取消'] //按钮
    }, function () {
        $.ajax({
            type: "POST",
            url: url,
            data: {instanceId:instanceId},
	        success: function (data) {
	            if (data.status == '1') {
	            	layer.msg(data.msg, {icon: 1, time: 1000},function(){location.reload()});
	            } else {
	                layer.msg(data.msg + data.data, {icon: 2, time: 1000},function(){location.reload()});
	            }
	        }
        });
    });
}