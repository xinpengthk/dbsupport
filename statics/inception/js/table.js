var open_handle;
$(document).ready(function () {
    $('.dataTables-base').dataTable();
    //添加配置页面
    $('.showPage').on('click', function () {
        $("#config_id").val('');
        $("#config").val('');
        $("#env_name").val('');
        $("#push_path").val('');
        $("#config_key").val('');
        $("#config_value").val('');
        open_handle = layer.open({
            type: 1,
            maxmin: true,
            area: ['500px', '70%'], //宽高
            content: $('#add_config')
        });
    });
    //提交配置表单
    $('.addconfigbutton').on('click', function () {
        var config_id = $("#config_id").val();
        var project = $("project").val();
        var project_id = $("#project_id").val();
        var env_name = $("#env_name").val();
        var push_path = $("#push_path").val();
        var config = $("#config").val();
        var config_key = $("#config_key").val();
        var config_value = $("#config_value").val();
//        alert(config_value);
        if (config_id > 0) {
            url = '/index/configuration/doEdit';
        } else {
            url = '/index/configuration/doAdd';
        }
        $.ajax({
            type: "POST",
            url: url,
//            dataType:json,
            data: {
                config: config,
                config_key: config_key,
                config_value: config_value,
                project: project,
                project_id: project_id,
                config_id: config_id,
                env_name: env_name,
                push_path: push_path,
            },
            success: function (data) {
                if (data.code === '200') {
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
});
function showConfigInfo(id, titlename) {
    layer.open({
        type: 1,
        title: titlename,
        maxmin: true,
        shade: false,
        area: ['500px', '70%'], //宽高
        content: $('#showInfo' + id)
    });
}

function editConfigInfo(id, key, env_name, push_path, config_key) {
    $("#config_id").val(id);
    $("#config").val(key);
    $("#config_value").val($("#showInfo" + id).text());
    $("#env_name").val(env_name);
    $("#push_path").val(push_path);
    $("#config_key").val(config_key);

    open_handle = layer.open({
        type: 1,
        maxmin: true,
        area: ['500px', '70%'], //宽高
        content: $('#add_config')
    });
}
function delConfig(id) {
    url = '/index/configuration/doDel';
    layer.confirm('你确定要删除吗？', {
        btn: ['删除', '点错了'] //按钮
    }, function () {
        $.ajax({
            type: "POST",
            url: url,
            data: "config_id=" + id,
            success: function (data) {
                layer.msg(data.msg, {icon: 1});
            }
        });
    });
}