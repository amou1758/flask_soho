from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# 配置数据的地址
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:123456@127.0.0.1/flask_sql_demo"

# 动态追踪修改设置, 如未设置只会提示警告, 不建议开启
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# 查询时会显示原始 SQL 语句
# app.config["SQLALCHEMY_ECHO"] = True


db = SQLAlchemy(app)

"""
两张表:
角色(管理员 / 普通用户)
用户(角色ID)

"""

# 数据的模型需要继承自 --> db.Model
class Role(db.Model):
    # 定义表
    __tablename__ = "roles"
    # 定义字段
    # db.Colum 表示的是一个字段
    # 字段类型, 是否为主键
    id = db.Column(db.Integer, primary_key=True)
    # 字段类型及长度, 是否唯一约束
    name = db.Column(db.String(16), unique=True)

    # 在一的这方, 写关联
    # users = db.relationship('User'): 表示和 User 模型发生了关联, 增加了一个 User 属性
    # backref='role': 表示 role 是 user 的关联属性
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role: {} {}>'.format(self.name, self.id)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    email = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    # 声明为外键, 参数为:  与什么表进行关联
    # User 希望有一个 Role 属性, 但是这个属性的定义, 需要在另一个模型中定义
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"))

    def __repr__(self):
        return '<User: {} {} {} {} >'.format(self.name, self.id, self.email, self.password)


@app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    # 删除表
    db.drop_all()

    # 创建表
    db.create_all()
    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()

    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='li', email='li@163.com', password='123456', role_id=ro2.id)
    us3 = User(name='zhang', email='zhang@163.com', password='123456', role_id=ro1.id)
    us4 = User(name='zhao', email='zhao@163.com', password='123456', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4])
    db.session.commit()

    app.run(debug=True)
