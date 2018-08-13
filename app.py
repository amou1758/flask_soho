from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)



# 配置数据的地址
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1/3306/flask_sql_dome'

# 动态追踪修改设置, 如未设置只会提示警告, 不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 查询时会显示原始 SQL 语句
app.config['SQLALCHEMY_ECHO'] = True


db = SQLAlchemy(app)

'''
两张表:
角色(管理员 / 普通用户)
用户(角色ID)

'''

# 数据的模型需要继承自 --> db.Model
class Role(db.Model):
	# 定义表
	__table__ = 'roles'
	# 定义字段
	# db.Colum 表示的是一个字段
	# 字段类型, 是否为主键
	id = db.Column(db.Integer, primary_key=True)
	# 字段类型及长度, 是否唯一约束
	name = db.Column(db.String(16), unique=True)


class User(db.Model):
	__table__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(16), unique=True)
	# 声明为外键, 参数为:  与什么表进行关联
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))






@app.route('/')
def index():
	return "Hello World"



if __name__ == "__main__":
	app.run(debug=True)

