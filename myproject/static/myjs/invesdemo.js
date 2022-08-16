let invesdemo=document.getElementById("demo");

invesdemo.onclick=function invesDemo() {
    if (Math.floor(Math.random()*10) < 8){
        document.getElementById('emergrncy-no').checked=true;
    } else {
        document.getElementById('emergency-yes').checked=true;
    };

    document.getElementById('registchan-day').value = Math.floor(Math.random()*10000);
    document.getElementById('infocang-day').value = Math.floor(Math.random()*3000);
    document.getElementById('phone-day').value = Math.floor(Math.random()*1500);

    let n=Math.ceil(Math.random()*5);
    document.getElementById('OBSSOCIAL60').value=n;
    document.getElementById('DEFSOCIAL60').value=Math.floor(Math.random()*n);
  
    n=Math.ceil(Math.random()*10);
    if (n<9){
        document.getElementById('REQWeek').value=0;
        document.getElementById('REQMon').value=0;
        document.getElementById('REQRT').value=0
    }else{
        let n1=Math.floor(Math.random()*10);
        document.getElementById('REQMon').value=n1;
        let n2=Math.floor(Math.random()*n1);
        document.getElementById('REQWeek').value=n2;
        document.getElementById('REQRT').value=n1 + Math.floor(Math.random()*3)
    };
    n = Math.ceil(Math.random()*4) + document.getElementById('REQRT').value
    document.getElementById('REQYear').value=n;

    let e=document.getElementById('suitetype');
    n=Math.ceil(Math.random()*(e.options.length-1));
    e.value=e.options[n].innerHTML;
 
    document.getElementById('accountamt').value = Math.ceil(Math.random()*50000)*100;
    document.getElementById('cardavg').value = Math.ceil(Math.random()*50000)*100;

    let test=Math.ceil(Math.random()*10);
    if (test <=5){
        document.getElementById('DAYS_PERIOD_median').value=Math.random()*2000;
        if (Math.random()<=0.8){
            document.getElementById('NAME_TYPE_SUITE').value = 0;
        } else {
            document.getElementById('NAME_TYPE_SUITE').value = 1;
        };
        document.getElementById('weekdayStart').value=Math.ceil(Math.random()*7);
        document.getElementById('hour_apprstart').value=Math.floor(Math.random()*23);
        
        e=document.getElementById('CONTRACT');
        n=Math.ceil(Math.random()*(e.options.length-1));
        e.value=e.options[n].innerHTML;
        e=document.getElementById('yieldhigh');
        n=Math.ceil(Math.random()*(e.options.length-1));
        e.value=e.options[n].innerHTML;

        document.getElementById('DAYS_DECISION_median').value=Math.ceil(Math.random()*2921)+1;
        document.getElementById('CNT_PAYMENT_median').value=Math.floor(Math.random()*60);

        let n1 = Math.ceil(Math.random()*10000)*100;
        document.getElementById('PREV_APPLICATION_max').value=n1;
        let n2 = Math.ceil(Math.random()*30000)*10;
        document.getElementById('PREV_ANNUITY_median').value=n2;
        document.getElementById('PREV_CREDIT_max').value=Math.ceil(Math.random()*n1/100)*100;
        document.getElementById('PREV_CREDIT_sum').value=Math.ceil(Math.random()*n1/100)+n1;

        document.getElementById('creappmax').value=Math.random()*10;
        document.getElementById('PREV_DOWN_PAYMENT_median').value=Math.ceil(Math.random()*8000)*100;
        document.getElementById('RATE_DOWN_PAYMENT_median').value=Math.random();
        document.getElementById('PORTFOLIO_Cash').value=Math.random();

        document.getElementById('cashBank').value=Math.random();
        document.getElementById('accountpay').value=Math.random()*(1-document.getElementById('cashBank').value);
        document.getElementById('PREV_GOODS_PRICE_max').value=Math.ceil(Math.random()*8000)*100;
    }else{
        document.getElementById('DAYS_PERIOD_median').value='';
        document.getElementById('NAME_TYPE_SUITE').value='';
        document.getElementById('weekdayStart').value='';
        document.getElementById('hour_apprstart').value='';
        document.getElementById('DAYS_DECISION_median').value='';
        document.getElementById('CNT_PAYMENT_median').value='';
        document.getElementById('PREV_APPLICATION_max').value='';
        document.getElementById('PREV_ANNUITY_median').value='';
        document.getElementById('PREV_CREDIT_max').value='';
        document.getElementById('PREV_CREDIT_sum').value='';
        document.getElementById('creappmax').value='';
        document.getElementById('PREV_DOWN_PAYMENT_median').value='';
        document.getElementById('RATE_DOWN_PAYMENT_median').value='';
        document.getElementById('PORTFOLIO_Cash').value='';
        document.getElementById('cashBank').value='';
        document.getElementById('accountpay').value='';
        document.getElementById('PREV_GOODS_PRICE_max').value='';
    };
};

