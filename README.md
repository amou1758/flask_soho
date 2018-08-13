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



### 第十二章: 过滤器 —> [传送门](https://www.bilibili.com/video/av19817183/?p=12)

#### 过滤器

过滤器的本质就是函数. 有时候我们不仅仅只是需要输出变量的值, 我们还需要修改变量的显示, 是指格式化, 运算等等, 而在模版中是不能直接调用 Python 中的某些方法, 那么这就用到了过滤器

**使用方法: **

- 过滤器的使用方式为:  **变量名 | 过滤器**

```html
{{variable | filter_name(*args)}}
```

- 如果没有任何参数传给过滤器, 则可以把括号省略掉, 如下:

```html
{{variable | filter_name}}
```

- 如:  **“,**  这个过滤器的作用: 把变量 variable 的值的首字母转化为大写, 其他字幕转换为小写



#### 过滤器链式调用

**作用: ** 多个过滤器组合使用

```html
{{ variable | 过滤器1 | 过滤器2 | 过滤器3 | 过滤器n}}
```



### Flask 中常见的过滤器

#### 字符串操作:

```html
{# 当变量未定义时，显示默认字符串，可以缩写为d #}

<p>{{ name | default('No name', true) }}</p>

 

{# 单词首字母大写 #}

<p>{{ 'hello' | capitalize }}</p>

 

{# 单词全小写 #}

<p>{{ 'XML' | lower }}</p>

 

{# 去除字符串前后的空白字符 #}

<p>{{ '  hello  ' | trim }}</p>

 

{# 字符串反转，返回"olleh" #}

<p>{{ 'hello' | reverse }}</p>

 

{# 格式化输出，返回"Number is 2" #}

<p>{{ '%s is %d' | format("Number", 2) }}</p>

 

{# 关闭HTML自动转义 #}

<p>{{ '<em>name</em>' | safe }}</p>

 

{% autoescape false %}

{# HTML转义，即使autoescape关了也转义，可以缩写为e #}

<p>{{ '<em>name</em>' | escape }}</p>

{% endautoescape %}
```



#### 数值操作:

```html
{# 四舍五入取整，返回13.0 #}
<p>{{ 12.8888 | round }}</p>
 
{# 向下截取到小数点后2位，返回12.88 #}
<p>{{ 12.8888 | round(2, 'floor') }}</p>
 
{# 绝对值，返回12 #}
<p>{{ -12 | abs }}</p>
```



#### 列表操作:

```html
{# 取第一个元素 #}
<p>{{ [1,2,3,4,5] | first }}</p>
 
{# 取最后一个元素 #}
<p>{{ [1,2,3,4,5] | last }}</p>
 
{# 返回列表长度，可以写为count #}
<p>{{ [1,2,3,4,5] | length }}</p>
 
{# 列表求和 #}
<p>{{ [1,2,3,4,5] | sum }}</p>
 
{# 列表排序，默认为升序 #}
<p>{{ [3,2,1,5,4] | sort }}</p>
 
{# 合并为字符串，返回"1 | 2 | 3 | 4 | 5" #}
<p>{{ [1,2,3,4,5] | join(' | ') }}</p>
 
{# 列表中所有元素都全大写。这里可以用upper,lower，但capitalize无效 #}
<p>{{ ['tom','bob','ada'] | upper }}</p>
```



#### 字典列表操作:

```html
{% set users=[{'name':'Tom','gender':'M','age':20},
              {'name':'John','gender':'M','age':18},
              {'name':'Mary','gender':'F','age':24},
              {'name':'Bob','gender':'M','age':31},
              {'name':'Lisa','gender':'F','age':19}]
%}
 
 
{# 按指定字段排序，这里设reverse为true使其按降序排 #}
<ul>
{% for user in users | sort(attribute='age', reverse=true) %}
     <li>{{ user.name }}, {{ user.age }}</li>
{% endfor %}
</ul>
 
{# 列表分组，每组是一个子列表，组名就是分组项的值 #}
<ul>
{% for group in users|groupby('gender') %}
    <li>{{ group.grouper }}<ul>
    {% for user in group.list %}
        <li>{{ user.name }}</li>
    {% endfor %}</ul></li>
{% endfor %}
</ul>
 
{# 取字典中的某一项组成列表，再将其连接起来 #}
<p>{{ users | map(attribute='name') | join(', ') }}</p>
```

### Flask内置过滤器

Flask提供了一个内置过滤器”tojson”，它的作用是将变量输出为JSON字符串。这个在配合Javascript使用时非常有用。我们延用上节字典列表操作中定义的”users”变量

