# Generated by Django 2.2.3 on 2019-07-21 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_universities', '0002_auto_20190719_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuniversity',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='myuniversity',
            name='grade_rate',
            field=models.IntegerField(blank=True, default=60, null=True),
        ),
    ]
