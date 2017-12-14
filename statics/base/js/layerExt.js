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
	layer.open({
        type: 2,
        title: '工单详情',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '800px'], //宽高
        content: '/inception/detail/' + workflowid  + '/',
        end: function () {
        	location.reload();
        }
    });
}

function addWorkOrder() {
	layer.open({
		type : 2,
		title : '新增工单',
		shade : false,
		shadeClose : false,
		maxmin : true,
		area : [ '1200px', '800px' ], // 宽高
		content : '/inception/submitsql/',
		end : function() {
			location.reload();
		}
	});
}

function rollbackWorkOrder(workflowid) {
	layer.open({
        type: 2,
        title: '回滚请求',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '800px'], //宽高
        content: '/inception/rollback/?workflowid=' + workflowid,
        end: function () {
            location.reload();
        }
    });
}

// 主库配置类
function addMasterConfig() {
	 open_handle = layer.open({
        type: 2,
        title: '新增主库配置',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['800px', '700px'], //宽高
        content: '/inception/addMasterConfigForm/',
        end: function () {
            location.reload();
        }
    });
}


function changeMasterConfig(configid, clusterName, masterIpaddr, masterPort, masterUser, masterPasswd) {
	layer.open({
        type: 2,
        title: '修改主库配置',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['800px', '700px'], //宽高
        content: '/inception/addMasterConfigForm/',
        success: function(layero, index){
//        	$("#masterConfigId").val(configid);
//        	$("#clusterName").val(clusterName);
//        	$("#masterIpaddr").val(masterIpaddr);
//        	$("#masterPort").val(masterPort);
//        	$("#masterUser").val(masterUser);
//        	$("#masterPasswd").val(masterPasswd);
        	

        	var body = layer.getChildFrame('body', index);
            body.find("#masterConfigId").val(configid);
            body.find("#clusterName").val(clusterName);
            body.find("#masterIpaddr").val(masterIpaddr);
            body.find("#masterPort").val(masterPort);
            body.find("#masterUser").val(masterUser);
            body.find("#masterPasswd").val(masterPasswd);
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
	layer.open({
        type: 2,
        title: '工单详情',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '800px'], //宽高
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
	 open_handle = layer.open({
       type: 2,
       title: '新增用户',
 	   shade: false,
 	   shadeClose: false,
       maxmin: true,
       area: ['800px', '700px'], //宽高
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

function changeUserInfo(userId, userName, display, role, email, password, is_active, is_staff) {
	layer.open({
        type: 2,
        title: '修改用户信息',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['800px', '700px'], //宽高
        content: '/user/addUserForm/',
        success: function(layero, index){
        	var body = layer.getChildFrame('body', index);
            body.find("#userId").val(userId);
            body.find('#password').val(password)
            body.find("#userName").val(userName);
            body.find("#display").val(display);
            body.find("#role").val(role);
            body.find("#email").val(email);
            if (is_active == 'True') {
            	body.find("#is_active").attr('checked', 'checked');
            } else {
            	body.find("#is_active").removeAttr('checked');
            }
            if (is_staff == 'True'){
            	body.find("#is_staff").attr('checked', 'checked');
            } else {
            	body.find("#is_staff").removeAttr('checked');
            }
        },
        end: function () {
            location.reload();
        }
    });
}

// cmdb 类
function addHost() {
	 open_handle = layer.open({
       type: 2,
       title: '新增主机信息',
 	   shade: false,
 	   shadeClose: false,
       maxmin: true,
       area: ['800px', '850px'], //宽高
       content: '/cmdb/addHostForm/',
       end: function () {
           location.reload();
       }
   });
}

function changeHostInfo(hostId) {
	layer.open({
        type: 2,
        title: '修改主机信息',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['800px', '800px'], //宽高
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
    	            	var body = layer.getChildFrame('body', index);
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
	 open_handle = layer.open({
      type: 2,
      title: '新增主机用户信息',
	  shade: false,
	  shadeClose: false,
      maxmin: true,
      area: ['800px', '400px'], //宽高
      content: '/cmdb/addHostUserForm/',
      success: function(layero, index){
      	var body = layer.getChildFrame('body', index);
        body.find("#hostId").val(hostId);
      },
      end: function () {
          location.reload();
      }
  });
}

//
function getHostDetail(hostId) {
	layer.open({
        type: 2,
        title: '主机详情',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '800px'], //宽高
        content: '/cmdb/getHostDetail/' + hostId  + '/',
//        end: function () {
//        	location.reload();
//        }
    });
}

function changeHostUserInfo(hostId, hostUserId, hostUser, hostUserPasswd, hostUserDesc) {
	layer.open({
        type: 2,
        title: '修改主机用户信息',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['800px', '450px'], //宽高
        content: '/cmdb/addHostUserForm/',
        success: function(layero, index){
    	            var body = layer.getChildFrame('body', index);
    	            body.find("#hostId").val(hostId);
    	            body.find("#hostUserId").val(hostUserId);
    	            body.find("#hostUser").val(hostUser);
    	            body.find("#hostPasswd").val(hostUserPasswd);
    	            body.find("#userDesc").val(hostUserDesc);
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