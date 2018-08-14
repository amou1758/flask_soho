from flask import Flask, render_template


app = Flask(__name__)

"""
1. 配置数据库
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