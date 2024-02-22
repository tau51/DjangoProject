from django.db import models
from django.db.models import UniqueConstraint


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=32)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    deleted = models.BooleanField(default=False)


class clue(models.Model):
    username = models.CharField(max_length=32)
    province = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    club = models.CharField(max_length=32)
    link = models.CharField(max_length=64)
    fans = models.IntegerField(default=0)
    type = models.CharField(max_length=10)
    wechat = models.CharField(max_length=32)
    group = models.CharField(max_length=10)
    audits = models.CharField(max_length=10, null=True, default="未审核")
    settle = models.CharField(default="未结算", null=True)
    status = models.CharField(max_length=64, null=True, default=0)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    deleted = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['wechat', 'deleted'], name='unique_wechat'),
            UniqueConstraint(fields=['club', 'deleted'], name='unique_club')
        ]
