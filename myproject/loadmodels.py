import joblib
import numpy as np
import pandas as pd
from myproject import app, db, engine
from pathlib import Path

def load_date(skid):
    conn=engine.connect()
    query = f"SELECT SK_ID_CURR, CODE_GENDER_M, NAME_EDUCATION_TYPE,\
        DAYS_BIRTH, DAYS_EMPLOYED , DAYS_ID_PUBLISH, OBS_60_CNT_SOCIAL_CIRCLE, DEF_60_CNT_SOCIAL_CIRCLE,\
        DAYS_LAST_PHONE_CHANGE, AMT_REQ_CREDIT_BUREAU_YEAR, `NAME_CONTRACT_TYPE_Cash loans`,\
        `NAME_CONTRACT_TYPE_Revolving loans`, AMT_INCOME_TOTAL, DAYS_REGISTRATION, CNT_FAM_MEMBERS,\
        HOUR_APPR_PROCESS_START_x FROM applications WHERE SK_ID_CURR='{skid}';"
    proxy = conn.execute(query)
    table1 = proxy.fetchall()
    colname1 = ['SK_ID_CURR', 'CODE_GENDER_M', 'NAME_EDUCATION_TYPE',
        'DAYS_BIRTH', 'DAYS_EMPLOYED' , 'DAYS_ID_PUBLISH', 'OBS_60_CNT_SOCIAL_CIRCLE', 'DEF_60_CNT_SOCIAL_CIRCLE',
        'DAYS_LAST_PHONE_CHANGE', 'AMT_REQ_CREDIT_BUREAU_YEAR', 'NAME_CONTRACT_TYPE_Cash loans',
        'NAME_CONTRACT_TYPE_Revolving loans', 'AMT_INCOME_TOTAL', 'DAYS_REGISTRATION', 'CNT_FAM_MEMBERS',
        'HOUR_APPR_PROCESS_START_x']
    if table1 != []:
        df1 = pd.DataFrame(table1,columns=colname1)
    else:
        df1 = pd.DataFrame()
    
    query = f" SELECT SK_ID_CURR, PREV_ANNUITY_median, PREV_APPLICATION_max, PREV_CREDIT_max, \
        PREV_CREDIT_sum, DAYS_DECISION_median, CONTRACT_Cash_loans, CONTRACT_Consumer_loans, \
        PORTFOLIO_Cash, YIELD_high, YIELD_low, YIELD_middle, RATE_DOWN_PAYMENT_median, CNT_PAYMENT_median, \
        DAYS_PERIOD_median, HOUR_APPR_PROCESS_START_y, WEEKDAY_APPR_PROCESS_START, `Cash through the bank`, \
         `PREV_CRE/APP_max` FROM database_prev WHERE SK_ID_CURR='{skid}';"
    proxy = conn.execute(query)
    table2 = proxy.fetchall()
    colname2 = ['SK_ID_CURR', 'PREV_ANNUITY_median','PREV_APPLICATION_max','PREV_CREDIT_max',
        'PREV_CREDIT_sum','DAYS_DECISION_median','CONTRACT_Cash_loans','CONTRACT_Consumer_loans',
        'PORTFOLIO_Cash','YIELD_high', 'YIELD_low', 'YIELD_middle','RATE_DOWN_PAYMENT_median','CNT_PAYMENT_median',
        'DAYS_PERIOD_median', 'HOUR_APPR_PROCESS_START_y','WEEKDAY_APPR_PROCESS_START','Cash through the bank',
        'PREV_CRE/APP_max']
    if table2 != []:
        df2 = pd.DataFrame(table2,columns=colname2)
    else:
        df2 = pd.DataFrame()
    conn.close()
    return df1,df2

def info_date(data):
    result = dict()
    if data['CODE_GENDER_M'][0] == 1:
        result['gender'] = '男'
    else:
        result['gender'] = '女'
    result['age'] = int(np.round_((data['DAYS_BIRTH'][0])/(-365.25)))

    result['education'] = ''
    if (data['NAME_EDUCATION_TYPE'][0] == 0): 
        result['education'] = '國中'
    if (data['NAME_EDUCATION_TYPE'][0] == 1): 
        result['education'] = '高中'
    if (data['NAME_EDUCATION_TYPE'][0] == 2): 
        result['education'] = '大學肆業'
    if (data['NAME_EDUCATION_TYPE'][0] == 3): 
        result['education'] = '大學'
    if (data['NAME_EDUCATION_TYPE'][0] == 4): 
        result['education'] = '研究所'

    result['income'] = data['AMT_INCOME_TOTAL'][0]
    result['contract'] = '' 
    if data['NAME_CONTRACT_TYPE_Cash loans'][0] == 1:
        result['contract'] = '現金貸款'
    else:
        result['contract'] = '循環貸款'
    return result

