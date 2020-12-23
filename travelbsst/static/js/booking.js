$(document).ready(function(){

$('.req-to-book').click(function(){
  alert(';ssds')


    var d = new Date();
    var result  = d.toLocaleDateString("zh-Hans-CN", { 
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
    }).replace(/[/]/g,'-');

  var second_date = new Date();

  second_date.setDate(d.getDate()+2);
  var result2  = second_date.toLocaleDateString("zh-Hans-CN", { 
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).replace(/[/]/g,'-');

  $('.firstdate').attr('min',result); 
  $('.firstdate').attr('value',result); 
  $('.seconddate').attr('min',result2); 
  $('.seconddate').attr('value',result2); 
  cal();
});
});


$('.firstdate').on('change', function() { 
      var second_date = new Date(document.getElementById("drop_date").value);
      var first_date = new Date(document.getElementById("pick_date").value);
     
      
      var datearray = $('.firstdate').val().split("-");
      var montharray = [01, 02, 03,04, 05,06,07, 08 ,09  ,10 ,11 ,12  ];
      
      var year = datearray[0];
      
      
      var month = datearray[1];
      
      var day = 2+parseInt(datearray[2]);
      
      var minDate = (year +"-"+ month +"-"+ day);
      $('.seconddate').attr('min',minDate); 
      $('.seconddate').attr('value',minDate); 

      if(second_date > first_date){
        cal();
      }
      });
      
      $('.seconddate').on('change', function() { 
      
      cal() 
      
      });
      
          function GetDays(){
              
                  var dropdt = new Date(document.getElementById("drop_date").value);
                  
                  var pickdt = new Date(document.getElementById("pick_date").value);
                  return parseInt((dropdt - pickdt) / (24 * 3600 * 1000));
          }
      
          function cal(){
      
                var dropdt = new Date(document.getElementById("drop_date").value);
                var days = GetDays();
                var price = 220;
                if(days > 2){
                  price += days*25;
                }
                alert('sdsdsdsdsdsdsdsdsdsd')
                price+=(price*0.12)+(price*0.05);
                document.getElementById("value-label").textContent= "$" +price ;
          
      }