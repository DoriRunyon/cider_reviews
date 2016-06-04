from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^rating/(?P<pk>\d+)/$', views.rating_detail, name='rating_detail'),
    url(r'^rating/(?P<pk>\d+)/edit/$', views.rating_edit, name='rating_edit'),
    url(r'^rating/(?P<pk>\d+)/delete/$', views.rating_delete, name='rating_delete'),

]