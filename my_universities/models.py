from django.db import models
from django.conf import settings
import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _
from django.db.models.signals import post_save, pre_save

User = settings.AUTH_USER_MODEL

def current_year():
    return datetime.date.today().year

def max_value_current_year(value):
    return MaxValueValidator(current_year() + 5)(value)

ENROLLMENT_STATUS = (
    ('applicant','Applicant'),
    ('current student', 'Current student'),
    ('alumni','Alumni'),
)

class MyUniversity(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    country     = models.CharField(max_length=256, null=True, blank=True)
    uni_name    = models.CharField(max_length=100, null=True, blank=True)
    st_year     = models.IntegerField(_('year'), validators=[MinValueValidator(1970), max_value_current_year],default=current_year)
    en_year     = models.IntegerField(_('en_year'), validators=[MinValueValidator(1970), max_value_current_year],default=current_year)
    enr_status  = models.CharField(max_length=64, choices=ENROLLMENT_STATUS)

    def __str__(self):
        return f"{self.id} {str(self.user)}"

def pre_save_userprofile_receiver(sender, instance, *args, **kwargs):
    en_year = instance.en_year
    st_year  = instance.st_year
    if en_year < current_year():
        instance.enr_status = "alumni"
    elif st_year > current_year():
        instance.enr_status = "applicant"
    else:
        instance.enr_status = "current student"

pre_save.connect(pre_save_userprofile_receiver, sender=MyUniversity)
