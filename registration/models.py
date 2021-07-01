from django.conf import settings
from django.db import models


# Create your models here.


class CommutingTime(models.Model):
    arrive_at_work = models.DateTimeField(verbose_name='出社時間', null=True, blank=True)
    leave = models.DateTimeField(verbose_name='退社時間', null=True, blank=True)
    count = models.IntegerField(verbose_name="合計労働時間",null=False,default=0)
    payment = models.IntegerField(verbose_name='時給',default=1000)
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

    def get_count(self):
        time = round((self.leave - self.arrive_at_work).seconds / 60 / 60)
        if self.count == 0:
            self.count += time
            return self.count

    def get_payment(self):
        payment = self.count *self.payment
        return payment


