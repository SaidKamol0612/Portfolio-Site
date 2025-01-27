from django.conf.urls.static import static
from django.urls import path
from config import settings

from .views import blog_view, single_view

urlpatterns = [
    path('', blog_view, name='blog'),
    path('single/', single_view, name='single'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)