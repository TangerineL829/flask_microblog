from flask import  Flask
from config import Config#从config模块导入Config类
app = Flask(__name__)
app.config.from_object(Config)










#导入routes函数 在app后面 防止交叉循环
from app import routes
