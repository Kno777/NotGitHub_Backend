from rest_framework import generics
from .models import UserPosts
from .permissions import IsAuthorOrReadOnly # new
from .serializers import UserPostSerializer, UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.reverse import reverse


class UserPostList(generics.ListCreateAPIView):
    queryset = UserPosts.objects.all()
    serializer_class = UserPostSerializer
    name = 'User Post List'
    
class UserPostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,) # new
    queryset = UserPosts.objects.all()
    serializer_class = UserPostSerializer
    name = 'User Post Detail'
    
class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    name = 'User List'
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    name = 'User Detail'
    