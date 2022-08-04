// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  document.getElementById('birth-day').value = "1990-01-01";
  var sameAddr1 = document.getElementById('same-address-1');
  sameAddr1.addEventListener('click', function(){
    if (this.checked){
      document.getElementById('address-contact-region').disabled = true;
      document.getElementById('address-contact-city').disabled = true;
      document.getElementById('address-contact-addr').disabled = true;
    } else {
      document.getElementById('address-contact-region').disabled = false;
      document.getElementById('address-contact-city').disabled = false;
      document.getElementById('address-contact-addr').disabled = false;
    }
  });

  var sameAddr2 = document.getElementById('same-address-2');
  sameAddr2.addEventListener('click', function(){
    if (this.checked){
      document.getElementById('address-work-region').disabled = true;
      document.getElementById('address-work-city').disabled = true;
      document.getElementById('address-work-addr').disabled = true;
    } else {
      document.getElementById('address-work-region').disabled = false;
      document.getElementById('address-work-city').disabled = false;
      document.getElementById('address-work-addr').disabled = false;
    }
  });

  var tcar1 = document.getElementById('tenure-care-yes');
  tcar1.addEventListener('click', function(){
    document.getElementById('tenure-care-date').disabled = false;
  });
  var tcar2 = document.getElementById('tenure-care-no');
  tcar2.addEventListener('click', function(){
    document.getElementById('tenure-care-date').disabled = true;
  });


  'use strict'
  
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


