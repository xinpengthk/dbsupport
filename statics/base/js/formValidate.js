$.validator.setDefaults({
	highlight : function(e) {
		$(e).closest(".form-group").removeClass("has-success").addClass(
				"has-error")
	},
	success : function(e) {
		e.closest(".form-group").removeClass("has-error").addClass(
				"has-success")
	},
	errorElement : "span",
//	errorPlacement : function(e, r) {
//		e.appendTo(r.is(":radio") || r.is(":checkbox") ? r.parent().parent()
//				.parent() : r.parent())
//	},
	errorClass : "help-block m-b-none",
	validClass : "help-block m-b-none"
});


$.extend($.validator.messages, {
    required: "必选字段!",
    remote: "请修正该字段!",
    email: "请输入正确格式的电子邮件!",
    url: "请输入合法的网址!",
    date: "请输入合法的日期!",
    dateISO: "请输入合法的日期 (ISO)!",
    number: "请输入合法的数字！",
    digits: "只能输入整数！",
    creditcard: "请输入合法的信用卡号！",
    equalTo: "两次输入不一致!",
    accept: "请输入拥有合法后缀名的字符串！",
    maxlength: $.validator.format("请输入一个长度最多是 {0} 的字符串"),
    minlength: $.validator.format("请输入一个长度最少是 {0} 的字符串"),
    rangelength: $.validator.format("请输入一个长度介于 {0} 和 {1} 之间的字符串"),
    range: $.validator.format("请输入一个介于 {0} 和 {1} 之间的值"),
    max: $.validator.format("请输入一个最大为 {0} 的值"),
    min: $.validator.format("请输入一个最小为 {0} 的值")
});


// 添加主库配置
$().ready(function() {
	$("#addMasterConfigForm").validate({
		onsubmit:true,// 是否在提交时验证
		onfocusout:false,// 是否在获取焦点时验证
		onkeyup :false,// 是否在敲击键盘时验证
		rules: {
			clusterName: {
		        required: true,
//		        minlength: 6
		    },
		    masterIpaddr: {
		        required: true,
//		        minlength: 6,
		    },
		    masterPort: {
		        required: true,
		    	digits:true
//		        minlength: 6,
		    },
		    masterUser: {
		        required: true,
//		        minlength: 6,
		    },
		    masterPasswd: {
		        required: true,
//		        minlength: 6,
		    },
		},
		submitHandler: function(form) { // 通过之后回调
			var v_cluster_id = $("#masterConfigId").val();
			var v_cluster_name = $("#clusterName").val();
			var v_master_host = $("#masterIpaddr").val();
			var v_master_port = $("#masterPort").val();
			var v_master_user = $("#masterUser").val();
			var v_master_password = $("#masterPasswd").val();
			
			url = '/inception/addMasterConfig/'
		    
		    $.ajax({
		        type: "POST",
		        url: url,
		        data: {
		        	cluster_id: v_cluster_id,
		        	cluster_name: v_cluster_name,
		        	master_host: v_master_host,
		        	master_port: v_master_port,
		        	master_user: v_master_user,
		        	master_password: v_master_password,
		        },
		        success: function (data) {
		            if (data.status == '1') {
		            	layer.msg(data.msg, 
		            			 {icon:1},
		            			 function(){
		            				 var index = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
		            				 parent.layer.close(index); //再执行关闭  
		            			   }
		            			 );
		            } else {
		                layer.msg(data.msg + data.data, {icon: 2});
		            }
		        }
		    });
		},
		invalidHandler: function(form, validator) {return false;}
	}); 
});

// 修改密码
$().ready(function() {
	$("#changePasswdForm").validate({
		onsubmit:true,// 是否在提交时验证
		onfocusout:false,// 是否在获取焦点时验证
		onkeyup :false,// 是否在敲击键盘时验证
		rules: {
			password: {
		        required: true,
//		        minlength: 6
		    },
		    confirm_password: {
		        required: true,
//		        minlength: 6,
		        equalTo: "#password"
		    },
		},
		submitHandler: function(form) { // 通过之后回调
		    var strPasswd1 = $("#password").val();
		    var strPasswd2 =$("#confirm_password").val();
		    url = '/user/changepasswd/'
		    $.ajax({
		        type: "POST",
		        url: url,
		        data: {
		        	password: strPasswd1,
		        	confirm_password: strPasswd2,
		        },
		        success: function (data) {
		            if (data.status == '1') {
		                layer.msg(data.msg, {
		                    icon: 1,
		                    time: 2000 //2秒关闭（如果不配置，默认是3秒）
		                }, function () {
           				 	var index = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
           				 	parent.layer.close(index); //再执行关闭  
		                });
		            } else {
		                layer.msg(data.msg, {icon: 2});
		            }
		        }
		    });
		},
		invalidHandler: function(form, validator) {return false;}
	}); 
});


// 添加用户
$().ready(function() {
	$("#addUserInfoForm").validate({
		onsubmit:true,// 是否在提交时验证
		onfocusout:false,// 是否在获取焦点时验证
		onkeyup :false,// 是否在敲击键盘时验证
		rules: {
			userName: {
		        required: true,
//		        minlength: 6
		    },
		    display: {
		        required: true,
//		        minlength: 6,
		    },
		    role: {
		        required: true,
//		        minlength: 6,
		    },
		    email: {
		        required: true,
		        email: true,
//		        minlength: 6,
		    },	    
		},
		submitHandler: function(form) { // 通过之后回调
			var v_userId = $('#userId').val();
			var v_username = $("#userName").val();
			var v_display = $("#display").val();
			var v_role = $("#role").val();
			var v_email = $("#email").val();
			var v_password = $("#password").val();
			var v_isactive = $("#is_active").is(':checked');
			var v_isstaff = $("#is_staff").is(':checked');
			
			url = '/user/addChangeUserInfo/'
		    
		    $.ajax({
		        type: "POST",
		        url: url,
		        data: {
		        	user_id: v_userId,
		        	user_name: v_username,
		        	display: v_display,
		        	role: v_role,
		        	email: v_email,
		        	password: v_password,
		        	is_active: v_isactive,
		        	is_staff: v_isstaff,
		        },
		        success: function (data) {
		            if (data.status == '1') {
		            	layer.msg(data.msg, 
		            			 {icon:1},
		            			 function(){
		            				 var index = parent.layer.getFrameIndex(window.name); //先得到当前iframe层的索引
		            				 parent.layer.close(index); //再执行关闭  
		            			   }
		            			 );
		            } else {
		                layer.msg(data.msg + data.data, {icon: 2});
		            }
		        }
		    });
		},
		invalidHandler: function(form, validator) {return false;}
	}); 
});

