# Generated by Django 3.2.4 on 2021-06-29 08:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_alter_commutingtime_arrive_at_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commutingtime',
            name='arrive_at_work',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='出社時間'),
        ),
    ]
