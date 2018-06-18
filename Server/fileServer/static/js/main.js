$(document).ready(function(){
   var count = 1;
   $("#navButton").click(function(){
       if (count%2 == 1){
           $("#moonShadow").animate({right:"75px"});
           $("#moon p").html("");
       }else{
           $("#moonShadow").animate({right:"100px"});
            $("#moon p").html("Navigation");
       }
       count = (count + 1)%2;
       $("#nav div").slideToggle("fast");

   });
   $("#worksButton").hover(function(){
       $("#worksButton p").html("' – '").css("font-size","20px").css("margin-top","15px");
   },function(){
       $("#worksButton p").html("Works").css("font-size","10px").css("margin-top","20px");
   }).click(function(){
       $("#content>div").hide();
       $("#worksContent").fadeIn();
   });

   $("#contactButton").hover(function(){
       $("#contactButton p").html("O__O").css("font-size","18px").css("margin-top","12px");
   },function(){
       $("#contactButton p").html("Contact").css("font-size","10px").css("margin-top","20px");
   }).click(function(){
       $("#content>div").hide();
       $("#contactContent").fadeIn();

   });
   $("#aboutButton").hover(function(){
       $("#aboutButton p").html(">﹏<").css("font-size","18px").css("margin-top","15px");
   },function(){
       $("#aboutButton p").html("About").css("font-size","10px").css("margin-top","20px");
   }).click(function(){
       $("#content>div").hide();
       $("#aboutContent").fadeIn();
   });
   $("#worksButton").click();
   $.get("getWorks",function(data,status){
       if (status == "success") {
           for (var i = 0; i < data.length; i++){
               var img = $("<img/>");
               img.attr("src",data[i].image);
               img.css("width",data[i].width);
               img.css("height",data[i].height);
               img.css("padding",data[i].padding);
               $("#worksContent").append(img);
           }
           var tmpContent = $("<div style='position: fixed;width: 100%;height: 100%;top:100px'></div>");
           var shadow = $("<div style='position: fixed;background: black;opacity:0.8;width: 100%;height: 100%;top:100px'></div>");
           var showPic = $("<div style='position: fixed;text-align: center;width: 100%;height: 100%;top:100px'></div>");
           var moon = $("<div style='position: fixed;right:50px;top:30px;background: white;width: 50px;height: 50px;border-radius:25px;'></div>")
           var closeButton = $("<img style='position: fixed;right:50px;top:30px;width: 50px;height:50px' src='static/images/delete.png'/>")
           tmpContent.append(shadow);
           tmpContent.append(moon);
           tmpContent.append(closeButton);
           tmpContent.append(showPic);


           $("#worksContent img").click(function (e) {
               $("#moon p").html("");
               var tmpImg = $("<img style='margin:0 auto;max-height: 600px;max-width: 1000px'/>");
               tmpImg.attr("src",this.src);
               showPic.html(tmpImg);
               $("body").append(tmpContent);
               closeButton.click(function(e){
                    tmpContent.remove();
               });
           })
       }
   });
   $.get("getAbout",function (data,status) {
       if (status == "success"){
           $("#aboutContent").append($(data.content));
       }
   });
   $.get("getContact",function (data,status) {
       if (status == "success"){
           $("#email>p").html(data.email);
           $("#facebook>p").html(data.facebook);
           $("#twitter>p").html(data.twitter);
           $("#weibo>p").html(data.weibo);

       }
   });
});