from app import app#导入APP对象
#定义路由
@app.route('/')
@app.route('/index')
#视图函数
def index():
    return "hello world"