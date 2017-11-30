
//$('.show-work-order-detail').click(function(){
//	layer.open({
//	  type: 2, 
////	  content: '/workflow/detail/' + {{workflow.id}}  + '/'
////	  content: '/workflow/detail/' + {{workflow.id}} + '/'
//	  content: '/workflow/allworkflow/\{\{workflow.id\}\}/' //这里content是一个URL，如果你不想让iframe出现滚动条，你还可以content: ['http://sentsin.com', 'no']
//		  
//	}); 
//});

function showWorkOrderDetail(workflowid) {
	parent.layer.open({
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
	parent.layer.open({
        type: 2,
        title: '新增工单',
  	  	shade: false,
  	  	shadeClose: false,
        maxmin: true,
        area: ['1200px', '800px'], //宽高
        content: '/inception/submitsql/',
        end: function () {
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
        area: ['1200px', '800px'], //宽高
        content: '/inception/rollback/?workflowid=' + workflowid,
        end: function () {
            location.reload();
        }
    });
}


