from flask import request
import datetime
from myproject import app, db, engine

def mainprocess(form):
    result = dict()
    result['NAME'] = form['lastName'] + form['firstName']
    result['CODE_GENDER_F'] = 0
    if form.get('gender') == 'female': result['CODE_GENDER_F'] = 1
    result['CODE_GENDER_M'] = 0
    if form.get('gender') == 'male': result['CODE_GENDER_M'] = 1
    
    result['NAME_EDUCATION_TYPE'] = 5
    if form.get('education') == '國中': result['NAME_EDUCATION_TYPE'] = 0
    if form.get('education') == '高中': result['NAME_EDUCATION_TYPE'] = 1
    if form.get('education') == '大學肆業': result['NAME_EDUCATION_TYPE'] = 2
    if form.get('education') == '大學': result['NAME_EDUCATION_TYPE'] = 3
    if form.get('education') == '研究所': result['NAME_EDUCATION_TYPE'] = 4

    result['NAME_FAMILY_STATUS_Civil marriage'] = 0
    if form.get('family-type') == '同居': result['NAME_FAMILY_STATUS_Civil marriage'] = 1
    result['NAME_FAMILY_STATUS_Married'] = 0
    if form.get('family-type') == '已婚': result['NAME_FAMILY_STATUS_Married'] = 1
    result['NAME_FAMILY_STATUS_Separated'] = 0
    if form.get('family-type') == '離婚': result['NAME_FAMILY_STATUS_Separated'] = 1
    result['NAME_FAMILY_STATUS_Single / not married'] = 0
    if form.get('family-type') == '未婚': result['NAME_FAMILY_STATUS_Single / not married'] = 1
    result['NAME_FAMILY_STATUS_Widow'] = 0
    if form.get('family-type') == '鰥寡': result['NAME_FAMILY_STATUS_Widow'] = 1

    result['CNT_FAM_MEMBERS'] = form['family-member']
    result['CNT_CHILDREN'] = form['family-child']
    date1 = datetime.date.fromisoformat(form['birth-day'])
    date0 = datetime.date.today()
    result['APPLY_DAY'] = str(date0)
    result['DAYS_BIRTH'] = (date1 - date0).days

    result['FLAG_PHONE'] = 0
    if form.get('phone-home'): result['FLAG_PHONE'] = 1
    result['FLAG_WORK_PHONE'] = 0
    if form.get('phone-mobile'): result['FLAG_WORK_PHONE'] = 1
    result['FLAG_EMAIL'] = 0
    if form.get('email'): result['FLAG_EMAIL'] = 1

    result['REG_REGION_NOT_LIVE_REGION'] = 1
    if form.get('address-main-region') == form.get('address-contact-region'):
        result['REG_REGION_NOT_LIVE_REGION'] = 0
    result['REG_CITY_NOT_LIVE_CITY'] = 1
    if form.get('address-main-city') == form.get('address-contact-city'):
        result['REG_CITY_NOT_LIVE_CITY'] = 0
    if form.get('same-address-1') != None:
        result['REG_REGION_NOT_LIVE_REGION'] = 0
        result['REG_CITY_NOT_LIVE_CITY'] = 0
    
    result['NAME_HOUSING_TYPE_House / apartment'] = 0
    if form.get('housetype') == '獨棟': result['NAME_HOUSING_TYPE_House / apartment'] = 1
    result['NAME_HOUSING_TYPE_Municipal apartment'] = 0
    if form.get('housetype') == '公寓(Municipal)': result['NAME_HOUSING_TYPE_Municipal apartment'] = 1
    result['NAME_HOUSING_TYPE_Office apartment'] = 0
    if form.get('housetype') == '套房(office)': result['NAME_HOUSING_TYPE_Office apartment'] = 1
    result['NAME_HOUSING_TYPE_Rented apartment'] = 0
    if form.get('housetype') == '出租公寓': result['NAME_HOUSING_TYPE_Rented apartment'] = 1
    result['NAME_HOUSING_TYPE_With parents'] = 0
    if form.get('housetype') == '與父母同住': result['NAME_HOUSING_TYPE_With parents'] = 1
    
    result['LIVE_REGION_NOT_WORK_REGION'] = 1
    if form.get('address-work-region') == form.get('address-contact-region'):
        result['LIVE_REGION_NOT_WORK_REGION'] = 0
    result['LIVE_CITY_NOT_WORK_CITY'] = 1
    if form.get('address-work-city') == form.get('address-contact-city'):
        result['LIVE_CITY_NOT_WORK_CITY'] = 0
    if form.get('same-address-2') != None:
        result['LIVE_REGION_NOT_WORK_REGION'] = 0
        result['LIVE_CITY_NOT_WORK_CITY'] = 0
    
    result['REG_REGION_NOT_WORK_REGION'] = 1
    if form.get('address-main-region') == form.get('address-work-region'):
        result['REG_REGION_NOT_WORK_REGION'] = 0
    result['REG_CITY_NOT_WORK_CITY'] = 1
    if form.get('address-main-city') == form.get('address-work-city'):
        result['REG_CITY_NOT_WORK_CITY'] = 0
    if (form.get('same-address-1') != None) and (form.get('same-address-2') != None):
        result['REG_REGION_NOT_WORK_REGION'] = 0
        result['REG_CITY_NOT_WORK_CITY'] = 0

    result['FLAG_EMP_PHONE'] = 0
    if form.get('phone-mobile'): result['FLAG_EMP_PHONE'] = 1

    result['NAME_INCOME_TYPE_Commercial associate'] = 0
    if form.get('income-type') == '投資': result['NAME_INCOME_TYPE_Commercial associate'] = 1
    result['NAME_INCOME_TYPE_Pensioner'] = 0
    if form.get('income-type') == '退休金': result['NAME_INCOME_TYPE_Pensioner'] = 1
    result['NAME_INCOME_TYPE_State servant'] = 0
    if form.get('income-type') == '公職俸給': result['NAME_INCOME_TYPE_State servant'] = 1
    result['NAME_INCOME_TYPE_Working'] = 0
    if form.get('income-type') == '工作': result['NAME_INCOME_TYPE_Working'] = 1

    result['OCCUPATION_TYPE_Accountants'] = 0
    if form.get('profession-type') == '會計師': result['OCCUPATION_TYPE_Accountants'] = 1
    result['OCCUPATION_TYPE_Cleaning staff'] = 0
    if form.get('profession-type') == '清潔人員': result['OCCUPATION_TYPE_Cleaning staff'] = 1
    result['OCCUPATION_TYPE_Cooking staff'] = 0
    if form.get('profession-type') == '廚房人員': result['OCCUPATION_TYPE_Cooking staff'] = 1
    result['OCCUPATION_TYPE_Core staff'] = 0
    if form.get('profession-type') == '公司經營者': result['OCCUPATION_TYPE_Core staff'] = 1
    result['OCCUPATION_TYPE_Drivers'] = 0
    if form.get('profession-type') == '司機': result['OCCUPATION_TYPE_Drivers'] = 1
    result['OCCUPATION_TYPE_High skill tech staff'] = 0
    if form.get('profession-type') == '技術人員': result['OCCUPATION_TYPE_High skill tech staff'] = 1
    result['OCCUPATION_TYPE_Laborers'] = 0
    if form.get('profession-type') == '一般勞工': result['OCCUPATION_TYPE_Laborers'] = 1
    result['OCCUPATION_TYPE_Low-skill Laborers'] = 0
    if form.get('profession-type') == '非技術勞工': result['OCCUPATION_TYPE_Low-skill Laborers'] = 1
    result['OCCUPATION_TYPE_Managers'] = 0
    if form.get('profession-type') == '管理人員': result['OCCUPATION_TYPE_Managers'] = 1
    result['OCCUPATION_TYPE_Medicine staff'] = 0
    if form.get('profession-type') == '醫事人員': result['OCCUPATION_TYPE_Medicine staff'] = 1
    result['OCCUPATION_TYPE_Private service staff'] = 0
    if form.get('profession-type') == '私人服務人員': result['OCCUPATION_TYPE_Private service staff'] = 1
    result['OCCUPATION_TYPE_Sales staff'] = 0
    if form.get('profession-type') == '銷售人員': result['OCCUPATION_TYPE_Sales staff'] = 1
    result['OCCUPATION_TYPE_Security staff'] = 0
    if form.get('profession-type') == '保全、警衛人員': result['OCCUPATION_TYPE_Security staff'] = 1

    result['ORGANIZATION_TYPE_Agriculture'] = 0
    if form.get('profession-org') == '農業': result['ORGANIZATION_TYPE_Agriculture'] = 1
    result['ORGANIZATION_TYPE_Bank'] = 0
    if form.get('profession-org') == '銀行': result['ORGANIZATION_TYPE_Bank'] = 1
    result['ORGANIZATION_TYPE_Construction'] = 0
    if form.get('profession-org') == '建築業': result['ORGANIZATION_TYPE_Construction'] = 1
    result['ORGANIZATION_TYPE_Government'] = 0
    if form.get('profession-org') == '政府機關': result['ORGANIZATION_TYPE_Government'] = 1
    result['ORGANIZATION_TYPE_Housing'] = 0
    if form.get('profession-org') == '房仲業': result['ORGANIZATION_TYPE_Housing'] = 1
    result['ORGANIZATION_TYPE_Kindergarten'] = 0
    if form.get('profession-org') == '幼保機構': result['ORGANIZATION_TYPE_Kindergarten'] = 1
    result['ORGANIZATION_TYPE_Medicine'] = 0
    if form.get('profession-org') == '藥商': result['ORGANIZATION_TYPE_Medicine'] = 1
    result['ORGANIZATION_TYPE_Military'] = 0
    if form.get('profession-org') == '軍事機構': result['ORGANIZATION_TYPE_Military'] = 1
    result['ORGANIZATION_TYPE_Police'] = 0
    if form.get('profession-org') == '警察機構': result['ORGANIZATION_TYPE_Police'] = 1

    result['ORGANIZATION_TYPE_Postal'] = 0
    if form.get('profession-org') == '郵政機構': result['ORGANIZATION_TYPE_Postal'] = 1
    result['ORGANIZATION_TYPE_Restaurant'] = 0
    if form.get('profession-org') == '旅館業': result['ORGANIZATION_TYPE_Restaurant'] = 1
    result['ORGANIZATION_TYPE_School'] = 0
    if form.get('profession-org') == '教育機構': result['ORGANIZATION_TYPE_School'] = 1
    result['ORGANIZATION_TYPE_Security'] = 0
    if form.get('profession-org') == '保全': result['ORGANIZATION_TYPE_Security'] = 1
    result['ORGANIZATION_TYPE_Security Ministries'] = 0
    if form.get('profession-org') == '安全機構': result['ORGANIZATION_TYPE_Security Ministries'] = 1
    result['ORGANIZATION_TYPE_Services'] = 0
    if form.get('profession-org') == '服務業': result['ORGANIZATION_TYPE_Services'] = 1
    result['ORGANIZATION_TYPE_Self-employed'] = 0
    if form.get('profession-org') == '自雇': result['ORGANIZATION_TYPE_Self-employed'] = 1
    result['ORGANIZATION_TYPE_Other'] = 0
    if form.get('profession-org') == '其他': result['ORGANIZATION_TYPE_Other'] = 1
    result['ORGANIZATION_TYPE_XNA'] = 0
    if form.get('profession-org') == None: result['ORGANIZATION_TYPE_XNA'] = 1

    if form.get('profession-date'):
        date1 = datetime.date.fromisoformat(form['profession-date'])
        result['DAYS_EMPLOYED'] = (date1 - date0).days
    else:
        result['DAYS_EMPLOYED'] = 0
    result['AMT_INCOME_TOTAL'] = form['annaulincome']

    result['FLAG_OWN_CAR_N'] = 0
    if form.get('tenure-care') == 'tenure-care-no': result['FLAG_OWN_CAR_N'] = 1
    result['FLAG_OWN_CAR_Y'] = 0
    if form.get('tenure-care') == 'tenure-care-yes': result['FLAG_OWN_CAR_Y'] = 1
    
    result['FLAG_OWN_REALTY_N'] = 0
    if form.get('tenure-house') == 'tenure-house-no': result['FLAG_OWN_REALTY_N'] = 1
    result['FLAG_OWN_REALTY_Y'] = 0
    if form.get('tenure-house') == 'tenure-house-yes': result['FLAG_OWN_REALTY_Y'] = 1
    
    result['NAME_CONTRACT_TYPE_Cash loans'] = 0
    if form.get('apply-type') == 'apply-type1': result['NAME_CONTRACT_TYPE_Cash loans'] = 1
    result['NAME_CONTRACT_TYPE_Revolving loans'] = 0
    if form.get('apply-type') == 'apply-type2': result['NAME_CONTRACT_TYPE_Revolving loans'] = 1
    result['AMT_CREDIT'] = form['apply-amount']
    result['HOUR_APPR_PROCESS_START_x'] = datetime.datetime.now().hour

    result['FINAL_CHECK'] = 0
    
    return result


def mainwritesql(data):
    colword=''
    valword=''
    for k,v in data.items():
        colword = colword + '`' + str(k) + '`,'
        if isinstance(v, str):
            valword = valword + "'" + v + "',"
        else:
            valword = valword + str(v) + ","
    colword = colword[:-1]
    valword = valword[:-1]

    conn=engine.connect()
    query = f"SELECT max(SK_ID_CURR) FROM temp;"
    proxy = conn.execute(query)
    SK_ID = proxy.fetchall()[0][0] +1
    query = f"INSERT INTO temp(SK_ID_CURR, {colword}) VALUES ({SK_ID},{valword})"
    proxy = conn.execute(query)
    conn.close()

    info = {}
    info['sk_id'] = SK_ID
    info['fullname'] = data['NAME']
    info['applyday'] = data['APPLY_DAY']
    return info