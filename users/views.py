from rest_framework import generics
from .models import UserProfile
from .serializers import UserProfileSerializer
from .permissions import IsAuthorOrReadOnly , IsAuthenticatedOrWriteOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse
from posts import views
from rest_framework.documentation import include_docs_urls
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class CreateUserProfile(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticatedOrWriteOnly]
    name = 'Create User Profile'


class ListUserProfile(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    name = 'List User Profile'
    
class DetailUserProfile(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    name = 'Detail User Profile'

    
class ApiRoot(generics.GenericAPIView):
    name = 'API-ROOT'
    
    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(views.UserList.name, request=request),
            'post': reverse(views.UserPostList.name, request=request),
            'profile': reverse(ListUserProfile.name, request=request),
            'create/profile':reverse(CreateUserProfile.name, request=request)
        })
        