def risk_index(indexlist):
    risk_ind = dict()
    risk_ind['R11'] = '低'
    risk_ind['R12'] = '低'
    risk_ind['R21'] = '--'
    risk_ind['R22'] = '--'
    risk_ind['R31'] = '--'
    risk_ind['R32'] = '--'
    risk_ind['C11'] = 'color:blue'
    risk_ind['C12'] = 'color:blue'
    risk_ind['C21'] = 'color:black'
    risk_ind['C22'] = 'color:black'
    risk_ind['C31'] = 'color:black'
    risk_ind['C32'] = 'color:black'
    if indexlist[0] == 1: 
        risk_ind['R11'] = '高'
        risk_ind['C11'] = 'color:red'
    if indexlist[1] == 1: 
        risk_ind['R12'] = '高'
        risk_ind['C12'] = 'color:red'

    if len(indexlist) == 6:
        risk_ind['R21'] = '低'
        risk_ind['R22'] = '低'
        risk_ind['R31'] = '低'
        risk_ind['R32'] = '低'
        risk_ind['C21'] = 'color:blue'
        risk_ind['C22'] = 'color:blue'
        risk_ind['C31'] = 'color:blue'
        risk_ind['C32'] = 'color:blue'
        if indexlist[2] == 1: 
            risk_ind['R21'] = '高'
            risk_ind['C21'] = 'color:red'
        if indexlist[3] == 1: 
            risk_ind['R22'] = '高'
            risk_ind['C22'] = 'color:red'
        if indexlist[4] == 1: 
            risk_ind['R31'] = '高' 
            risk_ind['C31'] = 'color:red'   
        if indexlist[5] == 1: 
            risk_ind['R32'] = '高'
            risk_ind['C32'] = 'color:red'
    return risk_ind
    

## data must be a dataframe
def main_simple_predict(data):
    dt = data[['NAME_EDUCATION_TYPE', 'DAYS_BIRTH', 'DAYS_EMPLOYED', 'DAYS_ID_PUBLISH','OBS_60_CNT_SOCIAL_CIRCLE', 'DEF_60_CNT_SOCIAL_CIRCLE',
       'DAYS_LAST_PHONE_CHANGE', 'AMT_REQ_CREDIT_BUREAU_YEAR','NAME_CONTRACT_TYPE_Cash loans', 'NAME_CONTRACT_TYPE_Revolving loans']]
    f = "myproject/static/models/RF_main.pkl"
    model = joblib.load(f)
    return model.predict(dt)[0]

def main_loans_predict(data):
    dt = data[['AMT_INCOME_TOTAL', 'DAYS_BIRTH', 'DAYS_EMPLOYED', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH', 'HOUR_APPR_PROCESS_START_x','OBS_60_CNT_SOCIAL_CIRCLE', 'DAYS_LAST_PHONE_CHANGE','AMT_REQ_CREDIT_BUREAU_YEAR']]
    f = "myproject/static/models/main_randomforest_ml"
    model = joblib.load(f)
    return model.predict(dt)[0]

def prev_simple_predict(data):
    dt = data[['PREV_CREDIT_sum', 'PREV_CRE/APP_max', 'DAYS_DECISION_median','DAYS_PERIOD_median', 'CONTRACT_Cash_loans', 'CONTRACT_Consumer_loans','PORTFOLIO_Cash', 'YIELD_high', 'YIELD_low', 'YIELD_middle']]
    f = "myproject/static/models/xgboostModel_all_prev.pkl"
    model = joblib.load(f)
    return model.predict(dt)[0]

def prev_loans_predict(data):
    dt = data[['PREV_ANNUITY_median', 'PREV_CREDIT_sum', 'RATE_DOWN_PAYMENT_median', 'DAYS_DECISION_median', 'CNT_PAYMENT_median', 'DAYS_PERIOD_median', 'YIELD_high', 'HOUR_APPR_PROCESS_START_y', 'WEEKDAY_APPR_PROCESS_START', 'Cash through the bank']]
    f = "myproject/static/models/prev_randomforest_ml2"
    model = joblib.load(f)
    return model.predict(dt)[0]

def mixed_simple_predict(data):
    dt = data[['DAYS_BIRTH', 'DAYS_EMPLOYED', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH','DAYS_LAST_PHONE_CHANGE', 'PREV_ANNUITY_median', 'PREV_CREDIT_max','PREV_CREDIT_sum', 'PREV_CRE/APP_max', 'DAYS_DECISION_median']]
    f = "myproject/static/models/RF_half_main_prev.pkl"
    model = joblib.load(f)
    return model.predict(dt)[0]

def mixed_loans_predict(data):
    dt = data[['PREV_ANNUITY_median', 'PREV_CREDIT_sum', 'DAYS_DECISION_median', 'DAYS_PERIOD_median', 'AMT_INCOME_TOTAL', 'DAYS_BIRTH', 'DAYS_EMPLOYED', 'DAYS_REGISTRATION', 'DAYS_ID_PUBLISH', 'DAYS_LAST_PHONE_CHANGE']]
    f = "myproject/static/models/main_prev_randomforest_ml2"
    model = joblib.load(f)
    return model.predict(dt)[0]