let thisdemo = document.getElementById('demo');
thisdemo.addEventListener("click", clickdemo);

function clickdemo() {
    document.getElementById('lastName').value="郭";
    document.getElementById('firstName').value="興";
    if (Math.floor(Math.random()*10) < 6){
        document.getElementById('gender-male').checked=true;
    } else {
        document.getElementById('gender-female').checked=true;
    };

    function randomDate(start, end) {
        let randate = new Date(start.getTime() + Math.random() * (end.getTime() - start.getTime()));
        randate = randate.toISOString().substring(0, 10);
        return randate
    };
    let d = randomDate(new Date(1950, 0, 1), new Date(2004, 0, 1));
    document.getElementById('birth-day').value = d

    let e=document.getElementById('education');
    let n=Math.ceil(Math.random()*(e.options.length-1));
    e.value=e.options[n].innerHTML;

    e=document.getElementById('family-type');
    n=Math.ceil(Math.random()*(e.options.length-1));
    e.value=e.options[n].innerHTML;
    document.getElementById('family-member').value=Math.ceil(Math.random()*4);
    document.getElementById('family-child').value=Math.floor(Math.random()*3);
    if (Math.floor(Math.random()*10) < 8){
        document.getElementById('phone-home').value="03-2547895";
    } else {
        document.getElementById('phone-home').value="";
    };
    if (Math.floor(Math.random()*10) < 9){
        document.getElementById('phone-mobile').value="0911-345789";
    } else {
        document.getElementById('phone-mobile').value="";
    };
    if (Math.floor(Math.random()*10) < 9){
        document.getElementById('email').value="ispan@example.com";
    } else {
        document.getElementById('email').value="";
    };

    document.getElementById('address-main-region').value="台灣";
    e=document.getElementById('address-main-city1');
    n=Math.ceil(Math.random()*(e.options.length-1));
    e.value=e.options[n].innerHTML;
    document.getElementById('address-main-addr').value="中山路121號";
    document.getElementById('address-contact-region').value="台灣";
    if (Math.floor(Math.random()*10) < 8){
        document.getElementById('address-contact-city1').value = e.value;
    } else {
        document.getElementById('address-contact-city1').value="台北市";
    };
    e=document.getElementById('housetype');
    n=Math.ceil(Math.random()*(e.options.length-1));
    e.value=e.options[n].innerHTML;

    document.getElementById('address-work-region').value="台灣";
    if (Math.floor(Math.random()*10) < 8){
        document.getElementById('address-work-city1').value = document.getElementById('address-contact-city1').value;
    } else {
        document.getElementById('address-work-city1').value="台北市";
    };
    if (Math.floor(Math.random()*10) < 8){
        document.getElementById('phone-work').value="0919183521";
    } else {
        document.getElementById('phone-work').value="";
    };
    
    if (Math.floor(Math.random()*20) < 19){
        document.getElementById('income-type').value="工作";
        e=document.getElementById('profession-type');
        e.value=e.options[Math.ceil(Math.random()*(e.options.length-1))].innerHTML;
        e=document.getElementById('profession-org');
        e.value=e.options[Math.ceil(Math.random()*(e.options.length-1))].innerHTML;
    } else {
        e=document.getElementById('income-type');
        n=Math.ceil(Math.random()*(e.options.length-2));
        e.value=e.options[n].innerHTML;
        document.getElementById('profession-type').value="醫事人員";
        document.getElementById('profession-org').value="自雇";
    };
    d = randomDate(new Date(1980, 0, 1), new Date());
    document.getElementById('profession-date').value=d;
    n=(Math.ceil(Math.random()*100000))*100+25650;
    document.getElementById('annaulincome').value=n.toString();
    document.getElementById('annaulincome').value="1100000";
    if (Math.random() < 0.66){
        document.getElementById('tenure-care-yes').checked=true;
        document.getElementById('tenure-care-date').disabled = false;
        document.getElementById('tenure-care-date').value="2028-12-25";
    } else {
        document.getElementById('tenure-care-no').checked=true;
        document.getElementById('tenure-care-date').disabled = true;
    };
    if (Math.random() < 0.7){
        document.getElementById('tenure-house-yes').checked=true;
    } else {
        document.getElementById('tenure-house-no').checked=true;
    };

    if (Math.random() < 0.91){
        document.getElementById('apply-type1').checked=true;
    } else {
        document.getElementById('apply-type2').checked=true;
    };
    n=(Math.ceil(Math.random()*800)+8)*500;
    document.getElementById('apply-amount').value=n.toString();
    document.getElementById('pravic').checked=true;
};