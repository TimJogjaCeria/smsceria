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
    def __init__(self, summary, details):
        self.summary = summary
        self.details = details

# class IndikatorDetail(object):
#     def __init__(self, detail):
#         self.detail = detail

class ListIndikatorAPI(views.APIView):
    """
    GET List Indokator
    """
    # serializer_class = JenisSerializer
    # permission_classes = (permissions.IsAuthenticated, )
    # authentication_classes = (authentication.TokenAuthentication,)    

    def get(self, request, pk, format=None):
        """
        Return a list of all indikator.
        """
        import urllib2
        import csv
        import json

        url = 'http://data.go.id/dataset/fec232bd-9e08-49f8-8165-51971d961581/resource/a7ba5107-7614-4a1e-adf1-9181f5599597/download/perkembanganhargaratarataberasgrosirdipasarindukcipinangpicmenurutjenisberas2011.csv'
        response = urllib2.urlopen(url)
        cr = csv.reader(response)
        result = []
        last_beras = ''
        # import ipdb; ipdb.set_trace();
        for row in cr:
            if row[2] == 'jenis_beras':
                pass
            elif last_beras != row[2]:
                last_beras = row[2]
                beras = {'jenis_beras':row[2], 'harga':row[3]}
                result.append(beras)

        komoditas = Komoditas.objects.get(pk=1)
        jenis = komoditas.komoditas_jenis.all()
        indikators = []
        for res in result:
            try:
                jns = jenis.get(nama__icontains=res.get('jenis_beras'))
                # import ipdb; ipdb.set_trace();
                harga_std = float(res.get('harga'))
                delt = jns.mean_price() - harga_std
                persentase = round((delt / harga_std) * 100, 2)
                details = []
                detail = 'Jumlah data yang dipakai didapat dari %s titik.' % jns.harganya.count()
                details.append(detail)
                summary = 'Pada %s %s terdapat kenaikan rata2 %s  harga standar pemerintah.' % (komoditas.nama, jns.nama, (str(persentase)+'%'))
                indikator1 = Indikator(summary=summary, details=details)
                indikators.append(indikator1)
            except Jenis.DoesNotExist:
                pass

            # import ipdb; ipdb.set_trace();
        indikator_serializer = IndikatorvitalSerializer(indikators, many=True)
        return Response(indikator_serializer.data)