from django.shortcuts import render, HttpResponse, redirect
from book.models import BookInfo, PeopleInfo

# Create your views here.


def home(request):
    return HttpResponse('首页!!!')


def create_book(request):
#     book = BookInfo.objects.create(
#         name='DV',
#         pub_date='2000-1-1',
#         readcount=10,
#     )
    return HttpResponse("create")



######################################## HttpRequest对象(Http请求对象) ########################################
"""
利用HTTP协议向服务器传参有四种途径
    1.提取URL的特定部分，如/weather/beijing/2018，可以在服务器端的路由中用正则表达式截取；
    2.查询字符串（query string)，形如key1=value1&key2=value2；
    3.请求体（body）中发送的数据，比如表单数据、json、xml；
    4.在http报文的头（header）中。
"""
def shop(request, city_id, mobile):
    # 验证path中路径参数数据的数据类型---方法一: 在视图函数里面验证(正则验证)(复用性弱)
    # import re
    # if not re.match('\d{5}',mobile): # 验证是否为长度为5,数据类型为int整型
    #     return HttpResponse('没有此商品')
    # 方法二: 在urls.py里

    ########### 1.URL路径参数 ###########
    # print(city_id,mobile)

    ########### 2.查询字符串参数 ###########
    query_params = request.GET
    # print(query_params)
    # <QueryDict: {'a': ['333', '444'], 'b': ['555']}>

    # data=query_params.get('a') # 和下面方法都能获取
    # data=query_params['a']
    # print(data)

    # QueryDict 具有字典的特性  还具有一键多值
    # 一键多值时 get获取只能获取最后一个值，所以要使用 getlist获取全部值
    # data = query_params.getlist('a')
    # print(data)

    return HttpResponse('李伟是傻屌')


########### 1.URL路径参数 ###########
"""
URL路径参数
http://ip:port/path1/path2/

在urls.py定义关键字 city_id,shop_id 来获取path1和path2等参数，然后将参数传递给函数
"""

########### 2.查询字符串参数 ###########
"""
查询字符串
http://ip:port/path/path/?key=value&key1=value1

url 以 ？ 为分割 分为2部分
？前边为 请求路径
？后边为 查询字符串  查询字符串 类似于字典 key=value 多个数据采用&拼接

使用request.GET获取
重要：查询字符串不区分请求方式，即假使客户端进行POST方式的请求，
依然可以通过request.GET获取请求中的查询字符串数据。
"""


########### 3.请求体（body）中发送的数据 ###########
########### 3.1 表单类型 Form Data ###########
#     前端发送的表单类型的请求体数据，可以通过request.POST属性获取，返回QueryDict对象
def register(request):
    data = request.POST
    print(data)
    # <QueryDict: {'username': ['itcast'], 'password': ['123']}>

    return HttpResponse('ok')


########### 3.2 非表单类型 非表单类型 Non-Form Data ###########
"""
非表单类型的请求体数据，Django无法自动解析，
可以通过request.body属性获取最原始的请求体数据，
自己按照请求体格式（JSON、XML等）进行解析。
request.body返回bytes类型。
"""
def json(request):
    # json数据不能通过 request.POST获取数据,要使用request.body
    body = request.body
    # print(body)
    # b'{\n"name":"itcast",\n"age":20\n}'  bytes类型的数据

    # 转化为字符串类型
    body_str = body.decode()
    # print(body_str)
    # {
    #     "name": "itcast",
    #     "age": 20
    # }

    # JSON形式的字符串 可以转换为 Python的字典
    # json.loads      JSON字符串转换为Python的字典
    # json.dumps      Python的字典转换为JSON字符串
    import json
    body_dict = json.loads(body_str)
    # print(body_dict)

    ########### 4.请求头 ##########
    # 可以通过request.META属性获取请求头headers中的数据，request.META为字典类型
    data = request.META
    # print(data)
    # print(data['SERVER_PORT'])

    return HttpResponse('json')


########### 其他常用HttpRequest对象属性 ###########
"""
method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'。
user：请求的用户对象。
path：一个字符串，表示请求的页面的完整路径，不包含域名和参数部分。
encoding：一个字符串，表示提交的数据的编码方式。
    如果为None则表示使用浏览器的默认设置，一般为utf-8。
    这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，
    接下来对属性的任何访问将使用新的encoding值。
FILES：一个类似于字典的对象，包含所有的上传文件。
"""
def method(request):
    # print(request.method)

    return HttpResponse('method')


