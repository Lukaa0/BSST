$(document).ready(function(){

  var e = document.getElementById("pricesell");
  var strUser = e.options[e.selectedIndex].value;
  
//initialize the variables
  var accomondation_price=parseFloat((strUser));
  var breakfast_price=parseFloat(document.getElementById("breakfast_price").innerHTML);
  var admin_fee = parseFloat(document.getElementById("administration_fee").innerHTML);
  var tour_price = 0;
  var comm_fund = parseFloat(document.getElementById("community_fund").innerHTML);
  var flat_fees = parseFloat(document.getElementById("flat_fees").innerHTML);
  var per_person_charges = parseFloat(document.getElementById("per_person_charges").innerHTML);
  var administration_charges = parseFloat(document.getElementById("administration_charge").innerHTML);

    //initialize current date on calendar
var today = new Date();
var dd = String(today.getDate()).padStart(2, '0');
var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
var yyyy = today.getFullYear();
var today = (yyyy+"-"+mm+"-"+dd);
$('.firstdate').attr('min',today);
$('.firstdate-popup').attr('min',today);
//set the second date to readonly
document.getElementById("drop_date").readOnly = true; 
// end

//additional_initialization
var selectedIndexText = $( "#sel1 option:selected" ).text();
document.getElementById("guests_number").value = selectedIndexText;

  
 selectedIndexText = $( "#sel2 option:selected" ).text();
 document.getElementById("accomodation_type").value = selectedIndexText;
 

  if (!$("#multitype").hasClass('multitype'))
  document.getElementById("sel2").disabled = true;


   $('#req-to-book').click(function(){

    //transfer date to popup
    setDate('.firstdate','.firstdate-popup');
    setDate('.seconddate', '.seconddate-popup');
    document.getElementById("pick_date_popup").readOnly = true; 
    document.getElementById("drop_date_popup").readOnly = true; 
    document.getElementById("sel1_popup").disabled=true;
    document.getElementById("sel2_popup").disabled = true;
   

    //form validation
    if(!document.getElementById("pick_date").value==""){ 
    $(this).attr("data-toggle", "modal");
    $(this).attr("data-target", "#exampleModalCenter");
    } 
    else {
      document.getElementById("errorlabel").innerHTML = "Please select the arrival date"
      document.getElementById("errorlabel").style.display = "initial";
      document.getElementById("errorlabel").style.color = "#ec7e24";
    }   
   });


   function validate(){

    //TODO

  var name =   document.getElementById("name");
   var surname = document.getElementById("surname");
   var email = document.getElementById("email");
   var countrylist = document.getElementById("country");
   var countrycode = document.getElementById("countrycode");
   var phonenumber = document.getElementById("phonenumber");
   var sendemailform = document.getElementById("sendemailform");
   }
    
    $('#send-req-popup').click(function(){

   

      var spliter = document.getElementById("total-value-label-popup").innerHTML.split('$');
    
     var value = parseFloat(spliter[1])
    $("#price_send").val(value);
    
    

    });



  $("#sel1").on("change",function(){

    var selectedIndexText = $( "#sel1 option:selected" ).text();
    document.getElementById("guests_number").value = selectedIndexText;

    if(!document.getElementById("pick_date").value==""){ 
      cal(accomondation_price,breakfast_price,tour_price);
    }
    

    var val = document.getElementById("sel1").value;
    $("#sel1_popup").val(val);
    
  });


  //room typeselector 

  $("#sel2").on("change",function(){

   
    var index = $("#sel2",).prop('selectedIndex');
    var selectedIndexText = $( "#sel2 option:selected" ).text();
    document.getElementById("accomodation_type").value = selectedIndexText;
    
       
    var e = document.getElementById("pricesell");
    var strUser = e.options[e.selectedIndex].value;
    console.log(parseFloat(strUser))

      accomondation_price=parseFloat((strUser));
      
      
       if(!document.getElementById("pick_date").value==""){ 
         cal(accomondation_price,breakfast_price,tour_price);
       }
      
     
       document.getElementById("sel2_popup").selectedIndex = index;
   
     });

     $("#sel2_popup").on("change",function(){

   
      var index = $("#sel2_popup",).prop('selectedIndex');
      
      var selectedIndexText = $( "#sel2_popup option:selected" ).text();
    document.getElementById("accomodation_type").value = selectedIndexText;
      
      document.getElementById('pricesell').selectedIndex = index;
         
      var e = document.getElementById("pricesell");
      var strUser = e.options[e.selectedIndex].value;
  
        accomondation_price=parseFloat((strUser));
        
        
         if(!document.getElementById("pick_date_popup").value==""){ 
           calpopup(accomondation_price,breakfast_price,tour_price);
         }
        
       
       
     
       });
       
 //getters
 function getDay($value) {
  var datearray = $($value).val().split("-");
  var day = datearray[2];
    
  return day;
}

function getMonth($value) {
  var datearray = $($value).val().split("-");
  var month = datearray[1];
  
  return month;
}

function getYear($value) {
  var datearray = $($value).val().split("-");
  var year = datearray[0];
  
  return year;
}

  
function setDate (getFrom,setTo){

  var date = $(getFrom).val();

  $(setTo).attr('value',date);


 

}
function addDays(date, days) {
 var result = new Date(date);
 result.setDate(result.getDate() + days);
 return result;
}

function setinterval2days(getFrom1,setTo1) 
{
  var date = addDays($(getFrom1).val(),2);
 var dateFormatted = formatDate(date)
 document.getElementById("drop_date").value = dateFormatted;
 $(setTo1).attr('min',dateFormatted);

}

function setinterval2dayspopup(getFrom1,setTo1) 
{
  var date = addDays($(getFrom1).val(),2);
 var dateFormatted = formatDate(date)
 document.getElementById("drop_date_popup").value = dateFormatted;
 $(setTo1).attr('min',dateFormatted);

}

function formatDate(date){
  
  var month = date.getMonth() + 1;
  var day = date.getDate();
  if(month<=9)
    month = '0'+month
  if(day<=9)
  day = '0'+day;
    var dateFormatted = date.getFullYear() + '-' + month +  '-' + day;
    return dateFormatted
}



  $('.firstdate').on('change', function() {
       
    if( document.getElementById("errorlabel").style.display == "initial" )
    document.getElementById("errorlabel").style.display = "none"

      if( document.getElementById("drop_date").readOnly = true)
      document.getElementById("drop_date").readOnly = false; 

       
           
       
          setinterval2days('.firstdate', '.seconddate' );
          

            
         

         cal(accomondation_price, breakfast_price,tour_price);
       
        });

        $('.seconddate').on('change', function() {
         
          cal(accomondation_price, breakfast_price,tour_price);

           

        });




            function GetDays(){

                    var dropdt = new Date(document.getElementById("drop_date").value);


                    var pickdt = new Date(document.getElementById("pick_date").value);


                    return parseInt((dropdt - pickdt) / (24 * 3600 * 1000));
            }

          
            function cal(accomondation_price, breakfast_price,tour_price){
                  
                  var price = 0;
                  var days = GetDays();
                  var numberof_guests = parseInt(document.getElementById("sel1",).value);
                  var breakfast_total = numberof_guests * breakfast_price * days;
                  
                  //summarize flat fees + per-person-charges.
                var tour_price = tour_price+flat_fees+(per_person_charges*numberof_guests);
                 // apply administration charge
                  tour_price = tour_price + tour_price*administration_charges;

                  var accomondation_total = days * accomondation_price+breakfast_total;
                  price+=accomondation_total+tour_price;
                  tour_price
                  
                  percent_value = price*0.17;
                  var adminperc = price *admin_fee
                  var comperc = price*comm_fund
                  price+=percent_value;

                  price= price;

                  document.getElementById("total-value-label").textContent= "$" +price.toFixed(2) ;
                   document.getElementById("total-value-label-popup").textContent= "$" +price.toFixed(2) ;
                   document.getElementById("accomodation-value-label-popup").textContent= "$" +accomondation_total.toFixed(2) ;
                  document.getElementById("accomodation-value-label").textContent= "$" +accomondation_total.toFixed(2) ;
                
                  document.getElementById("accomodation_and_breakfast").value = "" + accomondation_total.toFixed(2);
                  document.getElementById("popup_tour_price").value = "" +tour_price.toFixed(2) ;
                  document.getElementById("administration_fee_price").value = "" +adminperc.toFixed(2);
                  document.getElementById("community_fund_price").value = "" + comperc.toFixed(2);
                  document.getElementById("popup_total_price").value = "" + price.toFixed(2);


                  document.getElementById("tour-value-label").textContent= "$" +tour_price.toFixed(2) ;
                   document.getElementById("tour-value-label-popup").textContent= "$" +tour_price.toFixed(2) ;
                  document.getElementById("admin-value-label").textContent= "$" +adminperc.toFixed(2) ;
                   document.getElementById("admin-value-label-popup").textContent= "$" +adminperc.toFixed(2) ;
                  document.getElementById("community-value-label").textContent= "$" +comperc.toFixed(2) ;
                  document.getElementById("community-value-label-popup").textContent= "$" +comperc.toFixed(2) ;
                  document.getElementById('breakdown-boxes').style.display = "initial";
                  
        }  

        //mobile popup js start

        $('.firstdate-popup').on('change', function() {
          var second_date = new Date(document.getElementById("drop_date_popup").value);
          var first_date = new Date(document.getElementById("pick_date_popup").value);
  
        
          
             
         
            setinterval2dayspopup('.firstdate-popup', '.seconddate-popup' );
            
  
              
           
  
             calpopup(accomondation_price, breakfast_price,tour_price);
         
          });
  
          $('.seconddate-popup').on('change', function() {
           
             calpopup(accomondation_price, breakfast_price,tour_price);
  
             
  
          });

          function GetDayspopup(){

            var dropdt = new Date(document.getElementById("drop_date_popup").value);


            var pickdt = new Date(document.getElementById("pick_date_popup").value);


            return parseInt((dropdt - pickdt) / (24 * 3600 * 1000));
    }

    $("#sel1_popup").on("change",function(){
      var selectedIndexText = $( "#sel1_popup option:selected" ).text();
      document.getElementById("guests_number").value = selectedIndexText;

      if(!document.getElementById("pick_date_popup").value==""){ 
        calpopup(accomondation_price,breakfast_price,tour_price);
      }
    
    });

   

    function calpopup(accomondation_price, breakfast_price,tour_price){
      var price = 0;
      var days = GetDayspopup();
      var numberof_guests = parseInt(document.getElementById("sel1_popup",).value);
      var breakfast_total = numberof_guests * breakfast_price * days;
      var accomondation_total = days * accomondation_price+breakfast_total;
      
  //summarize flat fees + per-person-charges.
  var tour_price = tour_price+flat_fees+(per_person_charges*numberof_guests);
  // apply administration charge
   tour_price = tour_price + tour_price*administration_charges;

      price+=accomondation_total+tour_price;

      percent_value = price*0.17;
      var adminperc = price * admin_fee;
      var comperc = price*comm_fund;
      price+=percent_value;

      price= price;

                  document.getElementById("accomodation_and_breakfast").value = "" + accomondation_total.toFixed(2);
                  document.getElementById("popup_tour_price").value = "" +tour_price.toFixed(2) ;
                  document.getElementById("administration_fee_price").value = "" +adminperc.toFixed(2);
                  document.getElementById("community_fund_price").value = "" + comperc.toFixed(2);
                  document.getElementById("popup_total_price").value = "" + price.toFixed(2);
     
       document.getElementById("total-value-label-popup").textContent= "$" +price.toFixed(2) ;
    
      document.getElementById("accomodation-value-label-popup").textContent= "$" +accomondation_total.toFixed(2) ;


       document.getElementById("tour-value-label-popup").textContent= "$" +tour_price.toFixed(2) ;
     
       document.getElementById("admin-value-label-popup").textContent= "$" +adminperc.toFixed(2) ;
     
      document.getElementById("community-value-label-popup").textContent= "$" +comperc.toFixed(2) ;

      document.getElementById('breakdown-boxes').style.display = "initial";
      
}  

//country  code selector

$("#countrycode").on("change",function(){

   
  var index = $("#countrycode",).prop('selectedIndex');
    if(index!=0){
      $("#inputicon_countrycode").removeClass();
$("#inputicon_countrycode").addClass("fas");
$("#inputicon_countrycode").addClass("fas");
$("#inputicon_countrycode").addClass("fas"); 
$("#inputicon_countrycode").addClass("fa-check-circle"); 
$("#inputicon_countrycode").addClass("valid"); 
 $("#inputicon_countrycode").addClass("selectIcon"); 
document.getElementById("inputicon_countrycode").style.color = "#00635e";
    } else{
      $("#inputicon_countrycode").removeClass();
$("#inputicon_countrycode").addClass("fas"); 
$("#inputicon_countrycode").addClass("fa-times-circle"); 
$("#inputicon_countrycode").addClass("invalid"); 
$("#inputicon_countrycode").addClass("selectIcon"); 
document.getElementById("inputicon_countrycode").style.color = "#ec7e24";
    }
});

$("#country").on("change",function(){

   
  var index = $("#country",).prop('selectedIndex');
  
 
  document.getElementById('countrycode').selectedIndex = index;

     if(index!=0){
      $("#inputicon_country").removeClass();
        $("#inputicon_country").addClass("fas");
        $("#inputicon_country").addClass("fas");
        $("#inputicon_country").addClass("fas"); 
        $("#inputicon_country").addClass("fa-check-circle"); 
        $("#inputicon_country").addClass("valid"); 
         $("#inputicon_country").addClass("selectIcon"); 
         $("#inputicon_country").addClass("selectIcon"); 
         
        document.getElementById("inputicon_country").style.color = "#00635e";
// for country code
$("#inputicon_countrycode").removeClass();
$("#inputicon_countrycode").addClass("fas");
$("#inputicon_countrycode").addClass("fas");
$("#inputicon_countrycode").addClass("fas"); 
$("#inputicon_countrycode").addClass("fa-check-circle"); 
$("#inputicon_countrycode").addClass("valid"); 
 $("#inputicon_countrycode").addClass("selectIcon"); 
document.getElementById("inputicon_countrycode").style.color = "#00635e";

     } else{
      $("#inputicon_country").removeClass();
      $("#inputicon_country").addClass("fas"); 
      $("#inputicon_country").addClass("fa-times-circle"); 
      $("#inputicon_country").addClass("invalid"); 
      $("#inputicon_country").addClass("selectIcon"); 
      document.getElementById("inputicon_country").style.color = "#ec7e24";
// for country code
$("#inputicon_countrycode").removeClass();
$("#inputicon_countrycode").addClass("fas"); 
$("#inputicon_countrycode").addClass("fa-times-circle"); 
$("#inputicon_countrycode").addClass("invalid"); 
$("#inputicon_countrycode").addClass("selectIcon"); 
document.getElementById("inputicon_countrycode").style.color = "#ec7e24";
     }
  var e = document.getElementById("countrycode");
   
  
  
   });


  //mobile popup js end
        
  
  

//activities stuff
    (function (global) {
      var acts = [];
      
      var html = [];
            var str = global.localStorage.getItem("activities");
            var activities = JSON.parse(str);
            var accomCommunityName = $(".accom-com-name").attr("id");
            var counter = -1;
            var cunter =-1;
            var tempActivities = [];


              if(activities == null){
                document.getElementById("activity-value-label").innerHTML = document.getElementById("emptyactivities").innerHTML;
                document.getElementById("activity-value-label-popup").innerHTML = document.getElementById("emptyactivities").innerHTML;
            
              }
              else

            if(activities.length>0){
              for(var i =0;i<activities.length;i++){
                if(activities[i].communityName==accomCommunityName){
                  tempActivities.push(activities[i]);
              }
              
              }
              activities = tempActivities;
            }
            if(activities==null){
              document.getElementById("activity-value-label").innerHTML = document.getElementById("emptyactivities").innerHTML;
              document.getElementById("activity-value-label-popup").innerHTML = document.getElementById("emptyactivities").innerHTML;
            } else
            if(activities.length==0){ 

              document.getElementById("activity-value-label").innerHTML = document.getElementById("emptyactivities").innerHTML;
              document.getElementById("activity-value-label-popup").innerHTML = document.getElementById("emptyactivities").innerHTML;
             }

                else { 
      for(var i =0;i<activities.length;i++){
              acts.push(activities[i].activityId.replace(/-/g,' '));
              
            
      }

     

    



      $("#sel1").on("change",function(){
        
       

        cunter =-1;

        var sum=0;
        acts.forEach(element => {
          cunter++
          var currentprice = activities[cunter].activityprice* parseInt(document.getElementById("sel1").value); 
          document.getElementById(element.replace(/\s+/g, '-')+"#-p").innerHTML=  element + " - "+ currentprice +"$";
          sum  += currentprice;
        });
        document.getElementById("acts-total-value-label-popup").innerHTML = sum+"$";
      });

      var count2;
      $("#sel1_popup").on("change",function(){

        count2 =-1;

        var sum=0;
        acts.forEach(element => {
          count2++
          var currentprice = activities[count2].activityprice* parseInt(document.getElementById("sel1_popup").value); 
          document.getElementById(element.replace(/\s+/g, '-')+"#-p").innerHTML=  element + " - "+ currentprice +"$";
          sum  += currentprice;
        });
        document.getElementById("acts-total-value-label-popup").innerHTML = sum+"$";
      });
      
      var sum=0;

      acts.forEach(element => {
          counter++
          var currentprice = activities[counter].activityprice* parseInt(document.getElementById("sel1").value); 
          sum  += currentprice;
        $('#activity-value-label').append( " <div id="+element.replace(/\s+/g, '-')+"#> " + element +"<sup id=\"rem\" ><i class=\"fa fa-remove\" id="+element.replace(/\s+/g, '-')+"  aria-hidden=\"true\"\"  style=\"color:red; cursor:pointer;\"></i></sup> </div>" );
        $('#activity-value-label-popup').append( " <div id="+element.replace(/\s+/g, '-')+"#-p> " + element + " - "+ currentprice +"$" + " </div>" );

       });

       document.getElementById("acts-total-value-label-popup").innerHTML = sum+"$";

       var str = global.localStorage.getItem("activities");
        var allactivities=new Array();
         allactivities.sort();
                }
       $('.fa-remove').click(function(){
        
        
        str = global.localStorage.getItem("activities");
        allactivities=new Array();
        
           if(str){
               allactivities = JSON.parse(str);
           }
        
        if(includes(allactivities,this.id)){
          var index = -1
          for(i=0;i<allactivities.length;i++){
            if(allactivities[i].activityId==this.id)
              index = i;
          }
          allactivities.splice(index,1);
          acts.splice(index,1);
          activities.splice(index,1);
         
          global.localStorage.setItem("activities", JSON.stringify(allactivities));
     
          activate(this.id.replace(/-/g,' ')+" Removed");
          
          var currentElement  =  this.parentElement.parentElement.parentElement.parentElement;
                         
          $(currentElement).removeClass('hover');

          this.style.display = "none";
          var id = this.id+"#";
          var id1 = this.id+"#-p";
          
         document.getElementById(id).style.display = "none";
         document.getElementById(id1).style.display = "none";

         var sum=0;
         var cunt =-1;
         
        acts.forEach(element => {
          cunt++
          var currentprice = activities[cunt].activityprice* parseInt(document.getElementById("sel1").value); 
         
          document.getElementById(this.id.replace(/\s+/g, '-')+"#-p").innerHTML=  element + " - "+ currentprice +"$";
          sum += currentprice;
    
        });
        
        document.getElementById("acts-total-value-label-popup").innerHTML = sum+"$";
        
         

         if(allactivities.length==0){
          document.getElementById("activity-value-label").innerHTML = document.getElementById("emptyactivities").innerHTML;
          document.getElementById("activity-value-label-popup").innerHTML = document.getElementById("emptyactivities").innerHTML;
         }
          
         
        
            
         



      }

     

      function activate(name) {
        // Get the snackbar DIV
        var x = document.getElementById("snackbar");
      
        // Add the "show" class to DIV
        x.innerHTML=name;
      
        x.className = "show";
        // After 3 seconds, remove the show class from DIV
        setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
      }   
                
         });
     
         
            


          

}(window));



function includes(items,searchItem){
  var found = false;
for(var i = 0; i < items.length; i++) {
    if (items[i].activityId == searchItem) {
        found = true;
        break;
    }
}
return found
}

      });
