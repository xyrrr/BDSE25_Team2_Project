from flask_login import session_protected
from sqlalchemy.pool import QueuePool


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root:bdse25@localhost:3306/bdseprojects'
    SECRET_KEY = "iSpanbdse25"
    SESSION_PROTECTION = 'strong'
    SQLALCHEMY_ENGINE_OPTIONS = {
        'poolclass' : QueuePool,
        'pool_pre_ping': True,  
        'pool_recycle': 300,    # 多久後進行連線重置，-1為永不回收
        'pool_timeout': 900,    # 池滿後，最多等待連接時間
        'pool_size': 20,        # 連接池大小
        'max_overflow': 5,      # 超過pool外，最多可建立連接數
    }