######################################## HttpResponse对象(HTTP应答对象) ########################################
"""
视图在接收请求并处理后，必须返回HttpResponse对象或子对象。
HttpRequest对象由Django创建，HttpResponse对象由开发人员创建。
"""
def response(request):
    ########### 1.HttpResponse ###########
    """
    1.可以使用django.http.HttpResponse来构造响应对象。
    HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
    """
    # response=HttpResponse('res',status=200)
    """
    HTTP状态代码必须是100到599之间的整数
    1xx   消息
    2xx   成功
      200 ok
    3xx   重定向
    4xx   请求错误
      404 找不到页面   路由有问题
      403 禁止访问    权限问题
      405 请求方式不被允许
    5xx   服务器错误
    """

    """
    2.也可通过HttpResponse对象属性来设置响应体、响应体数据类型、状态码
    content：表示返回的内容。
    status_code：返回的HTTP响应状态码。
    响应头可以直接将HttpResponse对象当做字典进行响应头键值对的设置
    """
    # response['name']='itcast'

    ########### 2.HttpResponse子类 ###########
    # Django提供了一系列HttpResponse的子类，可以快速设置状态码
    """
    from django.http import HttpResponse,HttpResponseNotFound
        HttpResponseRedirect              301
        HttpResponsePermanentRedirect     302
        HttpResponseNotModified           304
        HttpResponseBadRequest            400
        HttpResponseNotFound              404
        HttpResponseForbidden             403
        HttpResponseNotAllowed            405
        HttpResponseGone                  410
        HttpResponseServerError           500
    """

    ########### 3.JsonResponse ###########
    from django.http import JsonResponse
    """
    若要返回json数据，可以使用JsonResponse来构造响应对象，作用：
    帮助我们将数据转换为json字符串
    设置响应头Content - Type为application / json
    """
    info = {
        'name': 'itcast',
        'address': 'diaomao'
    }
    girl_firends = [
        {
            'name': 'DV',
            'address': 'jack'
        },
        {
            'name': 'WF',
            'address': 'rose'
        }
    ]

    # data 返回的响应数据 一般是字典类型
    # response = JsonResponse(data=info)

    """
        safe = True 是表示 我们的data 是字典数据
        JsonResponse 可以把字典转换为json
        现在给了一个非字典数据，出了问题 我们自己负责
    """
    # response=JsonResponse(data=girl_firends,safe=False)

    # 也可以先把数据转换为JSON数据再返回，就不需要使用JsonResponse
    import json
    """
    json.loads      JSON数据转换为Python数据
    json.dumps      Python数据转换为JSON数据
    """
    data = json.dumps(girl_firends)
    response = HttpResponse(data)

    ########### 4.redirect重定向 ###########
    # 重新定制方向，跳转到别的网址
    # return redirect('http://www.itcast.cn')

    return response


######################################## 状态保持 ########################################
"""
浏览器请求服务器是无状态的。
无状态：指一次用户请求时，浏览器、服务器无法知道之前这个用户做过什么，每次请求都是一次新的请求。
无状态原因：浏览器与服务器是使用Socket套接字进行通信的，服务器将请求结果返回给浏览器之后，
          会关闭当前的Socket连接，而且服务器也会在处理页面完毕之后销毁页面对象。
有时需要保持下来用户浏览的状态，比如用户是否登录过，浏览过哪些商品等
实现状态保持主要有两种方式：
    在客户端存储信息使用 Cookie
    在服务器端存储信息使用 Session
"""

########### 1.Cookie ###########
"""
Cookie是由服务器端生成，发送给User-Agent（一般是浏览器），
浏览器会将Cookie的 key/value 保存到某个目录下的文本文件内，
下次请求同一网站时就发送该Cookie给服务器（前提是浏览器设置为启用cookie）。

Cookie的特点
    1. Cookie以键值对的格式进行信息的存储。
    2. Cookie基于域名安全，不同域名的Cookie是不能互相访问的，如访问itcast.cn时向浏览器中写了Cookie信息，
        使用同一浏览器访问baidu.com时，无法访问到itcast.cn写的Cookie信息。
    3. 当浏览器请求某网站时，会将浏览器存储的跟网站相关的所有Cookie信息提交给网站服务器。
"""

