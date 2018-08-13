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

@app.route('/')
def index():
	return "Hello World"



if __name__ == "__main__":
	app.run(debug=True)

