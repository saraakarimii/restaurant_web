from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, UpdateView,DeleteView,CreateView
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from store.models import Food,Category
def admin_panel(req):
    return render(req,'pages/admin/admin_panel.html')

class AllFoodList(ListView):
    model=Food
    template_name='pages/admin/food_list.html'
class AddFood(CreateView):
    model=Food
    fields='__all__'
    template_name='pages/edite_add.html'
    success_url ="/manager/food/"
class EditeFood(UpdateView):
    model=Food
    fields = [
        'name'
    ]
    template_name='pages/edite_add.html'
    success_url ="/manager/food/"

class DeleteFood(DeleteView):
    model=Food
    template_name='pages/delete.html'
    success_url ="/manager/food/"

class AllCategoryList(ListView):
    model=Category
    template_name='pages/admin/category_list.html'

class AddCategory(CreateView):
    model=Category
    fields='__all__'
    template_name='pages/edite_add.html'
    success_url ="/manager/category/"

class EditeCategory(UpdateView):
    model=Category
    fields = [
        'Category_title'
    ]
    template_name='pages/edite_add.html'
    success_url ="/customer/all_address/"

class DeleteCategory(DeleteView):
    model=Category
    template_name='pages/delete.html'
    success_url ="/manager/category/"