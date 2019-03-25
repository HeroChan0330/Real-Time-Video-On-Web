function init(){
	$(".ctrlBtn").mousedown(function(){
		var val=$(this).attr("comm");
		console.log(val);
		$.get("../command?comm=SetDir&val="+val,function(data,status){
			if(data!="success"){
				mui.toast("指令发送失败")
			}
		});
	});
	$("#speedCtrl").change(function(){
		var val=$(this).val();
		console.log("speed="+val.toString());
		$.get("../command?comm=SetSpeed&val="+val,function(data,status){
			if(data!="success"){
				mui.toast("指令发送失败")
			}
		});
	});
}
