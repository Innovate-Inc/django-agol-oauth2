from django.conf.urls import re_path

from .views import EsriProxy


urlpatterns = [
    re_path(r'^proxy/', EsriProxy.as_view()),
]
