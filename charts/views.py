from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

# from rest_framework import viewsets
# from .serializers import ChartSerializer
# from .models import Chart

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts/charts.html')

class ChartAPI(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        qs_count = User.objects.all().count()
        labels = ['User', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
        default_item = [qs_count, 12,34,55,11,3]
        data = {
            "labels":labels,
            "default":default_item,
        }

        return Response(data)

# class ChartSerializerAPI(viewsets.ModelViewSet):
#     queryset = Chart.objects.all()
#     serializer_class = ChartSerializer
