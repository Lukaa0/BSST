(function (global) {


class Activities{
  constructor(communityName,activityId,activityprice){
    this.communityName = communityName;
    this.activityId = activityId;
    this.activityprice = activityprice;
  }
 
}

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


    var str = global.localStorage.getItem("activities");
    var activities = JSON.parse(str);
    checkaActive();
    

    $(".favme").on('click', function(event){
      var  splitter1 = document.getElementById(this.id+"-price").innerHTML.split(':');
      
      var activityprice =  parseInt(splitter1[1]);

    

     

        var communityName = $(".com-name").attr("id");
         str = global.localStorage.getItem("activities");
         allactivities = new Array();

            if(str){
                allactivities = JSON.parse(str);
                
              
            }
            if(!includes(allactivities,this.id)){
                allactivities.push(new Activities(communityName,this.id,activityprice))
                global.localStorage.setItem("activities", JSON.stringify(allactivities));
                activate(this.id+" Added");
                
              
              // getcurrentelement
            var currentElement  =  this.parentElement.parentElement.parentElement.parentElement;
                               
            $(currentElement).addClass('hover');

                    }
            else if (includes(allactivities,this.id)){
                var index = -1
                for(i=0;i<allactivities.length;i++){
                  if(allactivities[i].activityId==this.id)
                    index = i;
                }
                
                allactivities.splice(index,1);
                global.localStorage.setItem("activities", JSON.stringify(allactivities));
           
                activate(this.id+" Removed");
                
                var currentElement  =  this.parentElement.parentElement.parentElement.parentElement;
                               
                $(currentElement).removeClass('hover');



            }
        })

       
        
        
        function activate(name) {
            // Get the snackbar DIV
            var x = document.getElementById("snackbar");
          
            // Add the "show" class to DIV
            x.innerHTML=name;

            x.className = "show";
            // After 3 seconds, remove the show class from DIV
            setTimeout(function(){ x.className = x.className.replace("show", ""); }, 3000);
          }


          //the func to check active activities
          function checkaActive(){

            
            if(activities!=null){
          

             str = global.localStorage.getItem("activities");
            

             for(var i =0;i<activities.length;i++){
                
              var id =  document.getElementById(activities[i].activityId);
              if(id!=null){
                 $(id).addClass('active'); 
                 
                  currentElement  =  id.parentElement.parentElement.parentElement.parentElement;
                               
                 $(currentElement).addClass('hover');
              }
            }
          }
           
                
            
         }
    
}(window));

