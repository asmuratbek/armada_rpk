"""armada URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from armada import settings
from base_data_app.views import index, service, thanks, send_call_back, about_company, get_project_in_key

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', index, name='index'),
    path('service/<int:id>/', service, name='service'),
    path('send_call_back', send_call_back, name='callback'),
    path('thanks/', thanks, name='thanks'),
    path('about_company/', about_company, name='about_company'),
    path('get_project_in_key/', get_project_in_key, name='key')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
