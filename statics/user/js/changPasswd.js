///admin/password_change/

$('.changePasswd').on('click', function () {
    $("#password").val('');
    $("#confirm_password").val('');
    open_handle = layer.open({
        type: 2,
        title: '修改密码',
        maxmin: true,
        area: ['400px', '450px'], //宽高
        content: '/user/changepasswdpost/'
    });
});
    
//提交配置表单
$('.changePasswdbutton').on('click', function () {
    var strPasswd1 = $("#password").val();
    var strPasswd2 =$("#confirm_password").val();
    url = '/user/changepasswd/'
//    alert(config_value);
    $.ajax({
        type: "POST",
        url: url,
//        dataType:json,
        data: {
        	password: strPasswd1,
        	confirm_password: strPasswd2,
        },
        success: function (data) {
            if (data.status === '1') {
                layer.msg(data.msg, {
                    icon: 1,
                    time: 2000 //2秒关闭（如果不配置，默认是3秒）
                }, function () {
                    layer.close(open_handle);
                });
            } else {
                layer.msg(data.msg, {icon: 2});
            }
        }
    });
});