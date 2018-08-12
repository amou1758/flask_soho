from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)


app.secret_key = 'amou1758'

'''
目的: 实现一个简单的登陆逻辑处理
1. 路由需要有get和post两种请求方式 ---> 需要判断请求方式
2. 获取请求的参数
3. 判断参数是否填写 & 密码是否相同
4. 如果判断都没有问题, 就返回一个success
'''

'''
给模版传递消息
flash  ---> 需要对内容加密, 因此需要设置 secret_key, 做加密消息的混淆
模版中需要遍历消息
'''

'''
使用WTF实现表单
自定义表单类
'''

class LoginForm(FlaskForm):
    username = StringField('用户名:')
    password = PasswordField('密码:')
    password2 = PasswordField('确认密码:')
    submit = SubmitField('提交')


@app.route('/form', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    return render_template('index.html', form=login_form)



@app.route('/', methods=['GET', 'POST'])
def index():
    # request: 请求对象 --> 获取请求方式, 数据
    # 1. 判断请求方式
    if request.method == 'POST':
        # 2. 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 3. 判断参数是否填写 & 密码是否相同
        if not all([username, password, password2]):
            flash("参数不完整")
        elif password != password2:
            flash("密码不一致")
        else:
            return 'success'
    return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)

