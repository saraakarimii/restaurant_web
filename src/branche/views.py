from django.db import models
from django.db.models import fields
from django.shortcuts import render
from store.models import Branche, Resturant,MenuItem,bill
from django.views.generic import ListView, UpdateView,DeleteView,CreateView,TemplateView
from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect, HttpResponse
from accounts.models import CostumUser
from permissions import is_staff_required

@is_staff_required()
class panel(TemplateView):
    def post(self, request):
        main=request.POST.get('is_main')
        
        if main=="yes":
            print("***************")
            return HttpResponseRedirect(reverse_lazy("main_complete_branch"))
        else:
            return HttpResponseRedirect(reverse_lazy("complete_branch"))


    
    template_name='pages/branche/panel.html'
    
    
@is_staff_required()
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

@is_staff_required()
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

@is_staff_required()
class meanuList(ListView):
    template_name='pages/branche/menu_list_branche.html'
    model=MenuItem
    def get_queryset(self):
     
        qs =super().get_queryset() 
        branche_user=Branche.objects.get(user=self.request.user)
        return qs.filter(branche=branche_user)

@is_staff_required()
class addmenu_item(CreateView):
    model=MenuItem
    fields=["price",'food','quantity','photo']
    template_name='pages/branche/add_menu_item.html'
    success_url ="/branche/menu/"
    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        branche_user=Branche.objects.get(user=self.request.user)
        self.object = form.save(commit=False)
        self.object.branche=branche_user
        self.object = form.save()
        print(self.object)
        return super().form_valid(form)

@is_staff_required()
class edit_menu(UpdateView):
    model=MenuItem
    fields=["price",'food','quantity','photo']
    template_name='pages/edite_add.html'
    success_url ="/branche/menu/"

@is_staff_required()
class delete_menu(DeleteView):
    model=MenuItem
    template_name='pages/delete.html'
    success_url ="/branche/menu/"


@is_staff_required()
class Edite_branche_Profile(UpdateView):
    model=Branche
    fields="__all__"
    template_name='pages/edite_add.html'
    success_url ="/branche/"

@is_staff_required()
class EditeProfile(UpdateView):
    model=CostumUser
    fields=["username","first_name","last_name","email","address"]
    template_name='pages/edite_add.html'
    success_url ="/branche/"
@is_staff_required()

class orders(TemplateView):
    template_name='pages/branche/orders.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        branche_user=Branche.objects.get(user=self.request.user)
        context['bills']=bill.objects.filter(choosen_branch=branche_user).all()
        
        return context

    def post(self, request):
        b_status=request.POST.get('branche_status')
        c_status=request.POST.get('customer_status')
       
        
        
        if b_status:
            b_status=str(request.POST.get('branche_status')).split(',')
            print(b_status)
            print("_________________")
            if b_status[1]=='recorded':
                targeted_bill=bill.objects.get(id=b_status[0])
                targeted_bill.branche_status="R"
                targeted_bill.save()
            if b_status[1]=='sent':
                targeted_bill=bill.objects.get(id=b_status[0])
                targeted_bill.branche_status="S"
                targeted_bill.save()
            if b_status[1]=='delivered':
                targeted_bill=bill.objects.get(id=b_status[0])
                targeted_bill.branche_status="D"
                targeted_bill.save()

        elif c_status:
            c_status=str(request.POST.get('customer_status')).split(',')
            print(c_status)
            print("++++++++++++++++++++++++++")
            
            if c_status[1]=='recorded':
                targeted_bill=bill.objects.get(id=c_status[0])
                targeted_bill.customer_status="R"
                targeted_bill.save()
            if c_status[1]=='sent':
                targeted_bill=bill.objects.get(id=c_status[0])
                targeted_bill.customer_status="S"
                targeted_bill.save()
            if c_status[1]=='delivered':
                targeted_bill=bill.objects.get(id=c_status[0])
                targeted_bill.customer_status="D"
                targeted_bill.save()
        return HttpResponseRedirect(reverse_lazy('orders'))
        


        

@is_staff_required()
class order_details(ListView):
    model=bill
    template_name='pages/branche/order_detail.html'
    def get_queryset(self):
        return bill.objects.filter(id=self.kwargs['pk']).all()
    



