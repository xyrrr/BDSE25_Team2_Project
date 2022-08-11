// Example starter JavaScript for disabling form submissions if there are invalid fields
(function () {
  document.getElementById('birth-day').value = "1990-01-01";
  
  var address00 = document.getElementById('address-main-region');
  address00.addEventListener('change', function(){
    if (address00.value == "台灣") {
      document.getElementById('address-main-contral-1').style.display = 'block';
      document.getElementById('address-main-city1').disabled = false;
      document.getElementById('address-main-city1').required = true;
      document.getElementById('address-main-contral-2').style.display = 'none';
      document.getElementById('address-main-city2').disabled = true;
      document.getElementById('address-main-city2').required = false;
    } else if (address00.value == "東南亞") {
      document.getElementById('address-main-contral-1').style.display = 'none';
      document.getElementById('address-main-city1').disabled = true;
      document.getElementById('address-main-city1').required = false;
      document.getElementById('address-main-contral-2').style.display = 'block';
      document.getElementById('address-main-city2').disabled = false;
      document.getElementById('address-main-city2').required = true;
    };
  });

  var address01 = document.getElementById('address-contact-region');
  address01.addEventListener('change', function(){
    if (address01.value == "台灣") {
      document.getElementById('address-contact-contral-1').style.display = 'block';
      document.getElementById('address-contact-city1').disabled = false;
      document.getElementById('address-contact-city1').required = true;
      document.getElementById('address-contact-contral-2').style.display = 'none';
      document.getElementById('address-contact-city2').disabled = true;
      document.getElementById('address-contact-city2').required = false;
    } else if (address01.value == "東南亞") {
      document.getElementById('address-contact-contral-1').style.display = 'none';
      document.getElementById('address-contact-city1').disabled = true;
      document.getElementById('address-contact-city1').required = false;
      document.getElementById('address-contact-contral-2').style.display = 'block';
      document.getElementById('address-contact-city2').disabled = false;
      document.getElementById('address-contact-city2').required = true;
    };
  });
  var sameAddr1 = document.getElementById('same-address-1');
  sameAddr1.addEventListener('change', function(){
    if (this.checked){
      document.getElementById('address-contact-region').disabled = true;
      document.getElementById('address-contact-city1').disabled = true;
      document.getElementById('address-contact-city2').disabled = true;
      document.getElementById('address-contact-addr').disabled = true;
    } else {
      document.getElementById('address-contact-region').disabled = false;
      document.getElementById('address-contact-city1').disabled = false;
      document.getElementById('address-contact-city2').disabled = false;
      document.getElementById('address-contact-addr').disabled = false;
    }
  });
  var sameAddr11 = document.getElementById('same-address-11');
  sameAddr11.addEventListener('change', function(){
    if (this.checked){
      document.getElementById('address-contact-region').disabled = true;
      document.getElementById('address-contact-city1').disabled = true;
      document.getElementById('address-contact-city2').disabled = true;
      document.getElementById('address-contact-addr').disabled = true;
    } else {
      document.getElementById('address-contact-region').disabled = false;
      document.getElementById('address-contact-city1').disabled = false;
      document.getElementById('address-contact-city2').disabled = false;
      document.getElementById('address-contact-addr').disabled = false;
    }
  });

  var address02 = document.getElementById('address-work-region');
  address02.addEventListener('change', function(){
    if (address02.value == "台灣") {
      document.getElementById('address-work-contral-1').style.display = 'block';
      document.getElementById('address-work-city1').disabled = false;
      document.getElementById('address-work-city1').required = true;
      document.getElementById('address-work-contral-2').style.display = 'none';
      document.getElementById('address-work-city2').disabled = true;
      document.getElementById('address-work-city2').required = false;
    } else if (address02.value == "東南亞") {
      document.getElementById('address-work-contral-1').style.display = 'none';
      document.getElementById('address-work-city1').disabled = true;
      document.getElementById('address-work-city1').required = false;
      document.getElementById('address-work-contral-2').style.display = 'block';
      document.getElementById('address-work-city2').disabled = false;
      document.getElementById('address-work-city2').required = true;
    };
  });
  var sameAddr2 = document.getElementById('same-address-2');
  sameAddr2.addEventListener('change', function(){
    if (this.checked){
      document.getElementById('address-work-region').disabled = true;
      document.getElementById('address-work-city1').disabled = true;
      document.getElementById('address-work-city2').disabled = true;
      document.getElementById('address-work-addr').disabled = true;
    } else {
      document.getElementById('address-work-region').disabled = false;
      document.getElementById('address-work-city1').disabled = false;
      document.getElementById('address-work-city2').disabled = false;
      document.getElementById('address-work-addr').disabled = false;
    }
  });
  var sameAddr22 = document.getElementById('same-address-22');
  sameAddr22.addEventListener('change', function(){
    if (this.checked){
      document.getElementById('address-work-region').disabled = true;
      document.getElementById('address-work-city1').disabled = true;
      document.getElementById('address-work-city2').disabled = true;
      document.getElementById('address-work-addr').disabled = true;
    } else {
      document.getElementById('address-work-region').disabled = false;
      document.getElementById('address-work-city1').disabled = false;
      document.getElementById('address-work-city2').disabled = false;
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


