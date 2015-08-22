import django_filters
from ..models import Komoditas, Jenis, Barang

class JenisFilter(django_filters.FilterSet):
    komoditas = django_filters.NumberFilter(name="komoditas")

    class Meta:
        model = Jenis
        fields = ('komoditas', )

    