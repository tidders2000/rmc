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
    
  
   $(function() {
    $.ajax({
      type: 'GET',
      url: '/names',
      success: function(response) {
        var response = response;
        var names = {};
        for (var i = 0; i < response.length; i++) {
          //console.log(countryArray[i].name);
          names[response[i].firstname] = response[i].flag; //countryArray[i].flag or null
        }
        $('input.autocomplete').autocomplete({
          data: names,
          limit: 5, // The max amount of results that can be shown at once. Default: Infinity.
        });
      }
    });
  });

    
  
}); 
  
 
  
   
    
 