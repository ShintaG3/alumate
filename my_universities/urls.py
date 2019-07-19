from django.urls import path
from . import views

urlpatterns = [
    path('my-university', views.MyUniversityUpdateView.as_view(), name='my_university')
]
