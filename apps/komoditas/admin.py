from django.contrib import admin
from .models import Komoditas, Jenis, Barang

# Register your models here.


class KomoditasAdmin(admin.ModelAdmin):
    list_display = ('nama', 'is_active', 'create_at', 'update_at')

admin.site.register(Komoditas, KomoditasAdmin)
# admin.site.register(BookRankings)
# admin.site.register(RankingStatistics)