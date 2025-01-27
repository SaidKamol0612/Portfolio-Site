from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.home.urls')),
    path('collection/', include('apps.collection.urls')),
    path('about/', include('apps.about.urls')),
    path('services/', include('apps.services.urls')),
    path('blog/', include('apps.blog.urls')),
    path('contact/', include('apps.contact.urls')),
]
