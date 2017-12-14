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


$(function(){
    // 判断整数value是否等于0 
    jQuery.validator.addMethod("isIntEqZero", function(value, element) { 
         value=parseInt(value);      
         return this.optional(element) || value==0;       
    }, "整数必须为0"); 
      
    // 判断整数value是否大于0
    jQuery.validator.addMethod("isIntGtZero", function(value, element) { 
         value=parseInt(value);      
         return this.optional(element) || value>0;       
    }, "整数必须大于0"); 
      
    // 判断整数value是否大于或等于0
    jQuery.validator.addMethod("isIntGteZero", function(value, element) { 
         value=parseInt(value);      
         return this.optional(element) || value>=0;       
    }, "整数必须大于或等于0");   
    
    // 判断整数value是否不等于0 
    jQuery.validator.addMethod("isIntNEqZero", function(value, element) { 
         value=parseInt(value);      
         return this.optional(element) || value!=0;       
    }, "整数必须不等于0");  
    
    // 判断整数value是否小于0 
    jQuery.validator.addMethod("isIntLtZero", function(value, element) { 
         value=parseInt(value);      
         return this.optional(element) || value<0;       
    }, "整数必须小于0");  
    
    // 判断整数value是否小于或等于0 
    jQuery.validator.addMethod("isIntLteZero", function(value, element) { 
         value=parseInt(value);      
         return this.optional(element) || value<=0;       
    }, "整数必须小于或等于0");  
    
    // 判断浮点数value是否等于0 
    jQuery.validator.addMethod("isFloatEqZero", function(value, element) { 
         value=parseFloat(value);      
         return this.optional(element) || value==0;       
    }, "浮点数必须为0"); 
      
    // 判断浮点数value是否大于0
    jQuery.validator.addMethod("isFloatGtZero", function(value, element) { 
         value=parseFloat(value);      
         return this.optional(element) || value>0;       
    }, "浮点数必须大于0"); 
      
    // 判断浮点数value是否大于或等于0
    jQuery.validator.addMethod("isFloatGteZero", function(value, element) { 
         value=parseFloat(value);      
         return this.optional(element) || value>=0;       
    }, "浮点数必须大于或等于0");   
    
    // 判断浮点数value是否不等于0 
    jQuery.validator.addMethod("isFloatNEqZero", function(value, element) { 
         value=parseFloat(value);      
         return this.optional(element) || value!=0;       
    }, "浮点数必须不等于0");  
    
    // 判断浮点数value是否小于0 
    jQuery.validator.addMethod("isFloatLtZero", function(value, element) { 
         value=parseFloat(value);      
         return this.optional(element) || value<0;       
    }, "浮点数必须小于0");  
    
    // 判断浮点数value是否小于或等于0 
    jQuery.validator.addMethod("isFloatLteZero", function(value, element) { 
         value=parseFloat(value);      
         return this.optional(element) || value<=0;       
    }, "浮点数必须小于或等于0");  
    
    // 判断浮点型  
    jQuery.validator.addMethod("isFloat", function(value, element) {       
         return this.optional(element) || /^[-\+]?\d+(\.\d+)?$/.test(value);       
    }, "只能包含数字、小数点等字符"); 
     
    // 匹配integer
    jQuery.validator.addMethod("isInteger", function(value, element) {       
         return this.optional(element) || (/^[-\+]?\d+$/.test(value) && parseInt(value)>=0);       
    }, "匹配integer");  
     
    // 判断数值类型，包括整数和浮点数
    jQuery.validator.addMethod("isNumber", function(value, element) {       
         return this.optional(element) || /^[-\+]?\d+$/.test(value) || /^[-\+]?\d+(\.\d+)?$/.test(value);       
    }, "匹配数值类型，包括整数和浮点数");  
    
    // 只能输入[0-9]数字
    jQuery.validator.addMethod("isDigits", function(value, element) {       
         return this.optional(element) || /^\d+$/.test(value);       
    }, "只能输入0-9数字");  
    
    // 判断中文字符 
    jQuery.validator.addMethod("isChinese", function(value, element) {       
         return this.optional(element) || /^[\u0391-\uFFE5]+$/.test(value);       
    }, "只能包含中文字符。");   
 
    // 判断英文字符 
    jQuery.validator.addMethod("isEnglish", function(value, element) {       
         return this.optional(element) || /^[A-Za-z]+$/.test(value);       
    }, "只能包含英文字符。");   
 
     // 手机号码验证    
    jQuery.validator.addMethod("isMobile", function(value, element) {    
      var length = value.length;    
      return this.optional(element) || (length == 11 && /^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$/.test(value));    
    }, "请正确填写您的手机号码。");

    // 电话号码验证    
    jQuery.validator.addMethod("isPhone", function(value, element) {    
      var tel = /^(\d{3,4}-?)?\d{7,9}$/g;    
      return this.optional(element) || (tel.test(value));    
    }, "请正确填写您的电话号码。");

    // 联系电话(手机/电话皆可)验证   
    jQuery.validator.addMethod("isTel", function(value,element) {   
        var length = value.length;   
        var mobile = /^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\d{8})$/;   
        var tel = /^(\d{3,4}-?)?\d{7,9}$/g;       
        return this.optional(element) || tel.test(value) || (length==11 && mobile.test(value));   
    }, "请正确填写您的联系方式"); 
 
     // 匹配qq      
    jQuery.validator.addMethod("isQq", function(value, element) {       
         return this.optional(element) || /^[1-9]\d{4,12}$/;       
    }, "匹配QQ");   
 
     // 邮政编码验证    
    jQuery.validator.addMethod("isZipCode", function(value, element) {    
      var zip = /^[0-9]{6}$/;    
      return this.optional(element) || (zip.test(value));    
    }, "请正确填写您的邮政编码。");  
    
    // 匹配密码，以字母开头，长度在6-12之间，只能包含字符、数字和下划线。      
    jQuery.validator.addMethod("isPwd", function(value, element) {       
         return this.optional(element) || /^[a-zA-Z]\\w{6,12}$/.test(value);       
    }, "以字母开头，长度在6-12之间，只能包含字符、数字和下划线。");  
    
    // 身份证号码验证
    jQuery.validator.addMethod("isIdCardNo", function(value, element) { 
      //var idCard = /^(\d{6})()?(\d{4})(\d{2})(\d{2})(\d{3})(\w)$/;   
      return this.optional(element) || isIdCardNo(value);    
    }, "请输入正确的身份证号码。"); 

    // IP地址验证   
    jQuery.validator.addMethod("ip", function(value, element) {    
      return this.optional(element) || /^(([1-9]|([1-9]\d)|(1\d\d)|(2([0-4]\d|5[0-5])))\.)(([1-9]|([1-9]\d)|(1\d\d)|(2([0-4]\d|5[0-5])))\.){2}([1-9]|([1-9]\d)|(1\d\d)|(2([0-4]\d|5[0-5])))$/.test(value);    
    }, "请填写正确的IP地址。");
   
    // 字符验证，只能包含中文、英文、数字、下划线等字符。    
    jQuery.validator.addMethod("stringCheck", function(value, element) {       
         return this.optional(element) || /^[a-zA-Z0-9\u4e00-\u9fa5-_]+$/.test(value);       
    }, "只能包含中文、英文、数字、下划线等字符");   
   
    // 匹配english  
    jQuery.validator.addMethod("isEnglish", function(value, element) {       
         return this.optional(element) || /^[A-Za-z]+$/.test(value);       
    }, "匹配english");   
    
    // 匹配汉字  
    jQuery.validator.addMethod("isChinese", function(value, element) {       
         return this.optional(element) || /^[\u4e00-\u9fa5]+$/.test(value);       
    }, "匹配汉字");   
    
    // 匹配中文(包括汉字和字符) 
    jQuery.validator.addMethod("isChineseChar", function(value, element) {       
         return this.optional(element) || /^[\u0391-\uFFE5]+$/.test(value);       
    }, "匹配中文(包括汉字和字符) "); 
      
    // 判断是否为合法字符(a-zA-Z0-9-_)
    jQuery.validator.addMethod("isRightfulString", function(value, element) {       
         return this.optional(element) || /^[A-Za-z0-9_-]+$/.test(value);       
    }, "判断是否为合法字符(a-zA-Z0-9-_)");   
    
    // 判断是否包含中英文特殊字符，除英文"-_"字符外
    jQuery.validator.addMethod("isContainsSpecialChar", function(value, element) {  
         var reg = RegExp(/[(\ )(\`)(\~)(\!)(\@)(\#)(\$)(\%)(\^)(\&)(\*)(\()(\))(\+)(\=)(\|)(\{)(\})(\')(\:)(\;)(\')(',)(\[)(\])(\.)(\<)(\>)(\/)(\?)(\~)(\！)(\@)(\#)(\￥)(\%)(\…)(\&)(\*)(\（)(\）)(\—)(\+)(\|)(\{)(\})(\【)(\】)(\‘)(\；)(\：)(\”)(\“)(\’)(\。)(\，)(\、)(\？)]+/);   
         return this.optional(element) || !reg.test(value);       
    }, "含有中英文特殊字符");   
   

	  //车牌号校验
	  function isPlateNo(plateNo){
	      var re = /^[\u4e00-\u9fa5]{1}[A-Z]{1}[A-Z_0-9]{5}$/;
	      if(re.test(plateNo)){
	          return true;
	      }
	      return false;
	  }
	  
    //身份证号码的验证规则
    function isIdCardNo(num){ 
    　   //if (isNaN(num)) {alert("输入的不是数字！"); return false;} 
    　　 var len = num.length, re; 
    　　 if (len == 15) 
    　　 re = new RegExp(/^(\d{6})()?(\d{2})(\d{2})(\d{2})(\d{2})(\w)$/); 
    　　 else if (len == 18) 
    　　 re = new RegExp(/^(\d{6})()?(\d{4})(\d{2})(\d{2})(\d{3})(\w)$/); 
    　　 else {
            //alert("输入的数字位数不对。"); 
            return false;
        } 
    　　 var a = num.match(re); 
    　　 if (a != null) 
    　　 { 
    　　 if (len==15) 
    　　 { 
    　　 var D = new Date("19"+a[3]+"/"+a[4]+"/"+a[5]); 
    　　 var B = D.getYear()==a[3]&&(D.getMonth()+1)==a[4]&&D.getDate()==a[5]; 
    　　 } 
    　　 else 
    　　 { 
    　　 var D = new Date(a[3]+"/"+a[4]+"/"+a[5]); 
    　　 var B = D.getFullYear()==a[3]&&(D.getMonth()+1)==a[4]&&D.getDate()==a[5]; 
    　　 } 
    　　 if (!B) {
            //alert("输入的身份证号 "+ a[0] +" 里出生日期不对。"); 
            return false;
        } 
    　　 } 
    　　 if(!re.test(num)){
            //alert("身份证最后一位只能是数字和字母。");
            return false;
        }
    　　 return true; 
    } 

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

//添加主机
$().ready(function() {
	$("#addHostForm").validate({
		onsubmit:true,// 是否在提交时验证
		onfocusout:false,// 是否在获取焦点时验证
		onkeyup :false,// 是否在敲击键盘时验证
		rules: {
			businessName: {
		        required: true,
		        maxlength: 32,
		    },
		    hostName: {
		        required: true,
		        maxlength: 64,
		    },
		    intranetIpAddr: {
		        required: true,
		        ip: true,
		    },
		    publicIpAddr: {
		        required: true,
		        ip: true,
		    },		   
		    sshPort: {
		        required: true,
		        digits: true,
//		        minlength: 6,
		    },	    
		},
		submitHandler: function(form) { // 通过之后回调
			var v_hostId = $('#hostId').val();
			var v_businessName = $('#businessName').val();
			var v_serviceEnv = $("#serviceEnv").val();
			var v_hostName = $("#hostName").val();
			var v_intranetIpAddr = $("#intranetIpAddr").val();
			var v_publicIpAddr = $("#publicIpAddr").val();
			var v_sshPort = $("#sshPort").val();
			var v_hostType = $("#hostType").val();
			var v_hostRole = $("#hostRole").val();
			var v_hostDesc = $("#hostDesc").val();
			
			url = '/cmdb/addChangeHostInfo/'
		    
		    $.ajax({
		        type: "POST",
		        url: url,
		        data: {
		        	host_id : v_hostId,
		        	business_name : v_businessName,
		        	service_env : v_serviceEnv,
		        	host_name : v_hostName,
		        	intranet_ipaddr : v_intranetIpAddr,
		        	public_ipaddr : v_publicIpAddr,
		        	ssh_port : v_sshPort,
		        	host_type : v_hostType,
		        	host_role : v_hostRole,
		        	host_desc : v_hostDesc,
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


//添加主机用户
$().ready(function() {
	$("#addHostUserForm").validate({
		onsubmit:true,// 是否在提交时验证
		onfocusout:false,// 是否在获取焦点时验证
		onkeyup :false,// 是否在敲击键盘时验证
		rules: {
			hostUser: {
		        required: true,
		        maxlength: 64,
		    },
		    hostPasswd: {
		        required: true,
		        maxlength: 300,
		    },
		    userDesc: {
		        required: true,
		    },    
		},
		submitHandler: function(form) { // 通过之后回调
			var v_hostUserId = $('#hostUserId').val();
			var v_hostId = $('#hostId').val();
			var v_hostUser = $('#hostUser').val();
			var v_hostPasswd = $("#hostPasswd").val();
			var v_userDesc = $("#userDesc").val();
			
			url = '/cmdb/addChangeHostUserInfo/'
		    
		    $.ajax({
		        type: "POST",
		        url: url,
		        data: {
		        	host_user_id : v_hostUserId,
		        	host_id : v_hostId,
		        	host_user : v_hostUser,
		        	host_passwd : v_hostPasswd,
		        	user_desc : v_userDesc,
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
