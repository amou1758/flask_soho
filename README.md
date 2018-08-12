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

### 第九章: Jinja2 模版引擎简介  —> [传送门](https://www.bilibili.com/video/av19817183/?p=9&t=229)

#### 模版

在前面的示例中, 视图函数的主要作用是生成请求的相应, 这是最简单的请求. 实际上, 视图函数有两个作用: 处理业务逻辑和返回相应诶容.

在大型应用中, 把业务逻辑和变现内容放在一块, 会增加代码的复杂度和维护成本.

- 模版是一个包含相应文本的文件, 其中用占位符(变量)表示动态部分. 告诉模版引擎其具体的值需要从使用的数据中获取
- 使用真是值替换变量, 再返回最终得到的字符串, 这个过程称为“**渲染**”
- Flask是使用 Jinja2 引擎来渲染模版的

**使用模版的好处 :**

- 视图函数只负责业务逻辑和数据处理(业务逻辑方面)
- 模版获取视图函数的数据结果进行展示(视图真是方面)
- 代码结构清洗, 耦合度低

#### Jinja2

**两个概念: **

- Jinja2: 是 Python 中一个被广泛应用的模版引擎, 是由 Python 实现的模版语言. 他的设计思想来源于 DJango 的模版引擎, 并扩展了其语法和一系列强大的功能, 是 Flask 内置的模版语言
- 模版语言: 是一种被设计来自动生成文档的简单文本格式, 在模版语言中, 一般都会把一些变量传给模版, 替换模版特定位置上预先定义好的展位变量名.

**渲染模版函数**

- Flask 提供的 render_template 函数封装了该模版引擎
- render_template 函数的第一个参数是模版的文件名. 后面的参数都是键值对, 表示模版中变量对应的真实值

**使用: **

注释:

- 使用 {{ # # }} 执行注释

```html
{# 下面是代码块的使用 #}
<!--下面是代码块的使用-->
这两个的作用是一样的
```



### 第十章: 变量代码块 —>[传送门](https://www.bilibili.com/video/av19817183/?p=10)

**{{}}** 来表示式变量名, 这种 {{}} 语法叫做 **变量代码块**

```html
{{ post.title }}
```

Jinja2 模版中的变量代码块可以是**任意的 Python 类型或对象**, 只要它能够被 Python 的 str() 方法转换为一个字符串就可以, 比如: 可以用过下面的方式现实一个字典或者列表中的某个元素

```html
{{ your_dict['key'] }}
{{ your_lsit[0] }}
```

#### 示例

```python
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

```



```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
这是模版 <br>
这是首页 <br>
{# 下面是代码块的使用 #}
<!--下面是代码块的使用-->
{{url_str}}<br>
{# 下面是列表的传入和使用 #}
{{my_list}}<br>
{{my_list.2}}<br>
{{my_list[2]}}<br>

{# 下面是字典的传入和使用 #}
{{ my_dict }}<br>
{{ my_dict.name }}<br>
{{ my_dict['url'] }}<br>
{{ my_dict.get('url') }}<br>

</body>
</html>
```



### 第十一章: 控制代码块 —> [传送门](https://www.bilibili.com/video/av19817183/?p=11):

- 用 {% %} 定义的控制代码块, 可以实现一些语言层次的功能, 比如循环或者 条件语句

**条件代码块**

```html
{% if user %}
	{{ user }}
{% else %}
	...
{% endif %}
```

**循环代码块**

```html
{% for item in items %}
	{{ item }}
{% endfor %}
```



**示例:**

```html
{# for 循环的基本使用 #}
{# my_list = [1, 3, 5, 7, 9] #}
{% for num in my_list %}
    {# if 条件语句的基本使用 #}
    {% if num > 3 %}
        {{ num }}<br>
    {% endif %}
{% endfor %}


```



