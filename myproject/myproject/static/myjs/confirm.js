var submit=document.getElementById('sent');
function check() {
  if (confirm("確認表單內容","請確認內容送出將無法改")==true){ 
    window.location ="thankapply.html"
     
    }else{ 
    return false; 
    } 
};
submit.addEventListener("click",check);