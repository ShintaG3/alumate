from django import forms
from .models import MyProfile

class MyProfileForm(forms.ModelForm):
    img = forms.ImageField(label='Image')
    country = forms.CharField(
                        required=False,
                        label='Country of Origin',
                        widget=forms.TextInput(
                                attrs={
                                    "class":"form-control",
                                    "id":"country_name"

                                }
                            )
                        )
    introduction = forms.CharField(
                        required=False,
                        widget=forms.Textarea(
                                attrs={
                                    "class":"form-control",

                                    "placeholder":"Introduce who you are",
                                }
                            )
                        )
    current_occupation = forms.CharField(
                        required=False,
                        label='Current Occupation',
                        widget=forms.TextInput(
                                attrs={
                                    "class":"form-control"
                                }
                            )
                        )
    tags = forms.CharField(
                        required=False,
                        widget=forms.TextInput(
                                attrs={
                                    "class":"form-control",


                                }
                            )
                        )
    class Meta:
        model = MyProfile
        fields = ('img','country','introduction','current_occupation','tags')
