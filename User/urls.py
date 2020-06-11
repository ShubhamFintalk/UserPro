from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='login'),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
    path("signup", views.signUp, name='signUp'),
    path("posts", views.posts, name='posts')
]
