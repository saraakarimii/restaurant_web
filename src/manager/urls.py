from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('',admin_panel,name='admin_panel'),
    path('food/', AllFoodList.as_view(),name='foods'),
    path('food/add', AddFood.as_view(),name='fadd'),
    path('food/<int:pk>/update', EditeFood.as_view(),name='fedite'),
    path('food/<int:pk>/delete', DeleteFood.as_view(),name='fdelete'),
    path('category/', AllCategoryList.as_view(),name='categories'),
    path('category/add', AddCategory.as_view(),name='cadd'),
    path('category/<int:pk>/update', EditeCategory.as_view(),name='cedite'),
    path('category/<int:pk>/delete', DeleteCategory.as_view(),name='cdelete')
  

]