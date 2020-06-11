#
from django.contrib import admin
from django.urls import path
from.import views
#
urlpatterns = [
    path('', views.Product_item, name='Product_item')
]
