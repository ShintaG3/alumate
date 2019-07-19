from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('boards.urls')),
    path('', include('accounts.urls')),
    path('', include('auths.urls')),
    path('', include('my_universities.urls')),
    path('', include('my_profiles.urls')),
    path('', include('universities.urls')),
    path('', include('charts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
