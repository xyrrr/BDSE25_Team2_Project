$('form').on('submit',function check(e) {
  if (confirm("請確認內容送出將無法改")==true){ 
        return true;
    }else{ 
      e.preventDefault();
    } 
});
