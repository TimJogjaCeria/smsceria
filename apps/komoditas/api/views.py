from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics, status
from ..models import Komoditas, Jenis, Barang
from .serializers import KomoditasSerializer, JenisSerializer, BarangSerializer, DetailBarangSerializer
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