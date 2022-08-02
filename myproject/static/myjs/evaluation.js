function checkid() {
  let num=document.getElementById("currid");
  let rex1=/\d{7}/;
  if (!rex1.test(num.value)) {
      num.setCustomValidity("請輸入7位數字");
    } else {
      num.setCustomValidity("");
      window.location="/report"
    }
  
    
}
  
