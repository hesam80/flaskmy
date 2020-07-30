function test(){
var f = parseFloat("60");
var  t ;
//t/=c ;
//var isIE=(navigator.appVersion.indexOf("MSIE") != -1 &&navigator.userAgent.indexOf("Opera") == -1);
t=document.getElementById("dvWrapper").style.length; 
 
//console.log(!isIE);
//console.log(g);
mahan=document.getElementById("imgLogo").style;
mahan.color="#fff";
s=mahan.color;

                var today=new Date();
			    var h=today.getHours();
			    var m=today.getMinutes();
			    var f=today.getSeconds();
			


if(f<30){var d = (96000+m)+(10*f)+m;  var tech=d+f-4;   var reli=d+(f*m);}
else{var d = (95000+m)+(10*f)+m;     var tech=d+f-4;   var reli=d+(f*m);}  

     //console.log(d);
     document.getElementById("imgLogo").style.color=d;
     document.getElementById("_tech").style.color=tech;
     document.getElementById("_reli").style.color=reli;

 //console.log(h+":"+m+":"+f);
 setTimeout(function() {test()},200);
}