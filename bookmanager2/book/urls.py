from django.urls import path
from book.views import create_book,shop,register,json,method

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
# converter 转换器类
# type_name  转换器名字
register_converter(MobileConverter,'phone')


# 这个是固定写法 urlpatterns = []
urlpatterns = [
    # path(路由，视图函数名)
    path('create/', create_book),

    # 验证path中路径参数数据的数据类型---方法二: 转换器
    path('<int:city_id>/<int:mobile>/', shop),

    path('register/',register),
    path('json/',json),
    path('method/',method),
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