$(document).ready(function(){
    var accomondation_price=20;
    var breakfast_price=5;
    var tour_price=150;
    
    $('.req-to-book').click(function(){
    
    
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
      cal(accomondation_price,breakfast_price,tour_price);
    });
    
    
    $("#sel1").on("change",function(){
      cal(accomondation_price,breakfast_price,tour_price);
    
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
            cal(accomondation_price,breakfast_price,tour_price);
          }
          });
          
          $('.seconddate').on('change', function() { 
          
            cal(accomondation_price,breakfast_price,tour_price);
          
          });
          
              function GetDays(){
                  
                      var dropdt = new Date(document.getElementById("drop_date").value);
                      
                      var pickdt = new Date(document.getElementById("pick_date").value);
                      return parseInt((dropdt - pickdt) / (24 * 3600 * 1000));
              }
          
              function cal(accomondation_price, breakfast_price,tour_price){
                    var price = 0;
                    var days = GetDays();
                    var numberof_guests = parseInt(document.getElementById("sel1").value);
                    var breakfast_total = numberof_guests * breakfast_price * days;
                    var accomondation_total = days * accomondation_price;
                    price+=accomondation_total+breakfast_total + tour_price;
                    percent_value = price*0.17;
                    price+=percent_value; 
                    document.getElementById("total-value-label").textContent= "$" +price ;
                    document.getElementById("breakfast-value-label").textContent= "$" +breakfast_total ;
                    document.getElementById("accomodation-value-label").textContent= "$" +accomondation_total ;
                    document.getElementById("tour-value-label").textContent= "$" +tour_price ;
    
          }
    
        });
    