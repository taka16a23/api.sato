"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from backend import settings

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('api/publish/', include('publish.urls'), name='publish'),
    path('api/security/', include('security.urls'), name='security'),
    path('api/formats/', include('formats.urls'), name='format'),
    path('api/about/', include('about.urls'), name='about'),
    path('api/calendar/', include('home.urls'), name='calendar'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
