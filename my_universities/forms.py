from django import forms
from django.utils.translation import gettext_lazy as _
import datetime

from .models import MyUniversity



def current_year():
    return datetime.date.today().year

def year_choices():
    return [(r,r) for r in range(1970, datetime.date.today().year+5)]

class MyUniversityForm(forms.ModelForm):
    st_year = forms.TypedChoiceField(label='Start Year', coerce=int, choices=year_choices, initial=current_year)
    en_year = forms.TypedChoiceField(label='End Year', coerce=int, choices=year_choices, initial=current_year)
    enr_status = forms.CharField(label='Enrollment Status', disabled=True)
    class Meta:
        model = MyUniversity
        fields =('country', 'uni_name','st_year','en_year','enr_status')
        labels = {
            'uni_name':_('University'),
            'enr_status':_('Enrollment Status'),
        }
