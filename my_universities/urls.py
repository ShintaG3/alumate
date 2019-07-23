from django.urls import path
from . import views

urlpatterns = [
    path('', views.MyUniversityUpdateView.as_view(), name='my_university')
]
