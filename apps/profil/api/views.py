from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions, generics, status
from ..models import Profile
from .serializers import ProfileSerializer
# from .permissions import IsOwner


class DetailProfileAPI(generics.ListCreateAPIView):
    """
    GET current user, and POST update 
    """
    model = Profile
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticated, )
    authentication_classes = (authentication.TokenAuthentication,)

    def get(self, request, format=None):
        user = User.objects.get(username=request.auth.user)
        serializer = ProfileSerializer(user.profile, context={'request': request})
        return Response(serializer.data)

    def post(self, request, format=None):
        profile = Profile.objects.get(user=request.auth.user)
        profile_serializer = ProfileSerializer(profile, data=request.data, context={'request': request})
        if profile_serializer.is_valid():
            profile_serializer.save()
            return Response(profile_serializer.data, status=status.HTTP_200_OK)
        return Response(profile_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
