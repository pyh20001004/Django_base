from django.shortcuts import render,HttpResponse
from book.models import BookInfo,PeopleInfo
# Create your views here.

# HttpRequest对象
# 利用HTTP协议向服务器传参有四种途径
#     1.提取URL的特定部分，如/weather/beijing/2018，可以在服务器端的路由中用正则表达式截取；
#     2.查询字符串（query string)，形如key1=value1&key2=value2；
#     3.请求体（body）中发送的数据，比如表单数据、json、xml；
#     4.在http报文的头（header）中。

def create_book(request):
    book=BookInfo.objects.create(
        name='DV',
        pub_date='2000-1-1',
        readcount=10,
    )
    return HttpResponse("create")



def shop(request,city_id,mobile):

    # 验证path中路径参数数据的数据类型---方法一: 在视图函数里面验证(正则验证)

    # import re
    # if not re.match('\d{5}',mobile): # 验证是否为长度为5,数据类型为int整型
    #     return HttpResponse('没有此商品')
    # 方法二: 在urls.py里

    # 1.URL路径参数
    # print(city_id,shop_id)

    # 2.查询字符串参数
    query_params=request.GET
    # print(query_params)
    # <QueryDict: {'a': ['333', '444'], 'b': ['555']}>

    # data=query_params.get('a') # 和下面两种方法都能获取
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
    # print(data)
    # <QueryDict: {'username': ['itcast'], 'password': ['123']}>

    return HttpResponse('ok')


########### 3.2 非表单类型 非表单类型 Non-Form Data ###########
#     非表单类型的请求体数据，Django无法自动解析，
#     可以通过request.body属性获取最原始的请求体数据，
#     自己按照请求体格式（JSON、XML等）进行解析。
#     request.body返回bytes类型。
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
# method：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'。
# user：请求的用户对象。
# path：一个字符串，表示请求的页面的完整路径，不包含域名和参数部分。
# encoding：一个字符串，表示提交的数据的编码方式。
#     如果为None则表示使用浏览器的默认设置，一般为utf-8。
#     这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，
#     接下来对属性的任何访问将使用新的encoding值。
# FILES：一个类似于字典的对象，包含所有的上传文件。
def method(request):
    # print(request.method)

    return HttpResponse('method')