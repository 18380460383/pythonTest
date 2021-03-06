from django.db import models


class userinfo(models.Model):
    # 如果没有models.AutoField，默认会创建一个id的自增列
    name = models.CharField(max_length=30)
    email = models.EmailField()
    memo = models.TextField()

    def __str__(self):
        return '(userinfo: %s, %s,%s)' % (self.name, self.email, self.memo)


class user(models.Model):
    # 如果没有models.AutoField，默认会创建一个id的自增列
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=32)
    level = models.IntegerField()
    login_time=models.DateTimeField()

    def __str__(self):

        return '(level: %s, %s,%s)' % (self.name, self.password, self.level)
