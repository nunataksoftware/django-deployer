# -*- coding: utf-8 -*-

from django.conf.urls import url

from deployer import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
