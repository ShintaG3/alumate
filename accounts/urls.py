from django.urls import path
from . import views
from django.conf import settings

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('setting/account/', views.UserUpdateView.as_view(), name='my_account'),
]
