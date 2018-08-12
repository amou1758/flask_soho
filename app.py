from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    # 假设需要传入一个网址
    url_str = 'www.itheima.com'

    my_list = [1, 3, 5, 7, 9]
    my_dict = {
        'name': "我是代码搬运工!!!",
        'url': "www.cnblog.com/username"
    }
    # 通常, 模版中使用的变量名和要床底的数据的变量名要保持一致
    return render_template('index.html', url_str=url_str, my_list=my_list, my_dict=my_dict)


# 使用同一个视图函数, 来显示不同用户的订单信息
# <> 定义路由的参数, <>内需要起个名字
@app.route("/orders/<int:order_id>")
def git_order_id(order_id):
    # 需要在视图函数的 () 内填入参数名, 后面的代码才能使用
    # 有时, 需要对路由做访问优化, 订单ID应该是int类型
    # 参数类型, 默认是一个字符串
    print(type(order_id))
    return "order_id is {}".format(order_id)


if __name__ == "__main__":
    app.run()

