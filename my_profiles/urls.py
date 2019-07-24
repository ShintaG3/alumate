from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyProfileUpdateView.as_view(), name='my_profile'),
    path('delete_img/', views.delete_img, name='delete_img'),
]
