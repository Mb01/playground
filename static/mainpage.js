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
	
	
	
	
	
	
	
	
	$('#term3').terminal(function(command, term){
		if(command !== ''){
			try{
				var result = window.eval(command);
				if(result !== undefined){
					term.echo(new String(result));
				}
			}catch(e){
				term.error(new String(e));
			}
		}else {
			term.echo('');
		}
	},{
		greetings: 'Javascript Interpreter',
		name: 'js_demo',
		height: 200,
		prompt: 'js>'});
});