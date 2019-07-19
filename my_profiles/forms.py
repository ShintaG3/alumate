from django import forms
from .models import MyProfile

class MyProfileForm(forms.ModelForm):
    img = forms.ImageField(label='Image')
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
        fields = ('img','introduction','current_occupation','tags')
        labels = {
            'img':'Image',
            'introduction':'Introduction',
            'current_occupation':'Current Occupation',
            'tags':'Tags',
        }
