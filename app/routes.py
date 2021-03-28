from app import app
from flask import render_template, flash, redirect, url_for  # 从flask包中导入render_template函数
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}  # 用户
    posts = [  # 创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/loginxxxxxx', methods=['GET', 'POST'])
def login():
    login_from = LoginForm()
    if login_from.validate_on_submit():
        flash('Login requested for user {},remember_me={}'.format(login_from.username.data, login_from.remember_me.data))
        return redirect(url_for('index') )
    return render_template('login.html', title='Sign In', form=login_from)
