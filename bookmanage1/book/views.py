from django.shortcuts import render, HttpResponse

# Create your views here.

from book.models import BookInfo


def index(request):
    # 再这里实现 增删改查

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

from book.models import BookInfo
from book.models import PeopleInfo

####################增加数据########################
# 方式一
# book = BookInfo(
#     name='Django',
#     pub_date='2000-1-1',
#     readcount=10
# )
# 必须要调用 对象的save方法才能将数据保存到数据库中
# book.save()

# 方式二
# objects -- 相当于一个代理 实现增删改查
# BookInfo.objects.create(
#     name='测试开发入门',
#     pub_date='2020-1-1',
#     readcount=100
# )
# 直接将数据保存到了数据库中


####################修改数据########################
# 方式1
# select * from bookinfo where id=6
# book = BookInfo.objects.get(id=6)
# book.name = '运维开发入门'
# 想要保存数据 需要调用 对象的save方法
# book.save()

# 方式二
# filter 过滤
BookInfo.objects.filter(id=6).update(name='爬虫入门', commentcount=666)
# 错误的
# BookInfo.objects.get(id=5).update(name='5555',commentcount=999)


####################删除数据########################
# 删除分两种:
# 物理删除(这条记录的数据 删除)
# 逻辑删除(修改标记位 例如 is_delete=False)
# 方式1
# book = BookInfo.objects.get(id=6)
# book.delete()

# 方式2
# BookInfo.objects.get(id=6).delete()
# BookInfo.objects.filter(id=5).delete()


####################查询数据########################
# get查询单一结果，如果不存在会抛出模型类.DoesNotExist异常
# try:
#     book = BookInfo.objects.get(id=1)
# except BookInfo.DoesNotExist:
#     print('查询结果不存在')

# all查询多个结果
BookInfo.objects.all()
from book.models import PeopleInfo

PeopleInfo.objects.all()

# count查询结果数量
BookInfo.objects.all().count()
BookInfo.objects.count()

###########################过滤查询##########################
# 实现SQL中的where功能，包括
#     filter过滤出多个结果
#     exclude排除掉符合条件剩下的结果
#     get过滤单一结果

# 模型类名.objects.filter(属性名__运算符=值)       获取n个结果  n=0,1,2,...
# 模型类名.objects.exclude(属性名__运算符=值)      获取n个结果  n=0,1,2,...
# 模型类名.objects.get(属性名__运算符=值)          获取1个结果 或者 异常

# 运算符:
#     相等
#         exact：表示判等
#     模糊查询
#         contains：是否包含
#         startswith、endswith：以指定值开头或结尾
#     空查询
#         isnull：是否为null
#     范围查询
#         in：是否包含在范围内
#     比较查询
#         gt大于 (greater then)
#         gte大于等于 (greater then equal)
#         lt小于 (less then)
#         lte小于等于 (less then equal)
#         不等于的运算符，使用exclude()过滤器
#     日期查询
#         year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算

# 查询编号为1的图书
book = BookInfo.objects.get(id=1)  # 简写形式 （属性名=值）
# exact：表示判等
book = BookInfo.objects.get(id__exact=1)  # 完整形式  (id__exact=1)
# pk primary key 主键
BookInfo.objects.get(pk=1)
BookInfo.objects.get(id=1)
BookInfo.objects.filter(id=1)

# 查询书名包含'湖'的图书
# contains：是否包含
BookInfo.objects.filter(name__contains='湖')

# 查询书名以'部'结尾的图书
# startswith、endswith：以指定值开头或结尾
BookInfo.objects.filter(name__endswith='部')

# 查询书名为空的图书
#     isnull：是否为null
BookInfo.objects.filter(name__isnull=True)

# 查询编号为1或3或5的图书
# in：是否包含在范围内
BookInfo.objects.filter(id__in=[1, 3, 5])

# 查询编号大于3的图
# gt大于 (greater then)
# gte大于等于 (greater then equal)
# lt小于 (less then)
# lte小于等于 (less then equal)
BookInfo.objects.filter(id__gt=3)

# 查询编号不等于3的书籍
# 不等于的运算符，使用exclude()过滤器
BookInfo.objects.exclude(id=3)

# 查询1980年发表的图书
# year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算
BookInfo.objects.filter(pub_date__year=1980)

# 查询1990年1月1日后发表的图书
BookInfo.objects.filter(pub_date__gt='1990-1-1')
# 错误的
# BookInfo.objects.filter(pub_date__gt='199011')


###########################F对象##############################
# 导入F对象
from django.db.models import F

# 使用： 2个属性的比较
# 语法形式： 以filter为例  模型类名.objects.filter(属性名__运算符=F('第二个属性名'))

# 查询阅读量大于等于评论量的图书
BookInfo.objects.filter(readcount__gte=F('commentcount'))

#########################并且查询#############################
# 并且查询
# 查询阅读量大于20，并且编号小于3的图书。
BookInfo.objects.filter(readcount__gt=20).filter(id__lt=3)
# 两种方式一致
BookInfo.objects.filter(readcount__gt=20, id__lt=3)

###########################Q对象##############################
# 导入Q对象
from django.db.models import Q

# 或者查询
# 或者语法：  模型类名.objects.filter(Q(属性名__运算符=值)|Q(属性名__运算符=值)|...)
# 并且语法：  模型类名.objects.filter(Q(属性名__运算符=值)&Q(属性名__运算符=值)&...)
# not 非 语法：  模型类名.objects.filter(～Q(属性名__运算符=值))

# 查询阅读量大于20，或者编号小于3的图书。
BookInfo.objects.filter(Q(readcount__gt=20) | Q(id__lt=3))

# 查询编号不等于3的书籍
BookInfo.objects.exclude(id=3)
BookInfo.objects.filter(~Q(id=3))

#############聚合函数#####################################

from django.db.models import Sum, Max, Min, Avg, Count

# 模型类名.objects.aggregate(Xxx('字段名'))
BookInfo.objects.aggregate(Sum('readcount'))

#########################排序############################
BookInfo.objects.all().order_by('readcount')



###################2个表的级联操作##############################
# 查询书籍为1的所有人物信息
# 先获取了id为1的书籍
book = BookInfo.objects.get(id=1)
# 1对多的关系模型中
# 系统会为我们自动添加一个关联模型 类名小写_set
# 再获取所有信息
book.peopleinfo_set.all()

# 查询人物为1的书籍信息
person = PeopleInfo.objects.get(id=1)
# PeopleInfo中设置了外键book就可以直接通过下面方式查询
person.book.name
person.book.pub_date
person.book.readcount
person.book.commentcount
person.book.is_delete



###############关联过滤查询#####################
# 语法形式
# 查询1的数据， 条件为 n
# 模型类名.objects.filter(关联模型类名小写__字段名__运算符=值)

# 查询图书，要求图书人物为"郭靖"
BookInfo.objects.filter(peopleinfo__name__exact='郭靖')
BookInfo.objects.filter(peopleinfo__name='郭靖')

# 查询图书，要求图书中人物的描述包含"八"
BookInfo.objects.filter(peopleinfo__description__contains='八')

# 查询书名为“天龙八部”的所有人物
# PeopleInfo中有与书名相关的book外键,所以直接用book
PeopleInfo.objects.filter(book__name='天龙八部')
PeopleInfo.objects.filter(book__name__exact='天龙八部')

# 查询图书阅读量大于30的所有人物
PeopleInfo.objects.filter(book__readcount__gt=30)
