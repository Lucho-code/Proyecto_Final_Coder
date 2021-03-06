"""blogrecetas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, re_path, include
from blogrecetas.views import Index, Contacto,AboutUs 
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name = 'index'),
    path('contacto/', Contacto.as_view(), name = 'contacto'),
    path('recetas/', include('recetas.urls', namespace = 'recetas')),
    path('about_us/', AboutUs.as_view(), name = 'about_us'),
    re_path('usuarios/', include('users.urls', namespace = 'users_app')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
