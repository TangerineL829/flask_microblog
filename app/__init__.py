from flask import  Flask
app = Flask(__name__)
print('等会谁（哪个包或模块）在使用我：',__name__)











#导入routes函数 在app后面 防止交叉循环
from app import routes
