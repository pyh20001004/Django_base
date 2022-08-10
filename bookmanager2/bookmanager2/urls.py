"""bookmanager2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from book.views import create_book
urlpatterns = [
    path('admin/', admin.site.urls),
    # path(路由，视图函数名)
    # path('index/',index),

    # 网页访问的话需要工程(bookmanager)的路由加上子应用(book)的路由,
    # 我们这里把工程的路由设为空,所以网页访问时只需要根据子应用的路由访问
    # 后面我们只需要在子应用的urls里设置路由
    path('', include('book.urls'))
]
