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

$(function(){
	$("#tabs").tabs();
	
	$("#next").click(function(){
		$.get("/ajax", function(data){
			$('#question').html(data);
		});
	});
	
	$("#createButton").click(function(){
		$.post("/ajax", $('#createForm').serialize()) ;
	});
});