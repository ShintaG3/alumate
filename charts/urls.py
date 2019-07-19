from django.urls import path
from . import views

urlpatterns = [
    path('chart/', views.ChartAPI.as_view(), name='chart-api'),
    path('chart/home/', views.HomeView.as_view(), name='chart-home')
]
