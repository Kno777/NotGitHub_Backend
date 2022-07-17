from django.urls import path, re_path
from .views import UserList, UserDetail, UserPostList, UserPostDetail

urlpatterns = [
    re_path(r'^users/$', UserList.as_view(), name=UserList.name), # new
    path('users/<int:pk>/', UserDetail.as_view()), # new
    re_path(r'^post/$', UserPostList.as_view(), name=UserPostList.name),
    path('post/<int:pk>/', UserPostDetail.as_view()),
]