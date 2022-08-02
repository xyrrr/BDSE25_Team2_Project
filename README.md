# BDSE25 Team2 Project - 信用貸款評分系統

金融機構對於缺乏傳統信用紀錄、財務資料等數據的新客戶，如應屆畢業生、新創者等人，難以套用內部評估系統而無法進行有效率放貸決策。若能透過客戶提供的背景資訊衡量客戶的信用，便能使金融機構能快速評估並拓展低放貸風險的新客戶。

* 使用資料集 : **[Home Credit Default Risk | Kaggle](https://www.kaggle.com/c/home-credit-default-risk)**<br>
![This is an image](https://www.homecredit.net/~/media/Images/H/Home-Credit-Group/logo/hcg-logo.png?h=71&iar=0&w=121)
<br>

## 特色
1.  透過客戶提供的**個人資訊**及**財產資訊**等，快速估計新客戶的信用評分。
2.  透過與資料庫的歷史客戶比較，推算新客戶適合的信用額度。

## 功能
1.  <span style="color: #AD5A5A">**資訊輸入介面**</span> : 供客戶或金融機構員工輸入客戶資訊的網頁表單。
2.  <span style="color: #AD5A5A">**評估資訊報告**</span> : 展示依客戶輸入資訊所計算出的信用評分與可負擔的信用額度，並提供資料庫內類似背景客戶之統計圖表，供金融機構員工登入帳號後調閱。
3. <span style="color: #AD5A5A">**模型結果報告**</span> : 紀錄所訓練出的模型的分析結果，供金融機構員工身份登入帳號後調閱。


## 網頁開發架構

```
|__ app.py: create all route
|__ config.py: set all config
|__ myproject
    |__ __init.py: 初始化Python的 "myproject" packages
    |__ models.py: 連接使用者資料庫
    |__ webforms.py: 註冊、登入表格設定
    |__ example.py: 示範檔from Sih-Yin
    |               0.啟動前可給予參數設定(內有說明)
    |               1.隨意輸入7位數字，點選評估紐
    |               2.可得到回傳報
    |__ static: all js, css, image (refer to Sih_Yin's README)
    |__ templates: all html (refer to Sih_Yin's README)
        |__ login.html: 登入頁面
        |__ register.html: 註冊頁面
        |__ customerindex.html: 一般(user)登入首頁
        |__ appicationCus.html: 一般(user)客戶申請表
        |__ thankapply.html: 一般(user)感謝申請頁面
        |__ index.html: 行員(admin)登入首頁
        |__ application.html: 行員(admin)登入申請表頁面
        |__ investigation.html: 行員(admin)登入徵信表頁面
        |__ evaluation.html: 行員(admin)登入評估頁面
        |__ creditreport.html: 行員(admin)登入評估報表頁面
        |__ _parts: 主頁面的小部分
            |__ _base.html: 頁面基礎
            |__ _styles.html:基礎Css
            |__ _scripts.html:基礎js
            |__ _foot.html: 頁面footer
            |
            |__ _navbarcus.html: 一般(user)頁面選單
            |                    <控制變數>
            |                    1.index|apply="active": 讓navbar該頁面連結可以亮起來 
            |
            |__ _navbarlogin.html: 行員(admin)頁面選單
            |
            |__ _indexmain.html: 首頁主體
            |                    <控制變數>
            |                    1.index|apply|inves|evalu="active": 讓navbar該頁面連結可以亮起來
            |                    2.bankername: 控制登入時帳號行員名稱
            |
            |__  _mainapply.html: 貸款申請主表
            |__  _maininves.html: 徵信主表(需登入)
            |__  _evaluation.html: 評估頁面主體
            |
            |__  _report.html: 評估回傳報表頁面主體
            |                    <控制變數>
            |                    1.bankername : 控制登入時帳號行員名稱
            |                    2.userid : 用戶ID or 名稱控制變數
            |                    3.bankername : 銀行員帳號名稱
            |                    4.username : 客戶名稱
            |                    5.gender : 客戶性別
            |                    6.userage : 客戶年齡
            |                    7.phonenumber : 客戶電話
            |                    8.email : 客戶Email
            |                    9.loantype : 客戶申請類別
            |                    11.loanAMT  : 客戶申請金額
            |                    12.score : 客戶評估分數
            |                    13.results : 加裝示範從資料庫收集的資料
            |
            |__  _thankapply.html: 客戶申請確認後回傳頁面
```