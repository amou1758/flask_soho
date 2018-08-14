from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据: 数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1/flask_books'

# 关闭自动跟踪修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# 创建数据库对象
db = SQLAlchemy(app)


"""
1. 配置数据库
    a. 导入 sqlalchemy 扩展
    b. 创建db对象, 并配置参数
    c. 终端创建数据
2. 添加书和作者的模型
3. 添加数据
4. 使用模版显示数据库查询的数据
5. WTF表单来显示表单
6. 实现相关的增删逻辑

"""

@app.route('/')
def index():
    return render_template('books.html')


if __name__ == "__main__":
    app.run(debug=True)