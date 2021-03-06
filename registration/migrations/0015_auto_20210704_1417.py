# Generated by Django 3.2.4 on 2021-07-04 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_commutingtime_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('wage', models.IntegerField(default=1000, verbose_name='時給')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='commutingtime',
            name='count',
        ),
        migrations.RemoveField(
            model_name='commutingtime',
            name='payment',
        ),
        migrations.AddField(
            model_name='commutingtime',
            name='per_day',
            field=models.IntegerField(blank=True, null=True, verbose_name='一日の勤務時間'),
        ),
    ]
