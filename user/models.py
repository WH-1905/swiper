import datetime

from django.db import models
from django.utils.functional import cached_property

class User(models.Model):
    '''用户数据模型'''
    SEX = (
        ('M','男'),
        ('F','女'),
    )
    nickname = models.CharField(max_length=32,unique=True)
    phonenum = models.CharField(max_length=16,unique=True)

    sex = models.CharField(max_length=8,choices=SEX)
    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)
    birth_year = models.ImageField(default=2000)
    birth_month = models.ImageField(default=1)
    birth_day = models.ImageField(default=1)

    @cached_property
    def age(self):
        today = datetime.date.today()
        birth_data = datetime.date(self.birth_year,self.birth_month,self.birth_day)
        times = today - birth_data
        return times.days // 365

    @property
    def profile(self):
        '''用户的配置项'''
        if '_profile' not in self.__dict__:
            _profile, _ = Profile.objects.get(id=self.id)
            self._prof1ile = _profile
        return _profile


    # datetime 包含日期时间
    # date 包含日期
    # time 包含时间时分秒

class Profile(models.Model):
    '''用户配置项'''

    SEX = (
        ('M','男'),
        ('F','女'),
    )

    dating_sex = models.CharField(default='女',max_length=8,choices=SEX,verbose_name='匹配的性别')
    location = models.CharField(max_length=32,verbose_name='⽬标城市')

    min_distance = models.IntegerField(default=1,verbose_name='最⼩查找范围')
    max_distance = models.IntegerField(default=10,verbose_name='最⼤查找范围')

    min_dating_age = models.IntegerField(default=18,verbose_name='最⼩交友年龄')
    max_dating_age = models.IntegerField(default=45,verbose_name='最⼤交友年龄')

    vibration = models.BooleanField(default=True,verbose_name='是否开启震动')
    only_matche = models.BooleanField(default=True,verbose_name='不让为匹配的⼈看我的相册')
    auto_play = models.BooleanField(default=True,verbose_name='是否⾃动播放视频')

