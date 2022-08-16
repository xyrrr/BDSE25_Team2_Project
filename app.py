# Create all route

from flask import render_template, redirect, request, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required
from myproject import app, db, engine, table_applications
from myproject import mainform, invesfrom, loadmodels, questdata
from myproject.models import User
from sqlalchemy import func
import math
import pandas as pd
import numpy as np
from flask_login import current_user

# 一般使用者專區
# user 頁面
@app.route('/')
def index():
    return render_template('customerindex.html', index="active")

# user home
@app.route('/home')
def home():
    return render_template('customerindex.html', index="active")

# user 貸款申請表單
@app.route('/cusapply')
def cusapply():
    return render_template('applicationCus.html', apply="active")

@app.route('/thankapply',methods = ['POST', 'GET'])
def thankapply():
    result=mainform.mainprocess(request.form)
    info=mainform.mainwritesql(result)

    form = LoginForm()
    if current_user.is_active:
        print('current_user=',current_user)
        return render_template('investigation.html',info=info)
    else:
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
    return render_template('index.html', index="active")

# admin version 貸款申請表單
@app.route('/adminapply')
@login_required
def adminapply():
    return render_template('application.html', apply="active")

# admin version 行員確認表單
@app.route('/admininves')
@login_required
def admininves():
    info = {}
    info['sk_id'] = ''
    info['fullname'] = ''
    info['applyday'] = ''
    return render_template('investigation.html', inves="active",info=info)

# 行員確認表單中確認資料用flask
@app.route('/getinfo',methods = ['POST', 'GET'])
@login_required
def getinfo():
    skid=request.form["skid"]
    data=questdata.quest_temp_data(skid)
    return jsonify(data)

# admin version 信用評估
@app.route('/admineval',methods = ['POST', 'GET'])
@login_required
def admineval():
    if request.method == "GET":
        sk_id = ""
        return render_template('evaluation.html', evalu="active", skid=sk_id)
    else:
        sk_id=request.form["currID"]
        data1,data2 = invesfrom.invesprocess(request.form)
        print(data1)
        print(data2)
        invesfrom.inveswritesql(data1,data2)
        return render_template('evaluation.html', evalu="active", skid=sk_id)

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

    return render_template('creditreport.html', evalu="active",data=datas, riskind=risk_ind, same_results=same_results, curr_results=curr_results, url_link=url_link)


if __name__ == '__main__':
    app.run(debug=True)