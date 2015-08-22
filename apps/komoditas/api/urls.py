from django.conf.urls import patterns, include, url
from ..api import views

urlpatterns = patterns('',
                       url(r'^$', views.ListKomoditasAPI().as_view(),
                           name='api-list-komoditas'),
                       url(r'^(?P<pk>\d+)/$', views.DetailKomoditasAPI().as_view(),
                           name='api-detail-komoditas'),
                       url(r'^jenis/$', views.ListJenisAPI().as_view(),
                           name='api-list-jenis'),
                       # url(r'^jenis/(?P<pk>\d+)/$', views.DetailKomoditasAPI().as_view(),
                       #     name='api-detail-jenis'),
                       url(r'^barang/$', views.ListBarangAPI().as_view(),
                           name='api-list-barang'),
                       url(r'^barang/(?P<pk>\d+)/$', views.DetailBarangAPI().as_view(),
                           name='api-detail-barang'),
                       )
