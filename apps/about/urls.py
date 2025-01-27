from django.conf.urls.static import static
from django.urls import path
from config import settings

from .views import about_view

urlpatterns = [
    path('', about_view, name='about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)