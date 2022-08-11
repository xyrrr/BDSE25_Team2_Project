from flask import Flask, render_template ,request
from flask_moment import Moment

app = Flask(__name__,template_folder='templates')
moment = Moment(app)

@app.route('/')
def index():
    return render_template('evaluation.html', evalu="active",bankername="Skye")
# index|apply|inves|evalu="active" :讓navbar該頁面連結可以亮起來
# bankername="banker name" : 控制登入時帳號行員名稱

@app.route('/report')
def report():
     result=[ {
            'id': '7894562',
            'type': 'POS',
            'amount': 56000,
            'other1':'header',
            'other2':'header'
        },
         {
            'id': '7894589',
            'type': 'Cash',
            'amount': 66000,
            'other1':'header',
            'other2':'header'
        }]
     return render_template('creditreport.html',userid="123456",bankername="Skye",username="Skye",gender="F",userage="18",phonenumber="#",email="#",loantype="POS",loanAMT="100000",score="80",results=result)


# userid="123456" : 用戶ID 
# bankername="Skye" : 銀行員帳號名稱
# username="Skye" : 客戶名稱
# gender="F": 客戶性別
# userage="18" : 客戶年齡
# phonenumber="#": 客戶電話
# email="#" : 客戶Email
# loantype="POS": 客戶申請類別
# loanAMT="100000" : 客戶申請金額
# score="80" : 客戶評估分數
# results=result : 加裝示範從資料庫收集的資料

if __name__=="__main__":
    app.run(debug=True)