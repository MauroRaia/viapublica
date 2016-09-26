from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reclamo/alta/', views.reclamo_alta, name='reclamo_alta')
]
