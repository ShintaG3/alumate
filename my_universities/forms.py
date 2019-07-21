from django import forms
from django.utils.translation import gettext_lazy as _
import datetime

from .models import MyUniversity



def current_year():
    return datetime.date.today().year

def year_choices():
    return [(r,r) for r in range(1970, datetime.date.today().year+11)]

class MyUniversityForm(forms.ModelForm):
    st_year         = forms.TypedChoiceField(label='Start Year', coerce=int, choices=year_choices,
                        initial=current_year, widget=forms.Select(
                                attrs={
                                    # 'placeholder': '',
                                    'name': 'en_year',
                                    'id': 'en_year',
                                    'class':'form-control',
                                }
                            )

                        )

    en_year         = forms.TypedChoiceField(label='End Year', coerce=int, choices=year_choices,
                        initial=current_year, widget=forms.Select(
                                attrs={
                                    # 'placeholder': '',
                                    'name': 'en_year',
                                    'id': 'en_year',
                                    'class':'form-control',
                                }
                            )

                        )
    uni_name        = forms.CharField(label='School', widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Ex: Boston University',
                                        'name': 'uni_name',
                                        'id': 'uni_name',
                                        'class':'form-control'
                                    }
                                )
                            )
    degree          = forms.CharField(label='Degree', widget=forms.TextInput(
                                    attrs={
                                        'placeholder': "Ex: Master's",
                                        'class':'form-control',
                                        'name':'degree',
                                        'id': 'degree',
                                    }
                                )
                            )
    field_of_study  = forms.CharField(label='Field of stud', widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Business',
                                        'class':'form-control',
                                        'name':'field_of_study',
                                        'id': 'field_of_study',
                                    }
                                )
                            )
    grade  = forms.CharField(label='Grade', widget=forms.TextInput(
                                    attrs={
                                        'placeholder': 'Disticntion',
                                        'class':'form-control',
                                        'name':'grade',
                                        'id': 'grade',
                                    }
                                )
                            )
    class Meta:
        model = MyUniversity
        fields =('uni_name', 'degree', 'field_of_study', 'st_year','en_year','grade')
        labels = {
            'uni_name':_('University'),
            'enr_status':_('Enrollment Status'),
        }
