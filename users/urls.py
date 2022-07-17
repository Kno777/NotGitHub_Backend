from django.urls import path, re_path
from . import views

urlpatterns = [
    path('profile/<int:pk>/', views.DetailUserProfile.as_view()),
    re_path(r'^profile/$', views.ListUserProfile.as_view(), name=views.ListUserProfile.name),
    re_path(r'^create/profile/$', views.CreateUserProfile.as_view(), name=views.CreateUserProfile.name),
    re_path(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name),
]
