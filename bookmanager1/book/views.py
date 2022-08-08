from django.shortcuts import render,HttpResponse

# Create your views here.

from book.models import BookInfo
def index(request):

    #再这里实现 增删改查
    # [book.id for book in BookInfo.objects.all()]
    # [book.id for book in BookInfo.objects.all()]
    # [book.id for book in BookInfo.objects.all()]
    # [book.id for book in BookInfo.objects.all()]
    # [book.id for book in BookInfo.objects.all()]
    #
    books = BookInfo.objects.all()
    print(books)
    # [book.id for book in books]
    # [book.id for book in books]
    # [book.id for book in books]
    # [book.id for book in books]
    # [book.id for book in books]

    return HttpResponse('index')


# name='abc'
# mysql 的数据存储在 硬盘
# redis 的数据存储在 内存
# 我把硬盘的数据保存在内存 也称之为 缓存

####################增加数据########################
from book.models import BookInfo
# 方式一
book=BookInfo(
    name='Django',
    pub_date='2000-1-1',
    readcount=10
)
# 必须要调用 对象的save方法才能将数据保存到数据库中
book.save()

# 方式二
# objects -- 相当于一个代理 实现增删改查
BookInfo.objects.create(
    name='测试开发入门',
    pub_date='2020-1-1',
    readcount=100
)
# 直接将数据保存到了数据库中


####################修改数据########################
# 方式1
# select * from bookinfo where id=6
book=BookInfo.objects.get(id=6)
book.name='运维开发入门'
# 想要保存数据 需要调用 对象的save方法
book.save()

# 方式二
# filter 过滤
BookInfo.objects.filter(id=6).update(name='爬虫入门',commentcount=666)
# 错误的
# BookInfo.objects.get(id=5).update(name='5555',commentcount=999)


####################删除数据########################
# 删除分两种:
    # 物理删除(这条记录的数据 删除)
    # 逻辑删除(修改标记位 例如 is_delete=False)
# 方式1
book=BookInfo.objects.get(id=6)
book.delete()

# 方式2
BookInfo.objects.get(id=6).delete()
BookInfo.objects.filter(id=5).delete()








