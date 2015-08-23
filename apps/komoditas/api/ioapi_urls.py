from django.conf.urls import patterns, include, url
from ..api import views

urlpatterns = patterns('',
                       url(r'^indikatorvital_komoditas/(?P<pk>\d+)/$', views.ListIndikatorAPI().as_view(),
                           name='api-summary-harga-komoditas'),
                       )
