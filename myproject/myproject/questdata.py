from myproject import app, db, engine
from pathlib import Path
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

def quest_data(skid):

    conn=engine.connect()
    query1 = f"SELECT a.SK_ID_CURR,a.AMT_INCOME_TOTAL,round((abs(a.DAYS_EMPLOYED)/365.25),1),a.AMT_REQ_CREDIT_BUREAU_QRT,p.PREV_CREDIT_max,p.PREV_ANNUITY_median\
            FROM applications a join database_prev p on a.SK_ID_CURR=p.SK_ID_CURR\
            WHERE a.AMT_INCOME_TOTAL =(SELECT AMT_INCOME_TOTAL FROM applications WHERE SK_ID_CURR='{skid}')  ORDER BY RAND() LIMIT 5;"
    proxy1 = conn.execute(query1)
    same_results = proxy1.fetchall()
    query2 = f"SELECT a.SK_ID_CURR,a.AMT_INCOME_TOTAL,round((abs(a.DAYS_EMPLOYED)/365.25),1),round((abs(a.DAYS_REGISTRATION)/365.25),1),round((abs(a.DAYS_ID_PUBLISH)/365.25),1),a.AMT_REQ_CREDIT_BUREAU_QRT,p.PREV_ANNUITY_median,p.PREV_CREDIT_max \
            FROM applications a join database_prev p on a.SK_ID_CURR=p.SK_ID_CURR  where a.SK_ID_CURR='{skid}';"
    proxy2 = conn.execute(query2)
    curr_results = proxy2.fetchall()

    # EMP.png
    query3 = f"SELECT round((abs(a.DAYS_EMPLOYED)/365.25)),avg(p.PREV_CREDIT_max)\
              FROM applications a join database_prev p on a.SK_ID_CURR=p.SK_ID_CURR\
              WHERE round((abs(DAYS_EMPLOYED)/365.25)) <= (SELECT round((abs(DAYS_EMPLOYED)/365.25))+5 FROM applications WHERE SK_ID_CURR='{skid}') and round((abs(DAYS_EMPLOYED)/365.25)) >= (SELECT round((abs(DAYS_EMPLOYED)/365.25))-5 FROM applications WHERE SK_ID_CURR='{skid}')\
              group by round((abs(a.DAYS_EMPLOYED)/365.25)) ;"
    proxy3 = conn.execute(query3)
    emp_result = proxy3.fetchall()
    fig=plt.figure()
    y1=[round(i[1]) for i in emp_result]
    x1=[i[0] for i in emp_result]
    plt.xlabel('Seniority', labelpad=20,fontsize=14)
    plt.ylabel('Max. Approved Loan Amount', labelpad=20, fontsize=14)
    plt.bar(x1,y1)
    url_link=dict()
    url_link['work'] = f'../..//static/img/Year_EMP{skid}.png'
    fig.savefig(f'myproject/static/img/Year_EMP{skid}.png',bbox_inches = 'tight')

    #  Incom.png  
    query4 = f"SELECT round(a.AMT_INCOME_TOTAL/10000),avg(p.PREV_CREDIT_max)\
               FROM applications a join database_prev p on a.SK_ID_CURR=p.SK_ID_CURR\
               WHERE round(a.AMT_INCOME_TOTAL/10000) <= (SELECT round(AMT_INCOME_TOTAL/10000)+5 FROM applications WHERE SK_ID_CURR='{skid}') and round(a.AMT_INCOME_TOTAL/10000) >= (SELECT round(AMT_INCOME_TOTAL/10000)-5 FROM applications WHERE SK_ID_CURR='{skid}')\
               group by round(a.AMT_INCOME_TOTAL/10000) ;"
    proxy4 = conn.execute(query4)
    income_result = proxy4.fetchall()
    fig=plt.figure()
    y2=[round(i[1]) for i in income_result]
    x2=[i[0] for i in income_result]
    plt.xlabel('Annual Income (ten thousand)', labelpad=20,fontsize=14)
    plt.ylabel('Max. Approved Loan Amount', labelpad=20, fontsize=14)
    plt.bar(x2,y2)
    url_link['income'] = f'../..//static/img/Income{skid}.png'
    fig.savefig(f'myproject/static/img/Income{skid}.png',bbox_inches = 'tight')

    conn.close()

    return same_results, curr_results, url_link
    same_results=same_results,curr_results=curr_results,url_work=url_work,url_income=url_income
