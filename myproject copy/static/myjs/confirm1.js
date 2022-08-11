var submit=document.getElementById('sent');
function check() {
  if (confirm("確認表單內容,送出將無法改")==true){ 
    return true;
    }else{ 
    return false; 
    } 
};
submit.addEventListener("click",check);