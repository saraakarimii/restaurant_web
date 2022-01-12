from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from .views import *
urlpatterns = [
    path('',customer_panel,name='customer_panel'),
    path('<int:pk>/edite/',EditeProfile.as_view(),name='edite_profile'),
    path('add_address/',Add_Adress,name='add_address'),
    path('all_address/',AllAddressList.as_view(),name='all_address'),
    path('address/<int:pk>/edite',EditeAddress.as_view(),name="edite_add"),
    path('address/<int:pk>/delete', OrderItemDelete.as_view(),name='delete_add'),
    path('history/',OrderHistoryList.as_view(),name='order_history'),
    path('branche/', AllBrancheList.as_view(),name='branches'),
    path('branche/<int:pk>', meanuList.as_view(),name='menui'),
    path('branche/add_food/<int:pk>', Add.as_view(),name='add'),
    path('bill/',bill_view.as_view(),name='card'),
    
    path('bill/<int:pk>/delete', OrderItemDelete.as_view(),name='fdelete')
]