```html
<script type="text/javascript">
var users = {{ users | tojson | safe }};
console.log(users[0].name);
</script>
```



注意，这里要避免HTML自动转义，所以加上safe过滤器。

#### 语句块过滤

Jinja2还可以对整块的语句使用过滤器。

```html
{% filter upper %}
    This is a Flask Jinja2 introduction.
{% endfilter %}
```



不过上述这种场景不经常用到。

#### 自定义过滤器

内置的过滤器不满足需求怎么办？自己写呗。过滤器说白了就是一个函数嘛，我们马上就来写一个。回到Flask应用代码中：

```python
def double_step_filter(l):
    return l[::2]
```



我们定义了一个”double_step_filter”函数，返回输入列表的偶数位元素（第0位，第2位,..）。怎么把它加到模板中当过滤器用呢？Flask应用对象提供了”add_template_filter”方法来帮我们实现。我们加入下面的代码：

```python
app.add_template_filter(double_step_filter, 'double_step')
```



函数的第一个参数是过滤器函数，第二个参数是过滤器名称。然后，我们就可以愉快地在模板中使用这个叫”double_step”的过滤器了：

```html
{# 返回[1,3,5] #}
<p>{{ [1,2,3,4,5] | double_step }}</p>
```



Flask还提供了添加过滤器的装饰器”template_filter”，使用起来更简单。下面的代码就添加了一个取子列表的过滤器。装饰器的参数定义了该过滤器的名称”sub”。

```python
@app.template_filter('sub')
def sub(l, start, end):
    return l[start:end]
```



我们在模板中可以这样使用它：

```html
{# 返回[2,3,4] #}
<p>{{ [1,2,3,4,5] | sub(1,4) }}</p>
```



Flask添加过滤器的方法实际上是封装了对Jinja2环境变量的操作。上述添加”sub”过滤器的方法，等同于下面的代码。

```python
app.jinja_env.filters['sub'] = sub
```



我们在Flask应用中，不建议直接访问Jinja2的环境变量。如果离开Flask环境直接使用Jinja2的话，就可以通过”jinja2.Environment”来获取环境变量，并添加过滤器。



### 第十三章: Web表单 —> [传送门](https://www.bilibili.com/video/av19817183/?p=13)

**web 表单是 web 应用程序的基本功能**

- 它是HTML页面中负责数据采集的邮件
- 表单由三个部分组成:
  - 表单标签
  - 表单域
  - 变淡按钮
- 表单允许用户输入数据, 负责 HTML 页面数据采集, 通过表单将用户输入的数据提交给服务器

在 Flask 中, 为了处理 web 表单, 我们一般使用 Flask- WTF 扩展.

它封装了 WTForms, 并且它有验证表单数据的功能



#### 示例

**使用普通方式实现表单**

在 HTML 页面中直接写 form 表单:

```html
<form action="post">
    <label>用户名:</label><input type="text" name="username"><br>
    <label>密码:</label><input type="password" name="password"><br>
    <label>确认密码:</label><input type="password" name="password2"><br>
    <input type="submit" value="提交"><br>
</form>
```

视图函数中获取表单数据

```python
from flask import Flask, render_template, request

app = Flask(__name__)


'''
目的: 实现一个简单的登陆逻辑处理
1. 路由需要有get和post两种请求方式 ---> 需要判断请求方式
2. 获取请求的参数
3. 判断参数是否填写 & 密码是否相同
4. 如果判断都没有问题, 就返回一个success
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    # request: 请求对象 --> 获取请求方式, 数据
    # 1. 判断请求方式
    if request.method == 'POST':
        # 2. 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 3. 判断参数是否填写 & 密码是否相同
        if not all([username, password, password2]):
            print("参数不完整")
        elif password != password2:
            print("密码不一致")
        else:
            return 'success'
    return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)
```



### 第十四章: flash消息闪现 —> [传送门](https://www.bilibili.com/video/av19817183/?p=14)

#### 示例:

