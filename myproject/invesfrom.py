from flask import request
import datetime
from myproject import app, db, engine

def invesprocess(form):
    result1 = dict()
    result2 = dict()
    result1['SK_ID_CURR'] = form['currID']
    result1['HOUR_APPR_PROCESS_START_x'] = datetime.datetime.now().hour

    result1['DAYS_REGISTRATION'] = float(form['registchan-day'])*-1
    result1['DAYS_ID_PUBLISH'] = float(form["infocang-day"])*-1
    result1['DAYS_LAST_PHONE_CHANGE'] = float(form["phone-day"])*-1
    result1['OBS_60_CNT_SOCIAL_CIRCLE'] = float( form["OBSSOCIAL60"])
    result1['DEF_60_CNT_SOCIAL_CIRCLE'] = float(form["DEFSOCIAL60"])
    result1['AMT_REQ_CREDIT_BUREAU_MON'] = float(form["REQWeek"])
    result1['AMT_REQ_CREDIT_BUREAU_QRT'] = float(form["REQRT"])
    result1['AMT_REQ_CREDIT_BUREAU_YEAR'] = float(form["REQYear"])

    result1['NAME_TYPE_SUITE_Children'] = 0
    result1['NAME_TYPE_SUITE_Family'] = 0
    result1['NAME_TYPE_SUITE_Spouse, partner'] = 0
    result1['NAME_TYPE_SUITE_Unaccompanied'] = 0
    if form.get('suitetype') == '小孩': result1['NAME_TYPE_SUITE_Children'] = 1
    if form.get('suitetype') == '無人陪同': result1['NAME_TYPE_SUITE_Unaccompanied'] = 1
    if form.get('suitetype') == '父母': result1['NAME_TYPE_SUITE_Spouse, partner'] = 1
    if form.get('suitetype') == '其他家人': result1['NAME_TYPE_SUITE_Family'] = 1
    
    result2['SK_ID_CURR'] = form['currID']
    if form.get('firstapp') == None: 
        result2['DAYS_PERIOD_median'] = form.get("DAYS_PERIOD_median")
        result2['NAME_TYPE_SUITE'] = form.get("NAME_TYPE_SUITE")
        result2['HOUR_APPR_PROCESS_START_y'] = form.get("weekdayStart")
        result2['WEEKDAY_APPR_PROCESS_START'] = form.get("hour_apprstart")

        result2['CONTRACT_Cash_loans'] = 0
        result2['CONTRACT_Consumer_loans'] = 0
        result2['CONTRACT_Revolving_loans'] = 0
        if form.get('CONTRACT') == '現金貸款': result2['CONTRACT_Cash_loans'] = 1
        if form.get('CONTRACT') == '消費貸款': result2['CONTRACT_Consumer_loans'] = 1
        if form.get('CONTRACT') == '循環貸款': result2['CONTRACT_Revolving_loans'] = 1
        result2['YIELD_high'] = 0
        result2['YIELD_low'] = 0
        result2['YIELD_middle'] = 0
        if form.get('CONTRACT') == '低': result2['YIELD_low'] = 1
        if form.get('CONTRACT') == '中': result2['YIELD_middle'] = 1
        if form.get('CONTRACT') == '高': result2['YIELD_high'] = 1

        result2['DAYS_DECISION_median'] = form.get("DAYS_DECISION_median")
        result2['CNT_PAYMENT_median'] = form.get("CNT_PAYMENT_median")
        result2['PREV_APPLICATION_max'] = form.get("PREV_APPLICATION_max")
        result2['PREV_ANNUITY_median'] = form.get("PREV_ANNUITY_median")
        result2['PREV_CREDIT_max'] = form.get("PREV_CREDIT_max")
        result2['PREV_CREDIT_sum'] = form.get("PREV_CREDIT_sum")
        result2['PREV_CRE/APP_max'] = form.get("creappmax")
        result2['PREV_DOWN_PAYMENT_median'] = form.get("PREV_DOWN_PAYMENT_median")
        result2['RATE_DOWN_PAYMENT_median'] = form.get("RATE_DOWN_PAYMENT_median")
        result2['PORTFOLIO_Cash'] = form.get("PORTFOLIO_Cash")
        result2['Cash through the bank'] = form.get("cashBank")
        result2['Non-cash from your account'] = form.get("accountpay")
        result2['PREV_GOODS_PRICE_max'] = form.get("PREV_GOODS_PRICE_max")

    nk=0
    for k in list(result2.keys()):
        if result2.get(k)=='': nk += 1

    if nk > 3:
        result2 = dict()
    return result1, result2


def inveswritesql(data1,data2):
    skid = data1['SK_ID_CURR']
    skid = int(skid)
    data1.pop('SK_ID_CURR', 3000)

    conn=engine.connect()
    ## 從temp調出資料
    query1 = f"SELECT * FROM temp WHERE SK_ID_CURR='{skid}';"
    proxy1 = conn.execute(query1)
    tempdata = proxy1.fetchall()
    datatemp = [i for i in tempdata[0]]
    ## 選取所有欄位名
    query2 = f"select column_name from INFORMATION_SCHEMA.COLUMNS where table_name='temp' ORDER BY ordinal_position;"
    proxy2 = conn.execute(query2)
    colname = proxy2.fetchall()
    colname = [i[0] for i in colname]
    result1 = dict(list(zip(colname,datatemp)))
    ## 刪除不會存入application的欄位
    [result1.pop(key) for key in ['NAME', 'APPLY_DAY', 'FINAL_CHECK', 'AMT_CREDIT']]

    ## 合併 輸入applications的資料
    data = {**result1, **data1}
    colword,valword = setsqlstring(data)
    ## 寫入資料到applications
    query1 = f"INSERT INTO applications ({colword}) VALUES ({valword});"
    proxy1 = conn.execute(query1)
    ## 將temp中該筆資料設為已存入資料庫
    query1 = f"UPDATE temp SET FINAL_CHECK=1 WHERE SK_ID_CURR='{skid}';"
    proxy1 = conn.execute(query1)

    ## 如果有給 data_prev的資料, 寫入data_prev
    if len(data2) > 2:
        colword,valword = setsqlstring(data2)
        query2 = f"INSERT INTO database_prev ({colword}) VALUES ({valword});"
        proxy2 = conn.execute(query2)

    conn.close()


def setsqlstring(inputdata):
    colword=''
    valword=''
    for k,v in inputdata.items():
        colword = colword + '`' + str(k) + '`,'
        if isinstance(v, str):
            valword = valword + "'" + v + "',"
        else:
            valword = valword + str(v) + ","
    colword = colword[:-1]
    valword = valword[:-1]
    return colword,valword 
