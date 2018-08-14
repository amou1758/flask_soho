from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据: 数据库地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:123456@127.0.0.1/flask_books'

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
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    def __repr__(self):
        return '<Book: {} {}>'.format(self.name, self.author_id)

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
    a. 查询所有的额作者的信息, 让信息传递给模版
    b. 模版中按照格式, for循环作者和书籍即可, (作者获取书籍, 用的是关系引用)
5. WTF表单来显示表单
6. 实现相关的增删逻辑

"""

@app.route('/')
def index():
    # 查询作者的信息  传递给模版
    authors = Author.query.all()


    return render_template('books.html', authors=authors)


if __name__ == "__main__":
    # 先清空数据库
    db.drop_all()
    # 创建需要的表结构
    db.create_all()

    # 生成数据
    au1 = Author(name='老张')
    au2 = Author(name='老王')
    au3 = Author(name='老李')
    au4 = Author(name='老赵')
    au5 = Author(name='老孙')

    db.session.add_all([au1, au2, au3, au4, au5])
    db.session.commit()

    bk1 = Book(name='三字经', author_id=au1.id)
    bk2 = Book(name='百家姓', author_id=au2.id)
    bk3 = Book(name='唐诗', author_id=au3.id)
    bk4 = Book(name='宋词', author_id=au4.id)
    bk5 = Book(name='公众号文章', author_id=au5.id)
    bk6 = Book(name='微博', author_id=au5.id)
    bk7 = Book(name='朋友圈', author_id=au3.id)
    db.session.add_all([bk1, bk2, bk3, bk4, bk5, bk6, bk7])
    db.session.commit()


    app.run(debug=True)