function checkid() {
  let num=document.getElementById("currid");
  let rex1=/\d/;
  if (!rex1.test(num.value)) {
      num.setCustomValidity("請輸入數字");
    } else {
      num.setCustomValidity("");
      window.location="/report"
    }
  
    
}
  
