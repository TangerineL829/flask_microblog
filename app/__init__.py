from flask import Flask
from config import Config  # 从config模块导入Config类
from flask_sqlalchemy import SQLAlchemy  # 从包中导入类
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)  # 数据库对象
migrate = Migrate(app, db)  # 迁移引擎对象
login = LoginManager(app)  # 注册
login.login_view = 'login'  # 如果没登录进入login界面

# 导入routes函数 在app后面 防止交叉循环
from app import routes,models
