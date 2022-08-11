from django.shortcuts import render, HttpResponse, redirect
from book.models import BookInfo,PeopleInfo
# Create your views here.

######################################## HttpRequest对象(Http请求对象) ########################################
"""
利用HTTP协议向服务器传参有四种途径
    1.提取URL的特定部分，如/weather/beijing/2018，可以在服务器端的路由中用正则表达式截取；
    2.查询字符串（query string)，形如key1=value1&key2=value2；
    3.请求体（body）中发送的数据，比如表单数据、json、xml；
    4.在http报文的头（header）中。
"""

def home(request):

    return HttpResponse('首页!!!')

def create_book(request):
    book=BookInfo.objects.create(
        name='DV',
        pub_date='2000-1-1',
        readcount=10,
    )
    return HttpResponse("create")


def shop(request,city_id,mobile):

    # 验证path中路径参数数据的数据类型---方法一: 在视图函数里面验证(正则验证)(复用性弱)
    # import re
    # if not re.match('\d{5}',mobile): # 验证是否为长度为5,数据类型为int整型
    #     return HttpResponse('没有此商品')
    # 方法二: 在urls.py里


    # 1.URL路径参数
    # print(city_id,mobile)

    # 2.查询字符串参数
    query_params=request.GET
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

    data=request.POST
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
    body=request.body
    # print(body)
    # b'{\n"name":"itcast",\n"age":20\n}'  bytes类型的数据

    # 转化为字符串类型
    body_str=body.decode()
    # print(body_str)
    # {
    #     "name": "itcast",
    #     "age": 20
    # }

    # JSON形式的字符串 可以转换为 Python的字典
    # json.loads      JSON字符串转换为Python的字典
    # json.dumps      Python的字典转换为JSON字符串
    import json
    body_dict=json.loads(body_str)
    # print(body_dict)

    ########### 4.请求头 ##########
    # 可以通过request.META属性获取请求头headers中的数据，request.META为字典类型
    data=request.META
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
    info={
        'name':'itcast',
        'address':'diaomao'
    }
    girl_firends=[
        {
            'name':'DV',
            'address':'jack'
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
    data=json.dumps(girl_firends)
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
    response=HttpResponse('set_cookie')
    # key, value=''
    # max_age 设置过期时间 是一个秒数 从响应开始 计数的一个秒数
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

    return HttpResponse(name+"-----"+password)
