"""misitio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include 
from django.conf.urls  import url,include
from web import views,urls
from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns



# router = routers.DefaultRouter()
# router.register(r'Mascota2', views.MascotaViewSet) 





urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    #path('login/$', views.login, name='login'),
    #path('logout/', auth_views.auth_logout, {'next_page': 'login'}, name='logout'),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('Mascota', views.MascotaReg, name='Mascota'),
    path('Contacto', views.ContactoReg, name='Contacto'),
    path('ListarPerros', views.ListarPerros, name='ListarPerros'),
    url('social', include('social_django.urls', namespace='social')),
    url ('', include ('pwa.urls')),
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('Prueba', views.Prueba, name='Prueba'),
    
    url(r'^', include('web.urls')),
    

    

] 

# urlpatterns = format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
