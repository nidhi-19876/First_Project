document.addEventListener("DOMContentLoaded", function(){

updateClock();

});

function updateClock(){

const clock=document.getElementById("clock");

if(clock){

setInterval(()=>{

const now=new Date();

clock.innerHTML="Current Time: "+now.toLocaleTimeString();

},1000);

}

}


/* ================= PARTICLES NETWORK ONLY HOMEPAGE ================= */

if(document.body.classList.contains("home-page")){

particlesJS("particles-js",{

particles:{
number:{value:80},
color:{value:"#00c3ff"},
shape:{type:"circle"},
opacity:{value:0.5},
size:{value:3},
line_linked:{
enable:true,
distance:150,
color:"#00c3ff"
},
move:{enable:true,speed:2}
}

});

}


/* ================= SEARCH FILTER ================= */

const searchInput=document.getElementById("searchInput");

if(searchInput){

searchInput.addEventListener("keyup",function(){

let filter=searchInput.value.toLowerCase();

let rows=document.querySelectorAll("#attendanceTable tr");

rows.forEach((row,index)=>{

if(index===0) return;

let text=row.textContent.toLowerCase();

row.style.display=text.includes(filter)?"":"none";

});

});

}


/* ================= ATTENDANCE CHART ================= */

const ctx=document.getElementById("attendanceChart");

if(ctx){

new Chart(ctx,{
type:"bar",
data:{
labels:["Present","Absent"],
datasets:[{
label:"Attendance Summary",
data:[10,2],
backgroundColor:["#00c3ff","#ff4d4d"]
}]
}
});

}