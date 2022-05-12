from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   path("cakes-api/", include('rest_framework.urls'),name= 'cakes-api'),
   path("",views.Home,name="Home"),
    path("cakes",views.Cakes_Lists,name= 'cakes_list'),
    path("cake-detail/<str:pk>/",views.Cake_Details,name= 'cake-detail'),
    path("addcake",views.add_cake,name= 'addcakes'),
    path("cake-update/<str:pk>/",views.update_cake,name= 'cake-update'),
    path("delete-cake/<str:pk>/",views.delete_cake,name= 'delete-cake'),
]