# Generated by Django 3.2.4 on 2021-07-01 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_auto_20210629_2133'),
    ]

    operations = [
        migrations.AddField(
            model_name='commutingtime',
            name='count',
            field=models.IntegerField(blank=True, null=True, verbose_name='合計労働時間'),
        ),
    ]