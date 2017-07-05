from django.conf.urls import url

from spiders import views

urlpatterns = [
    url(r'newhouses/$', views.newhouse_list),
    url(r'newhouses/(?P<pk>[0-9]+)/$', views.newhouse_detail),
]