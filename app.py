from flask import Flask, render_template, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

app = Flask(__name__)

# 配置数据: 数据库地址
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+mysqlconnector://root:123456@127.0.0.1/flask_books"

# 关闭自动跟踪修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "amou1758"

# 创建数据库对象
db = SQLAlchemy(app)


# 配置书和作者的模型
class Author(db.Model):
    # 表名
    __tablename__ = "authors"

    # 字段
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), unique=True)

    # 关系引用
    # books 是给自己(Author)用的, author是给 Book 模型用的
    books = db.relationship("Book", backref="author")

    # 规范性返回
    def __repr__(self):
        return "Author: {}".format(self.name)


class Book(db.Model):

    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(24), unique=True)

    # 创建外键
    author_id = db.Column(db.Integer, db.ForeignKey("authors.id"))

    def __repr__(self):
        return "<Book: {} {}>".format(self.name, self.author_id)


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
    a. 自定义表单类
    b. 模版中显示
    c. secret_key / 编码 / csrf_token
6. 实现相关的增删逻辑
    a. 添加内容

"""

# 自定义表单类
class AuthorForm(FlaskForm):
    author = StringField("作者:", validators=[DataRequired()])
    book = StringField("书籍:", validators=[DataRequired()])
    submit = SubmitField("提交")


@app.route("/", methods=["GET", "POST"])
def index():
    # 创建一个自定义的表单类
    author_form = AuthorForm()

    """
    验证逻辑:
    1. 调用 WTF 的验证函数  实现验证
    2. 通过验证, 获取数据
    3. 判断作者是否存在
    4. 如果作者存在, 再判断书籍是否存在, 如果没有重复书籍就添加书籍, 如果重复提示错误
    5. 如果作者不存在, 添加作者和书籍
    6. 验证不通过提示错误
    """
    if request.method == "POST":
        # 1. 调用 WTF 的验证函数  实现验证
        if author_form.validate_on_submit():
            # 2. 通过验证, 获取数据
            author_name = author_form.author.data
            book_name = author_form.book.data

            # 3. 判断作者是否存在
            author = Author.query.filter_by(name=author_name).first()

            # 4. 如果作者存在
            if author:
                # 判断书籍是否存在, 如果没有重复书籍, 进行添加, 反之提示错误
                book = Book.query.filter_by(name=book_name).first()
                if book:
                    flash("书籍已存在同名书籍")
                else:
                    # 添加书籍
                    try:
                        new_book = Book(name=book_name, author_id=author.id)
                        db.session.add(new_book)
                        db.session.commit()
                    except Exception as e:
                        flash("添加书籍失败")
                        print("" + str(e))
                        db.session.rollback()
            else:
                # 5. 如果作者不存在, 添加作者和书籍
                try:
                    new_author = Author(name=author_name)
                    db.session.add(new_author)
                    db.session.commit()

                    new_book = Book(name=book_name, author_id=new_author.id)
                    db.session.add(new_book)
                    db.session.commit()

                except Exception as e:
                    flash("添加作者或者书籍失败!!!")
                    print(e)
                    db.session.rollback()
        else:

            # 6. 验证不通过提示错误
            flash("参数不全!!!")

    # 查询作者的信息  传递给模版
    authors = Author.query.all()
    return render_template("books.html", authors=authors, form=author_form)


if __name__ == "__main__":
    # 先清空数据库
    db.drop_all()
    # 创建需要的表结构
    db.create_all()

    # 生成数据
    au1 = Author(name="老张")
    au2 = Author(name="老王")
    au3 = Author(name="老李")
    au4 = Author(name="老赵")
    au5 = Author(name="老孙")

    db.session.add_all([au1, au2, au3, au4, au5])
    db.session.commit()

    bk1 = Book(name="三字经", author_id=au1.id)
    bk2 = Book(name="百家姓", author_id=au2.id)
    bk3 = Book(name="唐诗", author_id=au3.id)
    bk4 = Book(name="宋词", author_id=au4.id)
    bk5 = Book(name="公众号文章", author_id=au5.id)
    bk6 = Book(name="微博", author_id=au5.id)
    bk7 = Book(name="朋友圈", author_id=au3.id)
    db.session.add_all([bk1, bk2, bk3, bk4, bk5, bk6, bk7])
    db.session.commit()

    app.run(debug=True)
