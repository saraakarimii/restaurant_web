from django.urls import path,include
from .views import *
urlpatterns = [
   
    path('',main.as_view(),name="main"),
  

]