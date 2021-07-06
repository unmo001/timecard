from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    wage = models.IntegerField(verbose_name='時給', default=1000)



class CommutingTime(models.Model):
    arrive_at_work = models.DateTimeField(verbose_name='出社時間', null=True, blank=True)
    leave = models.DateTimeField(verbose_name='退社時間', null=True, blank=True)
    count = models.IntegerField(verbose_name='一日の勤務時間', default=0)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "勤怠管理"

    def __str__(self):
        return str(self.arrive_at_work)

    def get_tdhours(self):
        if self.arrive_at_work and self.leave:
            return round((self.leave - self.arrive_at_work).seconds / 60 / 60)
        else:
            return None

    def get_count(self,):
        if self.count:
            return self.count * self.user.wage
        else:
            return None
