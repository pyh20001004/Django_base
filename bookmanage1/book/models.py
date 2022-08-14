from django.db import models

# Create your models here.

"""
1. 我们的模型类 需要继承自 models.Model
2. 系统会自动为我们添加一个主键--id
3. 定义属性(字段)
    属性名=model.类型（选项）

    2.1 属性名对应就是字段名
        字段名不要使用 python，mysql等关键字
        不要使用连续的下划线(__)
    2.1 类型 MySQL的类型
    2.3 选项  是否有默认值，是否唯一，是否为null
            CharField 必须设置 max_length
            verbose_name 主要是 admin站点使用          
4. 改变表的名称
    默认表的名称是： 子应用名_类名 都是小写
    修改表的名字
    create table `qq_user` (
        id int ,
        name varchar(10) not null default ''
    )

"""


class BookInfo(models.Model):

    name = models.CharField(max_length=10, unique=True) # 书名
    pub_date = models.DateField(null=True) # 发布日期
    readcount = models.IntegerField(default=0) # 阅读量
    commentcount = models.IntegerField(default=0) # 评论量
    is_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'bookinfo'  # 修改表的名字
        verbose_name = '书籍管理'  # admin站点使用的（了解）

    # 1对多的关系模型中
    # 系统会为我们自动添加一个关联模型 类名小写_set
    # peopleinfo_set=[PeopleInfo,PeopleInfo,...]

    # peopleinfo

    def __str__(self):
        return self.name

class PeopleInfo(models.Model):
    # 定义一个有序字典
    GENDER_CHOICE = (
        (1, 'male'),
        (2, 'female')
    )

    name = models.CharField(max_length=10, unique=True) # 人物名字
    gender = models.SmallIntegerField(choices=GENDER_CHOICE, default=1) # 性别
    description = models.CharField(max_length=100, null=True) # 人物描述
    is_delete = models.BooleanField(default=False)

    # 设置外键(键名.models.ForeignKey(类名,on_delete选项))
    # 系统会自动为外键添加 _id

    # 外键的级联操作(on_delete选项)
    # 主表 和 从表
    # 1 对 多
    # 书籍    对  人物

    # 在设置外键时，需要通过on_delete选项指明主表删除数据时，对于外键引用表数据如何处理，在django.db.models中包含了可选常量：
        # CASCADE级联，删除主表数据时连通一起删除外键表中数据
        # PROTECT保护，通过抛出ProtectedError异常，来阻止删除主表中被外键应用的数据
        # SET_NULL设置为NULL，仅在该字段null = True允许为null时可用
        # SET_DEFAULT设置为默认值，仅在该字段设置了默认值时可用
        # SET()设置为特定值或者调用特定方法
        # DO_NOTHING不做任何操作，如果数据库前置指明级联性，此选项会抛出IntegrityError异常
    book = models.ForeignKey(BookInfo, on_delete=models.CASCADE)
    # book=BookInfo()

    class Meta:
        db_table = 'peopleinfo'

    def __str__(self):
        return self.name
