from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^searchbus/$', views.searchbusPage, name='searchbus'),
    url(r'^searchcar/$', views.searchcarPage, name='searchbus'),
]
