from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics, status, views
from ..models import Komoditas, Jenis, Barang
from .serializers import KomoditasSerializer, JenisSerializer, BarangSerializer, DetailBarangSerializer, IndikatorvitalSerializer
from .filters import JenisFilter
# from .permissions import IsOwner


class ListKomoditasAPI(generics.ListAPIView):
    """
    GET List Komoditas
    """
    model = Komoditas
    queryset = Komoditas.objects.all()
    serializer_class = KomoditasSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (authentication.TokenAuthentication,)


class DetailKomoditasAPI(generics.RetrieveAPIView):
    """
    GET Detail Komoditas
    """
    model = Komoditas
    queryset = Komoditas.objects.all()
    serializer_class = KomoditasSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (authentication.TokenAuthentication,)


class ListJenisAPI(generics.ListAPIView):
    """
    GET List Jenis
    """
    model = Jenis
    queryset = Jenis.objects.all()
    serializer_class = JenisSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (authentication.TokenAuthentication,)
    filter_class = JenisFilter


class ListBarangAPI(generics.ListCreateAPIView):
    """
    GET List Barang
    """
    model = Barang
    queryset = Barang.objects.all()
    serializer_class = BarangSerializer
    permission_classes = (permissions.AllowAny, )
    authentication_classes = (authentication.TokenAuthentication,)


class DetailBarangAPI(generics.RetrieveUpdateDestroyAPIView):
    """
    GET Detail Barang
    """
    model = Barang
    queryset = Barang.objects.all()
    serializer_class = DetailBarangSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (authentication.TokenAuthentication,)


class Indikator(object):
    def __init__(self, summary):
        self.summary = summary


class ListIndikatorAPI(views.APIView):
    """
    GET List Indokator
    """
    serializer_class = JenisSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (authentication.TokenAuthentication,)    

    def get(self, request, pk, format=None):
        """
        Return a list of all indikator.
        """
        # import ipdb; ipdb.set_trace();
        indikators = []
        indikator1 = Indikator(summary='Terdapat kenaikan rata2 10% dari harga standar bulog di jakarta')
        indikator2 = Indikator(summary='Terdapat kenaikan rata2 10% dari harga standar bulog di jawa barat')
        indikators.append(indikator1)
        indikators.append(indikator2)
        indikator_serializer = IndikatorvitalSerializer(indikators, many=True)
        return Response(indikator_serializer.data)