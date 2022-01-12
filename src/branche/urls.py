from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *

from django.contrib.auth.decorators import permission_required
urlpatterns = [
    path('',permission_required('is_staff')(panel.as_view()),name='branche_panel'),
    path('complete/',permission_required('is_staff')(branche_complete.as_view()),name='complete_branch'),
    path('main_complete/',permission_required('is_staff')(main_branche_complete.as_view()),name='main_complete_branch'),
    path('menu/',permission_required('is_staff')(meanuList.as_view()),name='menulist_b'),
    path('add_menu/',permission_required('is_staff')(addmenu_item.as_view()),name='add_item'),
    path('menu/<int:pk>/edite',permission_required('is_staff')(edit_menu.as_view()),name='edite_menu_item'),
    path('menu/<int:pk>/delete',permission_required('is_staff')(delete_menu.as_view()),name='delete_menu_item'),
    path('<int:pk>/edite_branche/',permission_required('is_staff')(Edite_branche_Profile.as_view()),name='edite_branch'),
    path('<int:pk>/edite_user/',permission_required('is_staff')(EditeProfile.as_view()),name='edite_profile'),
    path('orders/',permission_required('is_staff')(orders.as_view()),name='orders'),
    path('orders/<int:pk>/',permission_required('is_staff')(order_details.as_view()),name='orders_item')
    


    


    

    ]