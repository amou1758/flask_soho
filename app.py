from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据: 数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1/flask_books'

# 关闭自动跟踪修改
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# 创建数据库对象
db = SQLAlchemy(app)


# 配置书和作者的模型
class Author(db.Model):
    # 表名
    __tablename__ = 'authors'

    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), unique=True)

    # 关系引用
    # books 是给自己(Author)用的, author是给 Book 模型用的
    books = db.relationship('Book', backref='author')

    # 规范性返回
    def __repr__(self):
        return 'Author: {}'.format(self.name)

class Book(db.Model):

    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), unique=True)

    # 创建外键
    author_id = db.Column(db.Integer, Foreignkey='authors.id')


    def __repr__(self):
        return '<Book: {}>'.format(self.name)

"""
1. 配置数据库
    a. 导入 sqlalchemy 扩展
    b. 创建db对象, 并配置参数
    c. 终端创建数据
2. 添加书和作者的模型
    a. 模型继承自 db.Model
    b. __tablename__ 定义表名
    c. db.Column 定义字段
    d. db.relationship 关系引用
    f. db.ForeignKey 创建外键
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