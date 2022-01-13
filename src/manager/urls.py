from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('',admin_panel,name='admin_panel'),
    path('food/', permission_required('is_superuser')(AllFoodList.as_view()),name='foods'),
    path('food/add',permission_required('is_superuser')(AddFood.as_view()),name='fadd'),
    path('food/<int:pk>/update', permission_required('is_superuser')(EditeFood.as_view()),name='fedite'),
    path('food/<int:pk>/delete', permission_required('is_superuser')(DeleteFood.as_view()),name='fdelete'),
    path('category/', permission_required('is_superuser')(AllCategoryList.as_view()),name='categories'),
    path('category/add', permission_required('is_superuser')(AddCategory.as_view()),name='cadd'),
    path('category/<int:pk>/update', permission_required('is_superuser')(EditeCategory.as_view()),name='cedite'),
    path('category/<int:pk>/delete', permission_required('is_superuser')(DeleteCategory.as_view()),name='cdelete')
  

]