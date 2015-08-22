from django.db.models import Q
from rest_framework import serializers
from ..models import Komoditas, Jenis, Barang
from apps.profil.api.serializers import ProfileSerializer


class KomoditasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Komoditas
        fields = ('id', 'nama', 'is_active', 'create_at', 'update_at')


class JenisSerializer(serializers.ModelSerializer):
    komoditas = serializers.SerializerMethodField()

    class Meta:
        model = Jenis
        fields = ('id', 'nama', 'komoditas', 'create_at', 'update_at')

    def get_komoditas(self, obj):
        return obj.komoditas.nama


class BarangSerializer(serializers.ModelSerializer):
    komoditas = serializers.SerializerMethodField()
    jenis = serializers.SerializerMethodField()
    # Write
    komoditas_id = serializers.IntegerField(write_only=True)
    jenis_id = serializers.IntegerField(write_only=True, required=False)
    nama = serializers.CharField(write_only=True)
    stok = serializers.DecimalField(max_digits=15, decimal_places=2)
    price = serializers.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        model = Barang
        fields = ('id', 'komoditas_id', 'jenis_id', 'komoditas', 'nama', 'jenis', 'stok', 'price',
                  'latitude', 'longitude', 'is_deleted', 'create_at', 'update_at')

    def validate_jenis_id(self, value):
        try:
            Jenis.objects.get(pk=value)
            return value
        except Jenis.DoesNotExist:
            raise serializers.ValidationError('jenis_id does not exist.')

    def validate_komoditas_id(self, value):
        try:
            Komoditas.objects.get(pk=value)
            return value
        except Komoditas.DoesNotExist:
            raise serializers.ValidationError('komoditas_id does not exist.')

    def get_komoditas(self, obj):
        return obj.jenis.komoditas.nama

    def get_jenis(self, obj):
        return obj.jenis.nama

    def create(self, validated_data):
        request = self.context.get('request')
        
        try:
            jenis = Jenis.objects.get(Q(pk=validated_data.get('jenis_id')) | Q(nama=validated_data.get('nama')))
        except Jenis.DoesNotExist:
            jenis = Jenis.objects.create(nama=validated_data.get('nama'), komoditas_id=validated_data.get('komoditas_id'))

        # import ipdb; ipdb.set_trace();
        del validated_data['nama']
        del validated_data['komoditas_id']
        validated_data['jenis_id'] = jenis.pk
        validated_data['user_id'] = request.auth.user.id

        try:
            barang = Barang.objects.get(jenis=jenis, user=request.auth.user)
            instance = super(BarangSerializer, self).update(
                barang, validated_data)
        except Barang.DoesNotExist:
            instance = super(BarangSerializer, self).create(validated_data)
        instance.save()
        return instance


class DetailBarangSerializer(serializers.ModelSerializer):
    komoditas = serializers.SerializerMethodField()
    jenis = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = Barang
        fields = ('id', 'komoditas', 'jenis', 'stok', 'price', 'latitude',
                  'longitude', 'is_deleted', 'create_at', 'update_at', 'user')

    def get_komoditas(self, obj):
        return obj.jenis.komoditas.nama

    def get_jenis(self, obj):
        return obj.jenis.nama

    def get_user(self, obj):
        serializers = ProfileSerializer(obj.user.profile)
        return serializers.data
