from django.db import models


class UserGroup(models.Model):
    """ User grouped by cities """
    gname = models.CharField(verbose_name='GroupName', unique=True, max_length=32)






# 对于 Django的字符串字段（CharField、TextField），一般不推荐同时使用 null=True，因为这会造成两种空值表示：NULL 和 ""。
class UserInfo(models.Model):
    """ Users table """
    '''
    +----------+---------------+------+-----+---------+----------------+
    | Field    | Type          | Null | Key | Default | Extra          |
    +----------+---------------+------+-----+---------+----------------+
    | id       | bigint        | NO   | PRI | NULL    | auto_increment |
    | uname    | varchar(32)   | NO   |     | NULL    |                |
    | pwd      | varchar(64)   | NO   |     | NULL    |                |
    | age      | int           | NO   |     | NULL    |                |
    | score    | decimal(10,2) | YES  |     | NULL    |                |
    | gender   | smallint      | NO   |     | NULL    |                |
    | group_id | varchar(32)   | NO   | MUL | NULL    |                |
    +----------+---------------+------+-----+---------+----------------+
    gruop字段被换成了group_id ，该字段是外键，指向 UserGroup 表的 gname 字段
    '''
    uname = models.CharField(max_length=32)
    pwd = models.CharField(max_length=64)
    age = models.IntegerField(verbose_name='age')
    group = models.ForeignKey(verbose_name='inGroup',  null=True, blank=True, to=UserGroup, to_field='gname', on_delete=models.CASCADE)
    score = models.DecimalField(verbose_name='score', null=True, blank=True, max_digits=10, decimal_places=2, default=0)
    # gender = models.BooleanField(verbose_name='gender', default=True, help_text='1-male, 2-female', choices=((1, 'male'), (2, 'female')))
    gender_choices = (
        (1, 'male'),
        (2, 'female')
    )
    gender = models.SmallIntegerField(verbose_name='gender', choices=gender_choices, default=1)
