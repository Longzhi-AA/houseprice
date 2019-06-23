from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^map/', views.addr_map),
    url(r'^index/', views.index),
]