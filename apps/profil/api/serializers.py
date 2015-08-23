from rest_framework import serializers
from ..models import Profile

class ProfileSerializer(serializers.ModelSerializer):    
    username = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ('id', 'username', 'email', 'gender', 'phone_number', 'latitude', 'longitude', 'create_at', 'update_at')

    def get_username(self, obj):
        return obj.user.username

    def get_email(self, obj):
        return obj.user.email