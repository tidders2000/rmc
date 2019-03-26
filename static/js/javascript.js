  $(document).ready(function(){
   $('.fixed-action-btn').floatingActionButton();
     
    
    $('.sidenav').sidenav();
    $('.tooltipped').tooltip();
    $('select').formSelect();
    $('.datepicker').datepicker();
  
      
   $('.slider').slider({
    height: 700,
    indicators: false
    });
  
var names=[];

function loadnames(){
	$.getJSON('/names', function(data, status, xhr){
		for (var i = 0; i < data.length; i++ ) {
        	names.push(data[i].name);
    	}
});
};

loadnames();

$('#names').autocomplete({
	source: names, 
	});
}); 
  
 
  
   
    
 