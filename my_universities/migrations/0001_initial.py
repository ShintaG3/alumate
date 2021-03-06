# Generated by Django 2.2.3 on 2019-07-19 06:22

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import my_universities.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUniversity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=256, null=True)),
                ('uni_name', models.CharField(blank=True, max_length=100, null=True)),
                ('st_year', models.IntegerField(default=my_universities.models.current_year, validators=[django.core.validators.MinValueValidator(1970), my_universities.models.max_value_current_year], verbose_name='year')),
                ('en_year', models.IntegerField(default=my_universities.models.current_year, validators=[django.core.validators.MinValueValidator(1970), my_universities.models.max_value_current_year], verbose_name='en_year')),
                ('enr_status', models.CharField(choices=[('applicant', 'Applicant'), ('current student', 'Current student'), ('alumni', 'Alumni')], max_length=64)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
