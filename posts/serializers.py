from django.contrib.auth import get_user_model # new
from rest_framework import serializers
from .models import UserPosts

class UserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPosts
        fields = ('id', 'user', 'folder_name', 'code_insert', 'commit', 'created_at',)
        
        
class UserSerializer(serializers.ModelSerializer): # new
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)    