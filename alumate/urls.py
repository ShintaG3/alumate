from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('boards/', include('boards.urls')),
    path('account/', include('accounts.urls')),
    path('aouth/', include('auths.urls')),
    path('my-university/', include('my_universities.urls')),
    path('my-profile/', include('my_profiles.urls')),
    path('university/', include('universities.urls')),
    path('', include('charts.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
