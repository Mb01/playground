//Created on Dec 2, 2012
//author: mark
//included in head of mainpage.html



function readCookie(name) {
	var nameEQ = name + "=";
	var ca = document.cookie.split(';');
	for(var i=0;i < ca.length;i++) {
		var c = ca[i];
		while (c.charAt(0)==' ') c = c.substring(1,c.length);
		if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length,c.length);
	}
	return null;
}


var attach = function(){
	$cb = $("#createButton").parent();
	oldVal = $cb.html();
	$.post("/ajax", $('#createForm').serialize());
	$cb.fadeOut('slow');
	$cb.html(oldVal);
	$cb.fadeIn('slow');
	$("#createButton").click(attach);
	$("#createForm")[0].reset();
};


$(function(){
	$("#tabs").tabs();
	
	$("#next").click(function(){
		$.get("/ajax", function(data){
			$('#question').html(data);
		});
	});
	
	$("#createButton").click(attach);
});