from rest_framework import serializers
from ..models import Profile

class ProfileSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Profile
        fields = ('gender', 'phone_number', 'latitude', 'longitude', 'create_at', 'update_at')
