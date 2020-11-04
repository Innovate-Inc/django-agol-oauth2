from django.conf.urls import url

from .views import EsriProxy


urlpatterns = [
    url(r'^proxy/', EsriProxy.as_view()),
]