"""
Cookie流程:
    第一次请求，携带 查询字符串
    http://127.0.0.1:8000/set_cookie/?username=itcast&password=123
    服务器接收到请求之后，获取username.服务器设置cookie信息，cookie信息包括 username
    浏览器接收到服务器的响应之后，应该把cookie保存起来
    
    第二次及其之后的请求，我们访问http://127.0.0.1:8000 都会携带cookie信息。 服务器就可以读取cookie信息，来判断用户身份
"""
def set_cookie(request):
    # 获取查询字符串数据
    username = request.GET.get('username')
    password = request.GET.get('password')

    # 1. 服务器设置Cookie信息
    # 可以通过HttpResponse对象中的set_cookie方法来设置cookie。
    response = HttpResponse('set_cookie')
    # key, value=''
    # max_age 设置Cookie过期时间 是一个秒数 从响应开始 计数的一个秒数
    response.set_cookie('name', username, max_age=60 * 60)
    response.set_cookie('password', password)

    # 3. 删除Cookie
    # 可以通过HttpResponse对象中的delete_cookie方法来删除。
    # response.delete_cookie('name')

    return response


def get_cookie(request):
    # 2. 获取cookie
    print(request.COOKIES)
    # request.COOKIES 字典数据
    name = request.COOKIES.get('name')
    password = request.COOKIES.get('password')

    return HttpResponse(name + "-----" + password)


########### 1.Session ###########
"""
session 是保存在服务器端 -- 数据相对安全
session需要依赖于cookie
"""

########### 1.Session ###########
"""
Session流程:
    第一次请求 http://127.0.0.1:8000/set_session/?username=itheima 。我们在服务器端设置sesison信息
    服务器同时会生成一个sessionid的cookie信息。
    浏览器接收到这个信息之后，会把cookie数据保存起来
    
    第二次及其之后的请求 都会携带这个cookie里的sessionid. 服务器会验证这个sessionid. 验证没有问题会读取相关数据。实现业务逻辑
"""
def set_session(request):
    # 1.模拟 获取用户信息
    username = request.GET.get('username')
    # 2.设置session信息
    # 假如 我们通过模型查询 查询到了 用户的信息

    request.session['user_id'] = 1
    request.session['username'] = username

    # clear 删除session里的数据，但是 key有保留
    # request.session.clear()

    # flush 是删除所有的数据，包括key
    # request.session.flush()

    # 删除session中的指定键及值，在存储中只删除某个键及对应的值。
    # del request.session['键']

    # 设置session的有效期
    # request.session.set_expiry(3600)

    return HttpResponse('set_session')


def get_session(request):
    # user_id=request.session['user_id']
    # username=request.session['username']
    # 获取字典的时候尽量使用get,能够减少异常的发生
    user_id = request.session.get('user_id')
    username = request.session.get('username')

    content = '{},{}'.format(user_id, username)  # 相当于'%s,%s'%user_id,%username

    return HttpResponse(content)


########### 2.存储方式 ###########
"""
在settings.py文件中，可以设置session数据的存储方式，可以保存在数据库、本地缓存等。
2.1 数据库
    存储在数据库中，如下设置可以写，也可以不写，这是默认存储方式。
2.2 本地缓存
    存储在本机内存中，如果丢失则不能找回，比数据库的方式读写更快。
2.3 混合存储
    优先从本机内存中存取，如果没有则从数据库中存取。
2.4 Redis(在settings.py中配置)
在redis中保存session，需要引入第三方扩展，我们可以使用django-redis来解决。
"""

########### 3.Session操作 ###########
"""
1）以键值对的格式写session。
    request.session['键']=值
2) 根据键读取值。
    request.session.get('键',默认值)
3）清除所有session，在存储中删除值部分。
    request.session.clear()
4）清除session数据，在存储中删除session的整条数据。
    request.session.flush()
5）删除session中的指定键及值，在存储中只删除某个键及对应的值。
    del request.session['键']
6）设置session的有效期
    request.session.set_expiry(value)
    如果value是一个整数，session将在value秒没有活动后过期。
    如果value为0，那么用户session的Cookie将在用户的浏览器关闭时过期。
    如果value为None，那么session有效期将采用系统默认值， 默认为两周，可以通过在settings.py中设置SESSION_COOKIE_AGE来设置全局默认值。
"""


######################################## 类视图 ########################################


# 如何在一个视图中处理get和post请求

