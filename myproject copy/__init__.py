# 初始化Python的"myproject" packages

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from sqlalchemy.pool import QueuePool
from flask_moment import Moment


app = Flask(__name__,template_folder='templates')

app.config['SECRET_KEY']= 'iSpanbdse25'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:bdse25@localhost:3306/bdseprojects'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'poolclass' : QueuePool,
    'pool_pre_ping': True,  
    'pool_recycle': 300,    # 多久後進行連線重置，-1為永不回收
    'pool_timeout': 900,    # 池滿後，最多等待連接時間
    'pool_size': 20,        # 連接池大小
    'max_overflow': 5,      # 超過pool外，最多可建立連接數
    }

db = SQLAlchemy(app)
moment = Moment(app)
Migrate(app,db)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


engine = db.create_engine(app.config['SQLALCHEMY_DATABASE_URI'],
                        app.config['SQLALCHEMY_ENGINE_OPTIONS'])
connection  = engine.connect()
metadata = db.MetaData()

table_applications = db.Table('applications', metadata, autoload=True, autoload_with=engine)
table_users = db.Table('users',metadata, autoload=True, autoload_with=engine)
