from django.db import models
from django.db.models import fields
from django.http import request
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from store.models import Address, Branche, Food , MenuItem , bill , OrderItem,Customer
from accounts.models import CostumUser
from django.views.generic import ListView, UpdateView,DeleteView,CreateView,TemplateView
from django.views.generic.edit import FormMixin
from django.contrib import messages
from .forms import AddAddressForm
from django.contrib.auth.decorators import login_required
from permissions import customer_required
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.http.response import HttpResponseRedirect

@customer_required()
class customer_panel(TemplateView):
    template_name='pages/costumer/customer_panel.html'

@login_required
def Add_Adress(request):
  if request.method == "POST":
    city=request.POST.get('city')
    address=request.POST.get('address')
    postal_code=request.POST.get('postal_code')
    adress=Address.objects.get_or_create(city=city,address=address,postal_code=postal_code)[0]
    customer=request.user.customer
    customer.address.add(adress)
    customer.save()
    form = AddAddressForm(request.POST)
    if form.is_valid():
       form.save()
    
  forma=AddAddressForm()
  return render(request, 'pages/costumer/add_address.html',{'form': forma})
@customer_required()
class AllAddressList(TemplateView):
    template_name='pages/costumer/all_adress.html'
    def get_context_data(self, **kwargs):   
        context = super().get_context_data(**kwargs)
        context['mainad'] = CostumUser.objects.get(id=self.request.user.id).address
       
        context['customer_address']=Customer.objects.get(user=self.request.user).address.all()
        return context
@customer_required()
class OrderHistoryList(ListView):
    model=bill
    template_name='pages/costumer/history_list.html'
    def get_queryset(self):
        return bill.objects.filter(owner=self.request.user.customer).filter(customer_status="R").all()

@customer_required()
class EditeProfile(UpdateView):
    model=CostumUser
    fields=["username","first_name","last_name",'address']
    template_name='pages/edite_add.html'
    success_url ="/costumer/"
    
@customer_required()
class AddressDelete(DeleteView):
    model=Address
    template_name='pages/delete.html'
    # success_url =

def deletetask(request, pk):
    
    address = Address.objects.get(id=pk)
    address.delete()
    response = redirect('/costumer/all_address/')
    return response
    
    

@customer_required()
class EditeAddress(UpdateView):
    model=Address
    fields ="__all__"
    template_name='pages/edite_add.html'
    success_url ="/costumer/all_address/"
@customer_required()
class AllBrancheList(ListView):
    model=Branche
    template_name='pages/costumer/branche_list.html'
@customer_required()
class meanuList(TemplateView):
    template_name='pages/costumer/menu_list.html'
    model=MenuItem

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list']=MenuItem.objects.filter(branche__id=kwargs['pk'])
        context['branche']=MenuItem.objects.filter(branche__id=kwargs['pk']).first()
        return context
    

@customer_required()
class OrderItemDelete(DeleteView):
    model=OrderItem
    template_name='pages/delete.html'
    success_url ="/costumer/bill/"
@customer_required()
class bill_view(TemplateView):
    PermissionError_message='you should add from one branche'
    form_class=AddAddressForm
    template_name='pages/costumer/card_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        try:
            customer=self.request.user.customer
            context['mainad'] = CostumUser.objects.get(id=self.request.user.id).address
            context['otheradd']=Customer.objects.get(user=self.request.user).address.all()
        except :
            
            device=self.request.COOKIES['device']
            
            
            customer=Customer.objects.get_or_create(device=device)[0]
        
        
        context['orders'] = OrderItem.objects.filter(bill__owner=customer).filter(bill__customer_status="O")
        context['bill_obj']=bill.objects.filter(owner=customer).filter(customer_status="O")
        
        return context

    def post(self, request, *args, **kwargs):
        
        if request.method == 'POST':

            try:
              customer=self.request.user.customer
            
            except:
                 messages.warning(request, "you should signup or login first." )
                 return redirect("/costumer/bill/")
            if request.POST.get("city"):
                print("djjdjmbhjklbvccvghjk")
                city=request.POST.get('city')
                address=request.POST.get('address')
                postal_code=request.POST.get('postal_code')
                adress=Address.objects.get_or_create(city=city,address=address,postal_code=postal_code)[0]
                customer.address.add(adress)
                customer.save()
                return redirect("/costumer/bill/")
            else:
                
                branche=OrderItem.objects.filter(bill__owner=customer).filter(bill__customer_status="O").first().item.branche
                for i in OrderItem.objects.filter(bill__owner=customer).filter(bill__customer_status="O").all():
                    if i.item.branche!=branche :
                        messages.warning(request, "you cant add from another branche." )
                        return redirect("/costumer/bill/")
                    # if not self.request.user.customer:
                    #     return redirect("/costumer/bill/")
                    item=i.item
                    quantity=i.quantity
                    item.quantity-=int(quantity)
                    item.save()
                bil=bill.objects.filter(owner=self.request.user.customer).filter(customer_status="O").first()
                
                addresss =request.POST.get("unmain_add")
                print(addresss)
                print("________________________")
                if addresss:
                    addresss =str(request.POST.get("unmain_add")).split(",")
                    city=addresss[0]
                    address=addresss[1]
                    postal_code=addresss[2]
                    adress=Address.objects.get_or_create(city=city,address=address,postal_code=postal_code)[0]
                    bil.address=adress
                else:
                    main_add=request.POST.get("main_add")
                    bil.address=main_add

                bil.customer_status='R'
                bil.choosen_branch=branche
                bil.save()
                return HttpResponseRedirect(reverse_lazy('customer_panel'))




 
@customer_required()
class Add(DetailView):
    model=MenuItem
    template_name='pages/costumer/add_item.html'
    # success_url ="/costumer/bill/"
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            item=MenuItem.objects.get(id=self.kwargs['pk'])

           
           
            try:
                customer=request.user.customer
                
            
              
            except:
                print("""""""""""")
                device=request.COOKIES['device']
                print(device)
                customer=Customer.objects.get_or_create(device=device)[0]
                print("***************")
            

            order, created=bill.objects.get_or_create(owner=customer,customer_status='O')
            
            
        
            
            quantity=request.POST.get('quantity')

            if item.quantity < int(quantity) :
                messages.warning(request, "no enough food." )
                pk=self.kwargs['pk']
                return redirect("/costumer/bill/")

            orderitem, created=OrderItem.objects.get_or_create(bill=order,item=item)
            branche=OrderItem.objects.filter(bill__owner=customer).filter(bill__customer_status="O").first().item.branche
            bil=bill.objects.filter(owner=customer).filter(customer_status="O").first()
            item.quantity-=int(quantity)
            bil.choosen_branch=branche
            bil.save()
            orderitem.quantity=quantity
            item.save()
            orderitem.save()
            return redirect("/costumer/bill/")
    

