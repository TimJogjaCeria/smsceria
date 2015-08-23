from django.db import models
from django.db.models import Q, Avg
from django.contrib.auth.models import User
from apps.profil.models import Profile

# Create your models here.


class Komoditas(models.Model):
    nama = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Komoditas"

    def __unicode__(self):
        return '%s' % (self.nama)


class Jenis(models.Model):
    komoditas = models.ForeignKey(Komoditas, related_name="komoditas_jenis")
    nama = models.CharField(max_length=100, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Jenis"

    def __unicode__(self):
        return '%s - %s' % (self.komoditas, self.nama)

    def mean_price(self):
        res = self.harganya.all().aggregate(Avg('price'))
        if res.get('price__avg'):
            mean = res.get('price__avg')
        else:
            mean = 0
        return round(mean,2)


class Barang(models.Model):
    user = models.ForeignKey(User, related_name="hargaku")
    jenis = models.ForeignKey(Jenis, related_name="harganya")
    stok = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    price = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    latitude = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.CharField(max_length=100, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Barang"
        unique_together = ('user', 'jenis',)

    def __unicode__(self):
        return '%s : %s - %s' % (self.user, self.jenis, self.price)
