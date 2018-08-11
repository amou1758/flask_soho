# Flask入门

## [教程传送门](https://www.bilibili.com/video/av19817183)

FLask诞生于2010年, Python语言基于Wer看zeug工具编写的轻量级Web开发框架

Flask本身相当于一个内核, 其他几乎所有的功能都要用到扩展(右键扩展 FLask-Mail, 用户认证 Flask-Login), 都需要用第三方的扩展来实现



其 WSGI 工具箱采用 Werkzeug (路由模块), 模版引擎则使用 Jinja2. 这两个也是 Flask 框架的核心.



## Flask常用扩展包

- Flask-SQLalchemy: 操作数据库;
- Flask-migrate: 管理迁移数据库;
- Flask-Mail: 邮件;
- Flask-WTF: 表单;
- Flask-Bable: 提供国际化和本地化支持, 翻译;
- Flask-Sript: 插入脚本;
- Flask-Login: 认证用户状态;
- Flask-Open(): 认证;
- FLask-RESTful: 开发 REST API 工具;
- FLask-Bootstrap: 集成前端 Twitter Bootsstrap 框架;
- FLask-Moment: 本地化日期和时间;
- Flask-Admin: 简单而可扩展的管理接口的框架;

扩展列表: http://flask.pocoo.org/extensions/



### requirements 文件

Python 项目中必须包含一个 requirements.txt 文件, 用于记录所有依赖包机器精确的版本号, 以便在新环境中进行部署操作



在虚拟环境中使用以下命令将当前虚拟环境中的依赖包以版本号生成至文件中

#### 生成 requirements.txt 文件

```python
$ pip freeze >requirements.txt
```

安装或升级包后, 最好更新这个文件以保证虚拟环境中的依赖包



#### 安装 requirements.txt 依赖

当需要创建这个虚拟环境的完全副本, 可以创建一个新的虚拟环境, 并在其上运行以下命令

```python
$ pip install -r requirements.txt
```



### 运行 Flask 程序

1. 导入 Flask 扩张

```python
from flask import Flask
```

1. 创建 Flask 应用程序实例

```python
# 需要传入 __name__ , 作用是为了确定资源的所在路径 
app = Flask(__name__)
```

1. 定义路由及试图函数

```python
# Flask 中定义路由是通过装饰器实现的
# 路由默认只支持GET请求, 如果需要增加请求方法, 自行指定
@app.route('/', methods=['GET', 'POST'])
def index():
	return "Hello World"
```

1. 启动程序

```python
if __name__ == '__main__':
    # 执行 "app.run" , 你可以启动 flask 程序运行在一个简易的服务器上
    app.run()
```



### 路由参数处理

有时我们需要将同一类 URL 映射到同一个视图函数处理, 比如: 使用同一个视图函数 来现实不同拥护的订单信息



路由传递的参数默认当作 String 处理

```python
# 使用同一个视图函数, 来显示不同用户的订单信息
# <> 定义路由的参数, <>内需要起个名字
@app.route("/orders/<int:order_id>")
def git_order_id(order_id):
    # 需要在视图函数的 () 内填入参数名, 后面的代码才能使用
    # 有时, 需要对路由做访问优化, 订单ID应该是int类型
    # 参数类型, 默认是一个字符串
    print(type(order_id))
    return "order_id is {}".format(order_id)

```

