from rest_framework import serializers
from ..models import Komoditas, Jenis, Barang
from apps.profil.api.serializers import ProfileSerializer


class KomoditasSerializer(serializers.ModelSerializer):

    class Meta:
        model = Komoditas
        fields = ('id', 'nama', 'is_active', 'create_at', 'update_at')


class JenisSerializer(serializers.ModelSerializer):
    # komoditas_id = serializers.IntegerField(write_only=True)
    # nama = serializers.CharField()

    class Meta:
        model = Jenis
        fields = ('id', 'nama', 'create_at', 'update_at')


class BarangSerializer(serializers.ModelSerializer):
    komoditas = serializers.SerializerMethodField()
    jenis = serializers.SerializerMethodField()
    # Write
    jenis_id = serializers.IntegerField(write_only=True)
    stok = serializers.DecimalField(max_digits=15, decimal_places=2)
    price = serializers.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        model = Barang
        fields = ('id', 'jenis_id', 'komoditas', 'jenis', 'stok', 'price',
                  'latitude', 'longitude', 'is_deleted', 'create_at', 'update_at')

    def validate_jenis_id(self, value):
        try:
            Jenis.objects.get(pk=value)
            return value
        except Jenis.DoesNotExist:
            raise serializers.ValidationError('jenis_id does not exist.')

    def get_komoditas(self, obj):
        return obj.jenis.komoditas.nama

    def get_jenis(self, obj):
        return obj.jenis.nama

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user_id'] = request.auth.user.id
        try:
            barang = Barang.objects.get(jenis_id=validated_data.get('jenis_id'), user_id=validated_data.get('user_id'))
            instance = super(BarangSerializer, self).update(barang, validated_data)
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
