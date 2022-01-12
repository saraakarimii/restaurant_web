from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('',panel.as_view(),name='branche_panel'),
    path('complete/',branche_complete.as_view(),name='complete_branch'),
    path('main_complete/',main_branche_complete.as_view(),name='main_complete_branch'),
    path('menu/',meanuList.as_view(),name='menulist_b'),
    path('add_menu/',addmenu_item.as_view(),name='add_item'),
    path('menu/<int:pk>/edite',edit_menu.as_view(),name='edite_menu_item'),
    path('menu/<int:pk>/delete',delete_menu.as_view(),name='delete_menu_item'),
    path('<int:pk>/edite_branche/',Edite_branche_Profile.as_view(),name='edite_branch'),
    path('<int:pk>/edite_user/',EditeProfile.as_view(),name='edite_profile'),
    path('orders/',orders.as_view(),name='orders'),
    path('orders/<int:pk>/',order_details.as_view(),name='orders_item')
    


    


    

    ]