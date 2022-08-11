# Create all route

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from myproject import app, db, engine, table_applications
from myproject import mainform, loadmodels, questdata
from myproject.models import User
from sqlalchemy import func
import math
import pandas as pd
import numpy as np

# 一般使用者專區
# user 頁面
@app.route('/')
def index():
    return render_template('customerindex.html')

# user home
@app.route('/home')
def home():
    return render_template('customerindex.html')

# user 貸款申請表單
@app.route('/cusapply')
def cusapply():
    return render_template('applicationCus.html')
    # sumit後跳轉到感謝申請頁面 thankapply.html

@app.route('/thankapply',methods = ['POST', 'GET'])
def thankapply():
    result=mainform.mainprocess(request.form)
    return render_template('thankapply.html')


from myproject.webforms import LoginForm, RegistrationForm

@app.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        # add to db table
        db.session.add(user)
        db.session.commit()
        flash("感謝註冊本系統成為會員")
        return redirect(url_for('login'))
    return render_template('register.html',form=form)
   

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("您已經成功登入系統")
            next = request.args.get('next')
            if next == None or not next[0]=='/':
                next = url_for('admin')
                return redirect(next)
    return render_template('login.html',form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("您已經登出系統")
    return redirect(url_for('home'))


# 行員專區
# admin version home
@app.route('/adminhome')
@login_required
def admin():
    return render_template('index.html', index="active",bankername="Skye")

# admin version 貸款申請表單
@app.route('/adminapply')
@login_required
def adminapply():
    return render_template('application.html')

# admin version 徵信表單
@app.route('/admininves')
@login_required
def admininves():
    return render_template('investigation.html')

# admin version 信用評估
@app.route('/admineval')
@login_required
def admineval():
    return render_template('evaluation.html')

@app.route('/report',methods = ['POST', 'GET'])
@login_required
def report():
    skid=request.form["currid"]
    skid=int(skid)
    df1,df2 = loadmodels.load_date(skid)
    if len(df1) == 0:
        return render_template('creditreportnoid.html')
    datas = loadmodels.info_date(df1)
    datas['id'] = skid

    re_list = [loadmodels.main_simple_predict(df1),loadmodels.main_loans_predict(df1)]
    if len(df2) != 0:
        df = pd.merge(df1,df2)
        re_list2 = [loadmodels.prev_simple_predict(df2),loadmodels.prev_loans_predict(df2),
            loadmodels.mixed_simple_predict(df),loadmodels.mixed_loans_predict(df)]
        re_list = re_list + re_list2
    
    risk_ind = loadmodels.risk_index(re_list)
    same_results, curr_results, url_link = questdata.quest_data(skid)

    return render_template('creditreport.html',data=datas, riskind=risk_ind, same_results=same_results, curr_results=curr_results, url_link=url_link)



@app.route('/data-list')
@login_required
def data_list():

    # query string
    page = int(request.args.get('page') if request.args.get('page') else 1)
    each_page = 50

    # set total pages
    connection  = engine.connect() # connection 要放在view function中，否則會出現thread error
    query = db.select(func.count()).select_from(table_applications)
    proxy = connection.execute(query)
    total_pages = math.ceil(proxy.fetchall()[0][0]/each_page) # [0][0] => inorder to get the value

    # fetch data & decided by page
    query = db.select(table_applications).limit(each_page).offset((page-1)*each_page)
    proxy = connection.execute(query)
    results = proxy.fetchall()
    print(results[1].keys())

    # Close connection
    connection.close()
    
    return render_template('data_list.html',
                           page_header="Home Credit Applications Database",
                           total_pages=total_pages,
                           outputs=results,
                           page=page)

if __name__ == '__main__':
    app.run(debug=True)