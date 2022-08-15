// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
 
  let info_name = document.getElementById('fullName');
  let info_aday = document.getElementById('apply_day');
  let getinfo=document.getElementById("getinfo");
  getinfo.onclick=function() {
    document.getElementById('warning_id').style.display = 'none';
    document.getElementById('warning_already').style.display = 'none';
    sk_id = document.getElementById('currID').value;
    info_name.innerHTML = '';
    info_aday.innerHTML = '';
    // call flask route by ajax
    $.ajax({
        type : "POST",
        url : '/getinfo',
        data: {'skid':sk_id}
        }).done((datafromflask) => {
            console.log(datafromflask);
            if (Object.keys(datafromflask).length == 0){
              document.getElementById('warning_id').style.display = 'block';
            } else if (datafromflask['FINAL_CHECK'] == 1){
              document.getElementById('warning_already').style.display = 'block';
            } else {
              info_name.innerHTML = '&nbsp;&nbsp;' + datafromflask['NAME'];
              info_aday.innerHTML = '&nbsp;&nbsp;' + datafromflask['APPLY_DAY'];
            };            
        });
  };

  let resetbutton = document.getElementsByName("reset-all")[0];
  resetbutton.onclick=function(){
    document.getElementById('warning_id').style.display = 'none';
    document.getElementById('warning_already').style.display = 'none';
    info_name.innerHTML = '';
    info_aday.innerHTML = '';;
  };

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  var forms = document.querySelectorAll('.needs-validation')

  // Loop over them and prevent submission
  Array.prototype.slice.call(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }

        form.classList.add('was-validated')
      }, false)
    })
})()


