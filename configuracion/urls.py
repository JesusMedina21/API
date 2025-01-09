"""
URL configuration for configuracion project.

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

#Librerias por defecto de Django
from django.conf.urls import handler404, handler500, handler400, handler403
from django.contrib import admin
from django.urls import path, include
from api import defaults 

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from api import views

handler404 = defaults.page_not_found
handler500 = defaults.server_error
handler400 = defaults.bad_request  # Si lo has definido
handler403 = defaults.permission_denied  # Si lo has definido


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('logout/', views.logout_view, name='logout'),  # Cambia aquí también
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'), name='api'),
   # path('error/', views.error, name='error'),
    path('documentacion/', views.documentacion, name='documentacion'),
   # path('mantenimiento/', views.mantenimiento, name='mantenimiento'),
   
]