########## 方式一: 注册视图处理get和post请求(比较乱,不建议使用) ##########
def login(request):
    print(request.method)

    if request.method == 'GET':
        return HttpResponse('get 逻辑')
    elif request.method == 'POST':
        return HttpResponse('post 逻辑')


########## 方式二: 在Django中也可以使用类来定义一个视图，称为类视图。(建议使用) ##########
"""
类视图的定义

class 类视图名字（View）:

    def get(self,request):

        return HttpResponse('xxx')

    def http_method_lower(self,request):

        return HttpResponse('xxx')

1. 继承自View
2. 类视图中的方法 是采用 http方法小写来区分不同的请求方式
"""
from django.views import View
class LoginView(View):

    def get(self, request):
        return HttpResponse('get get get!!!')

    def post(self, request):
        return HttpResponse('post post post!!!')


class Person(object):
    # 对象方法
    def play(self):
        pass

    @classmethod
    def say(cls):
        pass

    @staticmethod
    def eat():
        pass

Person.say()

# cls=Person    这里cls就是类名
#
# Person()   # 两种都是调用类方法
# cls()



#################### 多继承和MRO的顺序 ####################

"""
我的订单、个人中心页面
如果登录用户 可以访问
如果未登录用户 不应该访问，应该跳转到登录页面

定义一个订单、个人中心 类视图

如果定义我有没有登录呢？？？ 我们以登录 后台站点为例
"""

# 判断用户是否登录---方法二(推荐)
from django.contrib.auth.mixins import LoginRequiredMixin
# LoginRequiredMixin 作用 判断 只有登录用户才可以访问页面
"""
LoginRequiredMixin 内部会进行用户是否登录的判断(一登录admin站点)
如果登录成功, 则显示页面
如果没有登录成功,系统会为我们跳转到系统的 accounts/login/ 页面
"""
# 多继承是根据 MRO 的顺序执行,所以要把 LoginRequiredMixin 放在View前面,先判断是否登录,再执行View
class OrderView(LoginRequiredMixin,View):

    def get(self,request):

        # 判断用户是否登录---方法一(比较麻烦,不推荐)
        # isLogin=True
        # if isLogin:
        #     return HttpResponse('你没有登录，跳转到整理页面中～～～～')

        return HttpResponse('GET 我的订单页面，这个页面必须登录')

    def post(self,requset):
        return HttpResponse('POST 我的订单页面，这个页面必须登录')

"""
多继承的语言
    Python,C++
"""



#################### 中间件 ####################
"""
1 中间件的定义方法
Django在中间件中预置了六个方法，这六个方法会在不同的阶段自动执行，对输入或输出进行干预。
    1.1 初始化方法：
        启动Django程序，初始化中间件时，自动调用一次，用于确定是否启用当前中间件
        def __init__(self, get_response=None):
          pass
    1.2 处理请求前的方法：(重要)
        在处理每个请求前，自动调用，返回None或HttpResponse对象
        def process_request(self, request):
          pass
    1.3 处理视图前的方法：（重要）
        在处理每个视图前，自动调用，返回None或HttpResponse对象
        def process_view(self, request, view_func, view_args, view_kwargs):
          pass
    1.4 处理模板响应前的方法：
        在处理每个模板响应前，自动调用，返回实现了render方法的响应对象
        def process_template_response(self, request, response):
          pass
    1.5 处理响应后的方法：（重要）
        在每个响应返回给客户端之前，自动调用，返回HttpResponse对象
        def process_response(self, request, response):
          pass
    1.6 异常处理：
        当视图抛出异常时，自动调用，返回一个HttpResponse对象
        def process_exception(self, request,exception):
          pass
"""

# 导入中间件的父类
from django.utils.deprecation import MiddlewareMixin
# 写好后在 settings.py 的 MIDDLEWARE 里注册后才能使用
class TestMiddleware_1(MiddlewareMixin):

    def process_request(self,request):
        print('11111 每次请求前 都会执行调用')

        username=request.COOKIES.get('name')
        if username is None:
            print("没有用户信息")
        else:
            print("有用户信息")

    def process_response(self,reequest,response):
        print('每次响应前 都会执行调用 11111')
        return response

class TestMiddleware_2(MiddlewareMixin):

    def process_request(self,request):
        print('22222 每次请求前 都会执行调用')

        username=request.COOKIES.get('name')
        if username is None:
            print("没有用户信息")
        else:
            print("有用户信息")

    def process_response(self,reequest,response):
        print('每次响应前 都会执行调用 22222')
        return response






















