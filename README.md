# 網頁開發架構

> `app.py`: create all route
> `config.py`: set all config
> myproject
>> `__init.py`: 初始化Python的 "myproject" packages
>> `models.py`: 連接使用者資料庫
>> `webforms.py`: 註冊、登入表格設定
>> `example.py`: 示範檔from Sih-Yin
>>               0.啟動前可給予參數設定(內有說明)
>>               1.隨意輸入7位數字，點選評估紐
>>               2.可得到回傳報
>> `static`: all js, css, image (refer to Sih_Yin's README)
>> `templates`: all html (refer to Sih_Yin's README)
>>> `login.html`: 登入頁面
>>> `register.html`: 註冊頁面
>>> `customerindex.html`: 一般(user)登入首頁
>>> `appicationCus.html`: 一般(user)客戶申請表
>>> `thankapply.html`: 一般(user)感謝申請頁面
>>> `index.html`: 行員(admin)登入首頁
>>> `application.html`: 行員(admin)登入申請表頁面
>>> `investigation.html`: 行員(admin)登入徵信表頁面
>>> `evaluation.html`: 行員(admin)登入評估頁面
>>> `creditreport.html`: 行員(admin)登入評估報表頁面
>>> `_parts`: 主頁面的小部分
>>> `_base.html`: 頁面基礎
>>> `_styles.html`:基礎Css
>>> `_scripts.html`:基礎js
>>> `_foot.html`: 頁面footer
>>>
>>> `_navbarcus.html`: 一般(user)頁面選單
>>>                   ```
>>>                   <控制變數>
>>>                   1.index|apply="active": 讓navbar該頁面連結可以亮起來 
>>>                   ```
>>> `_navbarlogin.html`: 行員(admin)頁面選單
>>>
>>> `_indexmain.html`: 首頁主體
>>>                   ```
>>>                    <控制變數>
>>>                    1.index|apply|inves|evalu="active": 讓navbar該頁面連結可以亮起來
>>>                    2.bankername: 控制登入時帳號行員名稱
>>>                   ```
>>>  `_mainapply.html`: 貸款申請主表
>>>  `_maininves.html`: 徵信主表(需登入)
>>>  `_evaluation.html`: 評估頁面主體
>>>
>>>  `_report.html`: 評估回傳報表頁面主體
>>>                   ```
>>>                   <控制變數>
>>>                    1.bankername : 控制登入時帳號行員名稱
>>>                    2.userid : 用戶ID or 名稱控制變數
>>>                    3.bankername : 銀行員帳號名稱
>>>                    4.username : 客戶名稱
>>>                    5.gender : 客戶性別
>>>                    6.userage : 客戶年齡
>>>                    7.phonenumber : 客戶電話
>>>                    8.email : 客戶Email
>>>                    9.loantype : 客戶申請類別
>>>                    11.loanAMT  : 客戶申請金額
>>>                    12.score : 客戶評估分數
>>>                    13.results : 加裝示範從資料庫收集的資料
>>>                    ```
>>>  `_thankapply.html`: 客戶申請確認後回傳頁面
  