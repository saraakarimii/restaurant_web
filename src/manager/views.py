from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, UpdateView,DeleteView,CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from store.models import Food,Category
from django.contrib.auth.decorators import permission_required
from permissions import superuser_required
@superuser_required()
class admin_panel(TemplateView):
     template_name='pages/admin/admin_panel.html'

@superuser_required()
class AllFoodList(ListView):
    model=Food
    template_name='pages/admin/food_list.html'
@superuser_required()
class AddFood(CreateView):
    model=Food
    fields='__all__'
    template_name='pages/edite_add.html'
    success_url ="/manager/food/"
@superuser_required()
class EditeFood(UpdateView):
    model=Food
    fields = [
        'name'
    ]
    template_name='pages/edite_add.html'
    success_url ="/manager/food/"
@superuser_required()
class DeleteFood(DeleteView):
    model=Food
    template_name='pages/delete.html'
    success_url ="/manager/food/"
@superuser_required()
class AllCategoryList(ListView):
    model=Category
    template_name='pages/admin/category_list.html'
@superuser_required()
class AddCategory(CreateView):
    model=Category
    fields='__all__'
    template_name='pages/edite_add.html'
    success_url ="/manager/category/"
@superuser_required()
class EditeCategory(UpdateView):
    model=Category
    fields = [
        'Category_title'
    ]
    template_name='pages/edite_add.html'
    success_url ="/customer/all_address/"
@superuser_required()
class DeleteCategory(DeleteView):
    model=Category
    template_name='pages/delete.html'
    success_url ="/manager/category/"