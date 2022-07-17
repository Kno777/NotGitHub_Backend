from django.db import models
from django.contrib.auth.models import User

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return f'{instance.user.username}_user_{instance.user.id}/{filename}' 
    
class UserPosts(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    folder_name = models.CharField(max_length=100, blank=True, null=True)
    code_insert = models.FileField(
        verbose_name="Insert Code",
        upload_to=user_directory_path,
        error_messages={'blank' : 'BLANK','required' : 'REQUIRED'}
    )  
    commit = models.CharField(max_length=100, default="Your Commit!")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(f'{self.user.username}' + ' ' + str(f'{self.folder_name}'))
    