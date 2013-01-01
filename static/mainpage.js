//Created on Dec 2, 2012
//author: mark

//included in head of mainpage.html

/*How to ajax
$(document).ready(function(){
	$.get('/ajax').done(function( data){
		alert(data);
	});
});
*/

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