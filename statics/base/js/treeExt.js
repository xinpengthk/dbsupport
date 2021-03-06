$(function() {
	var e = [ {
		text : "父节点 1",
		href : "#parent1",
		tags : [ "4" ],
		nodes : [ {
			text : "子节点 1",
			href : "#child1",
			tags : [ "2" ],
			nodes : [ {
				text : "孙子节点 1",
				href : "#grandchild1",
				tags : [ "0" ]
			}, {
				text : "孙子节点 2",
				href : "#grandchild2",
				tags : [ "0" ]
			} ]
		}, {
			text : "子节点 2",
			href : "#child2",
			tags : [ "0" ]
		} ]
	}, {
		text : "父节点 2",
		href : "#parent2",
		tags : [ "0" ]
	}, {
		text : "父节点 3",
		href : "#parent3",
		tags : [ "0" ]
	}, {
		text : "父节点 4",
		href : "#parent4",
		tags : [ "0" ]
	}, {
		text : "父节点 5",
		href : "#parent5",
		tags : [ "0" ]
	} ], 
	
	o = [ {
		text : "父节点 1",
		tags : [ "2" ],
		nodes : [ {
			text : "子节点 1",
			tags : [ "3" ],
			nodes : [ {
				text : "孙子节点 1",
				tags : [ "6" ]
			}, {
				text : "孙子节点 2",
				tags : [ "3" ]
			} ]
		}, {
			text : "子节点 2",
			tags : [ "3" ]
		} ]
	}, {
		text : "父节点 2",
		tags : [ "7" ]
	}, {
		text : "父节点 3",
		icon : "glyphicon glyphicon-earphone",
		href : "#demo",
		tags : [ "11" ]
	}, {
		text : "父节点 4",
		icon : "glyphicon glyphicon-cloud-download",
		href : "/demo.html",
		tags : [ "19" ],
		selected : !0
	}, {
		text : "父节点 5",
		icon : "glyphicon glyphicon-certificate",
		color : "pink",
		backColor : "red",
		href : "http://www.tesco.com",
		tags : [ "available", "0" ]
	} ],
	t = '[{"text": "父节点 1","nodes": [{"text": "子节点 1","nodes": [{"text": "孙子节点 1"},{"text": "孙子节点 2"}]},{"text": "子节点 2"}]},{"text": "父节点 2"},{"text": "父节点 3"},{"text": "父节点 4"},{"text": "父节点 5"}]';
	$("#treeview11").treeview({
		color : "#428bca",
		data : e,
		onNodeSelected : function(e, o) {
			$("#event_output").prepend("<p>您单击了 " + o.text + "</p>")
		}
	})
});