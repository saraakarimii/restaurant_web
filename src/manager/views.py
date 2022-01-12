from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, UpdateView,DeleteView,CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from store.models import Food,Category
from django.contrib.auth.decorators import permission_required

@permission_required('is_superuser')
def admin_panel(req):
    return render(req,'pages/admin/admin_panel.html')

@permission_required('is_superuser')
class AllFoodList(ListView):
    model=Food
    template_name='pages/admin/food_list.html'

@permission_required('is_superuser')
class AddFood(CreateView):
    model=Food
    fields='__all__'
    template_name='pages/edite_add.html'
    success_url ="/manager/food/"

@permission_required('is_superuser')
class EditeFood(UpdateView):
    model=Food
    fields = [
        'name'
    ]
    template_name='pages/edite_add.html'
    success_url ="/manager/food/"

@permission_required('is_superuser')
class DeleteFood(DeleteView):
    model=Food
    template_name='pages/delete.html'
    success_url ="/manager/food/"

@permission_required('is_superuser')
class AllCategoryList(ListView):
    model=Category
    template_name='pages/admin/category_list.html'

@permission_required('is_superuser')
class AddCategory(CreateView):
    model=Category
    fields='__all__'
    template_name='pages/edite_add.html'
    success_url ="/manager/category/"

@permission_required('is_superuser')
class EditeCategory(UpdateView):
    model=Category
    fields = [
        'Category_title'
    ]
    template_name='pages/edite_add.html'
    success_url ="/customer/all_address/"

@permission_required('is_superuser')
class DeleteCategory(DeleteView):
    model=Category
    template_name='pages/delete.html'
    success_url ="/manager/category/"