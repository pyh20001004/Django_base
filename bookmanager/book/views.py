from django.shortcuts import render

# Create your views here.
"""
视图
所谓的视图 其实就是python函数
视图函数有2个要求：
    1. 视图函数的第一个参数就是接收请求。这个请求其实就是 HttpRequest的类对象
    2. 必须返回一个响应
"""
# request
from django.http import HttpRequest
from django.http import HttpResponse

# 我们期望用户输入 http://127.0.0.1:8000/index/
# 来访问视图函数

# 在settings.py的TEMPLATES中有 'DIRS': [os.path.join(BASE_DIR,'templates')], 的时候
#     优先去项目根目录的templates中寻找(提前先配置: [os.path.join(BASE_DIR,'templates')])[不配置就是无效]
# 在settings.py的TEMPLATES中 'DIRS': [], 的时候
#     根据APP的注册顺序，在每个APP下的templates目录中寻找user_list.html文件
def index(request):
    # return  HttpResponse('ok')

    # render 渲染模板
    # request, template_name, context=None
    # request,           请求
    # template_name,    模板名字
    # context=None
    # 100/0
    # 模拟数据查询
    name = "DV"
    context = {
        'name': '马上双11，点击有惊喜'
    }
    roles = ["屌毛", "老八", "傻屌"]
    user_info = {"name": "李伟", "salary": 000000, 'role': "CTO0"}
    data_list = [
        {"name": "aaa", "salary": 11111, 'role': "CTO1"},
        {"name": "bbb", "salary": 22222, 'role': "CTO2"},
        {"name": "ccc", "salary": 33333, 'role': "CTO3"},
    ]
    return render(request,'book/index.html',{'n1':name,'n2':context,'n3':roles,'n4':user_info,'n5':data_list})