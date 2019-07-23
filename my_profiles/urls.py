from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyProfileUpdateView.as_view(), name='my_profile')
]
