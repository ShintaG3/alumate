# Generated by Django 2.2.3 on 2019-08-11 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_profiles', '0003_myprofile_identicon'),
    ]

    operations = [
        migrations.AddField(
            model_name='myprofile',
            name='country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]