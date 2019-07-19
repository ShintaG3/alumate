from django.urls import path
from . import views

urlpatterns = [
    path('my-profile', views.MyProfileUpdateView.as_view(), name='my_profile')
]
