from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin 
from .forms import CustomerRegisterForm, CustomUserChangeForm 
from .models import *


class CustomUserAdmin(admin.ModelAdmin): 
    add_form = CustomerRegisterForm 
    form = CustomUserChangeForm 
    model = CostumUser
    list_display = ['email', 'username', 'age', 'is_staff', ]

admin.site.register(CostumUser, CustomUserAdmin)


@admin.register(Customer)
class CustomerProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'age']
    list_display_links = ['id']
    list_editable = ['age', 'email']
    search_fields = ['username', 'email']
   
    

    def get_queryset(self, request):
        return Customer.objects.filter(is_staff=False)


@admin.register(Staff)
class StaffProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'age']
    list_display_links = ['username']
    list_editable = ['age', 'email']
    search_fields = ['username', 'email']
   

    def get_queryset(self, request):
        return Staff.objects.filter(is_staff=True, is_superuser=False)
        



@admin.register(Admin)
class AdminProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email', 'age']
    list_display_links = ['username']
    list_editable = ['age', 'email']
    search_fields = ['username', 'email']
   
    def get_queryset(self, request):
        return Admin.objects.filter(is_superuser=True)




