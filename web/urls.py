from django.conf.urls  import url,include
from django.conf import Path
from web import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    
    url(r'^Listado/$', views.Listado.as_view()),
    url(r'^Listado/(?P<pk>[0-9]+)/$', views.ListadoDetail.as_view()),
    
    


]


urlpatterns = format_suffix_patterns(urlpatterns)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