**index.html**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<form method="post">
    <label>用户名:</label><input type="text" name="username"><br>
    <label>密码:</label><input type="password" name="password"><br>
    <label>确认密码:</label><input type="password" name="password2"><br>
    <input type="submit" value="提交"><br>
    {# get_flashed_messages()函数用于获取 flash 提供的消息 #}
    {% for message in get_flashed_messages() %}
        {{ message }}
    {% endfor %}

</form>
</body>
</html>
```

**app.py**

```python
from flask import Flask, render_template, request, flash

app = Flask(__name__)


app.secret_key = 'amou1758'

'''
目的: 实现一个简单的登陆逻辑处理
1. 路由需要有get和post两种请求方式 ---> 需要判断请求方式
2. 获取请求的参数
3. 判断参数是否填写 & 密码是否相同
4. 如果判断都没有问题, 就返回一个success
'''

'''
给模版传递消息
flash  ---> 需要对内容加密, 因此需要设置 secret_key, 做加密消息的混淆
模版中需要遍历消息
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    # request: 请求对象 --> 获取请求方式, 数据
    # 1. 判断请求方式
    if request.method == 'POST':
        # 2. 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 3. 判断参数是否填写 & 密码是否相同
        if not all([username, password, password2]):
            flash("参数不完整")
        elif password != password2:
            flash("密码不一致")
        else:
            return 'success'
    return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True)

```



### 第十五章: WTF简介 —> [传送门](https://www.bilibili.com/video/av19817183/?p=15)



### WTForms 支持的 HTML 标准字段

| 字段                | 说明                                  |
| ------------------- | ------------------------------------- |
| StringField         | 文本字段                              |
| TextAreaField       | 多行文本字段                          |
| PasswordField       | 密码文本字段                          |
| HiddenField         | 隐藏文本字段                          |
| DateField           | 文本字段，值为 datetime.date 格式     |
| DateTimeField       | 文本字段，值为 datetime.datetime 格式 |
| IntegerField        | 文本字段，值为整数                    |
| DecimalField        | 文本字段，值为 decimal.Decimal        |
| FloatField          | 文本字段，值为浮点数                  |
| BooleanField        | 复选框，值为 True 和 False            |
| RadioField          | 一组单选框                            |
| SelectField         | 下拉列表                              |
| SelectMultipleField | 下拉列表，可选择多个值                |
| FileField           | 文件上传字段                          |
| SubmitField         | 表单提交按钮                          |
| FormField           | 把表单作为字段嵌入另一个表单          |
| FieldList           | 一组指定类型的字段                    |

#### 第十六章: 使用 Flask_WTF 实现表单 —> [传送门](https://www.bilibili.com/video/av19817183/?p=16)

**首先:  在虚拟环境中安装Flask-WTF**

**模版页面**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<hr>
<form action="">
    {{ form.username.label }}{{form.username}}<br>
    {{ form.password.label }}{{form.password}}<br>
    {{ form.password2.label }}{{form.password2}}<br>
    {{form.submit}}

</form>
</body>
</html>
```

**视图函数**

```python
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

app = Flask(__name__)


app.secret_key = 'amou1758'

'''
目的: 实现一个简单的登陆逻辑处理
1. 路由需要有get和post两种请求方式 ---> 需要判断请求方式
2. 获取请求的参数
3. 判断参数是否填写 & 密码是否相同
4. 如果判断都没有问题, 就返回一个success
'''

'''
给模版传递消息
flash  ---> 需要对内容加密, 因此需要设置 secret_key, 做加密消息的混淆
模版中需要遍历消息
'''

'''
使用WTF实现表单
自定义表单类
'''

class LoginForm(FlaskForm):
    username = StringField('用户名:')
    password = PasswordField('密码:')
    password2 = PasswordField('确认密码:')
    submit = SubmitField('提交')


@app.route('/form', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    return render_template('index.html', form=login_form)


if __name__ == "__main__":
	app.run(debug=True)
```



### 第十七章: WTF的逻辑验证 —> [传送门](https://www.bilibili.com/video/av19817183/?p=17)

### WTForms验证函数

| 验证函数    | 说明                                                   |
| ----------- | ------------------------------------------------------ |
| Email       | 验证电子邮件地址                                       |
| EqualTo     | 比较两个字段的值，常用于要求输入两次密码进行确认的情况 |
| IPAddress   | 验证IPv4网络地址                                       |
| Length      | 验证输入字符串的长度                                   |
| NumberRange | 验证输入的值在数字范围内                               |
| Optional    | 无输入值时跳过其他验证函数                             |
| Required    | 确保字段中有数据                                       |
| Regexp      | 使用正则表达式验证输入值                               |
| URL         | 验证URL                                                |
| AnyOf       | 确保输入值在可选值列表中                               |
| NoneOf      | 确保输入值不在可选列表中                               |

**模版页面**

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<form method="post">
    {{ form.csrf_token() }}
    {{ form.username.label }}{{form.username }}<br>
    {{ form.password.label }}{{form.password }}<br>
    {{ form.password2.label }}{{form.password2 }}<br>
    {{ form.submit }}

</form>
</body>
</html>
```

**视图函数**

```python
from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)


app.secret_key = 'amou1758'

'''
目的: 实现一个简单的登陆逻辑处理
1. 路由需要有get和post两种请求方式 ---> 需要判断请求方式
2. 获取请求的参数
3. 判断参数是否填写 & 密码是否相同
4. 如果判断都没有问题, 就返回一个success
'''

'''
给模版传递消息
flash  ---> 需要对内容加密, 因此需要设置 secret_key, 做加密消息的混淆
模版中需要遍历消息
'''

'''
使用WTF实现表单
自定义表单类
'''

class LoginForm(FlaskForm):
    username = StringField('用户名:', validators=[DataRequired()])
    password = PasswordField('密码:', validators=[DataRequired()])
    password2 = PasswordField('确认密码:', validators=[DataRequired(), EqualTo('password', '密码不一致')])
    submit = SubmitField('提交')


@app.route('/form', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    # 1. 判断请求方式
    if request.method == 'POST':
        # 2. 获取请求参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 3. 验证参数, WTF可以一句话实现所有的校验
        # CSRF_token
        if login_form.validate_on_submit():
            print(username, password, password2)
            return "success"
        else:
            flash('参数有误')

    return render_template('index.html', form=login_form)

if __name__ == "__main__":
	app.run(debug=True)
```



### 第十八章: Flask-SQLalchemy 扩张的简介及配置  —> [传送门](https://www.bilibili.com/video/av19817183/?p=18)

#### Flask-SQLAlchemy 扩展

- SQLAlchemy 实际上是对数据库的抽象. 让开发者不用直接 和 SQL 语句到交道, 而是通过 Python 对象来操作数据库, 在舍弃一些性能开销的同时, 换来的是开发效率的极大提升.
- SQLAlchemy 是一个关系型数据库框架, 他提供了高层的 ORM 和 底层的原生数据库的操作. flask-sqlalchemy 是一个简化了 SQLAlchemy 操作的 flask 扩展



#### 安装 Flask-SQLalchemy

```python
pip install flask-sqlalchemy
```

如果连接的是 mysql 数据库, 需要安装 mysqldb

```python
pip install flask-mysqldb
```



#### 使用 Flask-SQLAlchemy 管理数据库

在 Flask-SQLAlchemy 中, 数据库使用 URL 指定, 而且程序使用的数据库必须保存到Flask 配置对象的 SQLALCHEMY_DATABASE_URI 键中.



#### Flask 的数据库设置

```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@127.0.0.1:3306/test'
```

其他设置:

```python
# 动态追踪修改设置, 如未设置只会提示警告, 不建议开启
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 查询时会显示原始 SQL 语句
app.config['SQLALCHEMY_ECHO'] = True
```



### 第十九章: 定义数据模型 —> [传送门](https://www.bilibili.com/video/av19817183/?p=19)



### 常用的SQLAlchemy字段类型

| **类型名**   | **python****中类型** | **说明**                                            |
| ------------ | -------------------- | --------------------------------------------------- |
| Integer      | int                  | 普通整数，一般是32位                                |
| SmallInteger | int                  | 取值范围小的整数，一般是16位                        |
| BigInteger   | int或long            | 不限制精度的整数                                    |
| Float        | float                | 浮点数                                              |
| Numeric      | decimal.Decimal      | 普通整数，一般是32位                                |
| String       | str                  | 变长字符串                                          |
| Text         | str                  | 变长字符串，对较长或不限长度的字符串做了优化        |
| Unicode      | unicode              | 变长Unicode字符串                                   |
| UnicodeText  | unicode              | 变长Unicode字符串，对较长或不限长度的字符串做了优化 |
| Boolean      | bool                 | 布尔值                                              |
| Date         | datetime.date        | 时间                                                |
| Time         | datetime.datetime    | 日期和时间                                          |
| LargeBinary  | str                  | 二进制文件                                          |

### 常用的SQLAlchemy列选项

| **选项名**  | **说明**                                          |
| ----------- | ------------------------------------------------- |
| primary_key | 如果为True，代表表的主键                          |
| unique      | 如果为True，代表这列不允许出现重复的值            |
| index       | 如果为True，为这列创建索引，提高查询效率          |
| nullable    | 如果为True，允许有空值，如果为False，不允许有空值 |
| default     | 为这列定义默认值                                  |

### **常用的SQLAlchemy**关系选项

| **选项名**    | **说明**                                                     |
| ------------- | ------------------------------------------------------------ |
| backref       | 在关系的另一模型中添加反向引用                               |
| primaryjoin   | 明确指定两个模型之间使用的联结条件                           |
| uselist       | 如果为False，不使用列表，而使用标量值                        |
| order_by      | 指定关系中记录的排序方式                                     |
| secondary     | 指定多对多中记录的排序方式                                   |
| secondaryjoin | 在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件 |

#### 示例:

```python
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


```

