from werkzeug.urls import url_parse
from app import app, db
from flask import render_template, flash, redirect, url_for, request  # 从flask包中导入render_template函数
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required  # 第三方登录
from app.models import User

@app.route('/')
@app.route('/index')
@login_required#函数将被收到保护，并且不允许未经过身份验证的用户 拦截
def index():
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
    return render_template('index.html', title='Home', posts=posts)


@app.route('/login', methods=['GET', 'POST'])#z注册
def login():
    if current_user.is_authenticated:#已经登录返回主页
        return redirect(url_for('index'))
    login_from = LoginForm()
    if login_from.validate_on_submit():
        user = User.query.filter_by(username=login_from.username.data).first()
        if user is None or not user.check_password(login_from.password.data):
            # flash('Login requested for user {},remember_me={}'.format(login_from.username.data, login_from.remember_me.data))
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=login_from.remember_me.data)

        # 重定向到 next 页面
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':#重定向页面
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=login_from)
@app.route('/logout')#注册退出
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
