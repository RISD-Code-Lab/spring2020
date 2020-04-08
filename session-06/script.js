$(document).ready(function(){

	$('main').on('mousemove', function(e) {

		var cursorX = e.pageX / $(this).width();
		var cursorY = 1 - (e.pageY) / $(this).height();

		var positionX = Math.floor(cursorX * 1000);
		var positionY = Math.floor(cursorY * 1000);

		var setting = "'wght' " + positionY + ", 'wdth' " + positionX;
		$("#letters").css("font-variation-settings", setting);
	});

});
	