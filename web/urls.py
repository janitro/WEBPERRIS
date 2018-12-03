from django.conf.urls  import url,include
from web import views
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [
    
    url(r'^Listado/$', views.Listado.as_view()),
    url(r'^Listado/(?P<pk>[0-9]+)/$', views.ListadoDetail.as_view()),
    


]


urlpatterns = format_suffix_patterns(urlpatterns)