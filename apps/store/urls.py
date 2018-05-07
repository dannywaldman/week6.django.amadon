from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^store/add$', views.add),
    url(r'^store/checkout$', views.cart)
]
