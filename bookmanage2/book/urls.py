from django.urls import path
from book.views import home,create_book,shop,register,json,method,response
from book.views import set_cookie,get_cookie,set_session,get_session
from book.views import login
from book.views import LoginView,OrderView

from django.urls import converters
from django.urls.converters import register_converter

# 1. 定义转换器
class MobileConverter:
    # 验证数据的关键是： 正则
    regex = '1[3-9]\d{9}'

    # 验证没有问题的数据，给视图函数
    def to_python(self, value):
        return value

    # def to_url(self, value):
    #     # 将匹配结果用于反向解析传值时使用 (了解)
    #     return value

# 2. 先注册转换器，才能在第三步中使用
# 格式: register_converter(converter,type_name)
# converter 转换器类
# type_name  转换器名字
register_converter(MobileConverter,'phone')


# 这个是固定写法 urlpatterns = []
urlpatterns = [
    # path(路由，视图函数名)
    # 设置首页home
    path('', home),
    path('create/', create_book),

    # 验证path中路径参数数据的数据类型---方法二: 转换器(复用性强)
    # <转换器名字：变量名>
    # 转换器会对变量数据进行 正则的验证
    # 这里的int是converters.py文件里封装好的转换器(复制在下面多行注释里)，phone是我们自己定义的转换器
    path('<int:city_id>/<phone:mobile>/', shop),

    path('register/',register),
    path('json/',json),
    path('method/',method),
    path('res/',response),
    path('set_cookie/',set_cookie),
    path('get_cookie/',get_cookie),
    path('set_session/',set_session),
    path('get_session/',get_session),
    path('login/',login),

    #################### 类视图 ####################
    # 配置路由时，使用类视图的 as_view() 方法来添加
    # 因为 as_view 函数是一个闭包函数,加上()来调用内部的 view 函数
    path('163login/',LoginView.as_view()),
    path('order/',OrderView.as_view()),

]

"""
converters.py中的IntConverter类(<int:city_id>/<int:mobile>中的int原理)

class IntConverter:
    regex = '[0-9]+'

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)
"""