# Generated by Django 2.2.3 on 2019-07-22 05:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_universities', '0004_auto_20190722_0043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuniversity',
            name='description',
        ),
        migrations.RemoveField(
            model_name='myuniversity',
            name='grade_rate',
        ),
    ]
