let thisdemo = document.getElementById('demo');
thisdemo.addEventListener("click", clickdemo);

function clickdemo() {
    document.getElementById('lastName').value="郭";
    document.getElementById('firstName').value="興";
    document.getElementById('gender-male').checked=true;
    document.getElementById('birth-day').value = "1991-06-04"

    let e=document.getElementById('education');
    let n=Math.floor(Math.random()*e.options.length);
    e.value=e.options[n].innerHTML;

    document.getElementById('family-type').value="未婚";
    document.getElementById('family-member').value="2";
    document.getElementById('family-child').value="0";
    document.getElementById('phone-home').value="03-2547895";
    document.getElementById('phone-mobile').value="0911-345789";
    document.getElementById('email').value="ispan@example.com";
    document.getElementById('address-main-region').value="台灣";
    document.getElementById('address-main-city').value="桃園市";
    document.getElementById('address-main-addr').value="中壢區新生路二段421號";
    document.getElementById('same-address-1').checked=true;
    document.getElementById('address-contact-region').disabled = true;
    document.getElementById('address-contact-city').disabled = true;
    document.getElementById('address-contact-addr').disabled = true;
    document.getElementById('housetype').value="公寓(Municipal)";

    document.getElementById('same-address-1').checked=true;
    document.getElementById('address-work-region').disabled = true;
    document.getElementById('address-work-city').disabled = true;
    document.getElementById('address-work-addr').disabled = true;
    document.getElementById('phone-work').value="0919183521";
    document.getElementById('income-type').value="工作";
    document.getElementById('profession-type').value="醫事人員";
    document.getElementById('profession-org').value="自雇";
    document.getElementById('profession-date').value="2019-11-11";
    document.getElementById('annaulincome').value="1100000";
    document.getElementById('tenure-care-yes').checked=true;
    document.getElementById('tenure-care-date').disabled = false;
    document.getElementById('tenure-care-date').value="2028-12-25";
    document.getElementById('tenure-house-yes').checked=true;

    n=Math.floor(Math.random()*2);
    document.getElementById('apply-type2').checked=true;
    n=(Math.ceil(Math.random()*800)+8)*500;
    document.getElementById('apply-amount').value=n.toString();
    document.getElementById('pravic').checked=true;
};