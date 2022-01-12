from django.db import models
from django.db.models import fields
from django.shortcuts import render
from store.models import Branche, Resturant,MenuItem,bill
from django.views.generic import ListView, UpdateView,DeleteView,CreateView,TemplateView
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect, HttpResponse
from accounts.models import CostumUser
def panel_branche(req):
    return render(req,'pages/branche/panel.html')

class panel(TemplateView):
    def post(self, request):
        main=request.POST.get('is_main')
        
        if main=="yes":
            print("***************")
            return HttpResponseRedirect(reverse_lazy("main_complete_branch"))
        else:
            return HttpResponseRedirect(reverse_lazy("complete_branch"))


    
    template_name='pages/branche/panel.html'
    
    

class branche_complete(TemplateView):
    template_name='pages/branch_complete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['choices']=Resturant.objects.filter().all()
        return context

    def post(self, request):
        name=request.POST.get('name')
        resturan=request.POST.get('resturant')
       
        branche_user=Branche.objects.get(user=self.request.user)
        branche_user.name=name
        # print(Resturant.objects.filter(name=resturan).first())
        res=Resturant.objects.get(name=resturan)
       
        branche_user.resturant_mother=res

        branche_user.save()
        return HttpResponseRedirect(reverse_lazy('branche_panel'))

class main_branche_complete(TemplateView):
    template_name='pages/main_branche_complete.html'

    def post(self, request):
        name=request.POST.get('branche_name')
        resturan=request.POST.get('res_name')
        
        branche_user=Branche.objects.get(user=self.request.user)
        branche_user.name=name
        branche_user.is_main=True
        res=Resturant.objects.create(name=resturan)
        branche_user.resturant_mother=res
        branche_user.save()
        return HttpResponseRedirect(reverse_lazy('branche_panel'))


class meanuList(ListView):
    template_name='pages/branche/menu_list_branche.html'
    model=MenuItem
    def get_queryset(self):
     
        qs =super().get_queryset() 
        branche_user=Branche.objects.get(user=self.request.user)
        return qs.filter(branche=branche_user)

class addmenu_item(CreateView):
    model=MenuItem
    fields=["price",'food','quantity']
    template_name='pages/branche/add_menu_item.html'
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        branche_user=Branche.objects.get(user=self.request.user)
        self.object = form.save(commit=False)
        self.object.branche=branche_user
        self.object = form.save()
        print(self.object)
        return super().form_valid(form)

class edit_menu(UpdateView):
    model=MenuItem
    fields=["price",'food','quantity']
    template_name='pages/edite_add.html'
    success_url ="/branche/menu/"

class delete_menu(DeleteView):
    model=MenuItem
    template_name='pages/delete.html'
    success_url ="/branche/menu/"


class Edite_branche_Profile(UpdateView):
    model=Branche
    fields="__all__"
    template_name='pages/edite_add.html'
    success_url ="/branche/"

class EditeProfile(UpdateView):
    model=CostumUser
    fields=["username","first_name","last_name","email","address"]
    template_name='pages/edite_add.html'
    success_url ="/branche/"

class orders(TemplateView):
    template_name='pages/branche/orders.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branche_user=Branche.objects.get(user=self.request.user)
        context['bills']=bill.objects.filter(choosen_branch=branche_user).all()
        
        return context

# class (TemplateView):
#     template_name='pages/branche/order_detail.html'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         branche_user=Branche.objects.get(user=self.request.user)
#         context['obj']=bill.objects.filter(id=kwargs['pk']).all()
#         return context

class order_details(ListView):
    model=bill
    template_name='pages/branche/order_detail.html'
    def get_queryset(self):
        return bill.objects.filter(id=self.kwargs['pk']).all()
    



