from django.shortcuts import render

from store.models import Branche,Resturant
from .forms import *
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.dispatch import receiver
from django.db.models.signals import post_save


def SignUp(req):
    return render(req,"pages/role_signup.html")

class CostumerSignUp(generic.CreateView):
    model=Customer
    form_class=CustomerRegisterForm
    success_url=reverse_lazy('login')
    template_name='registration/signup.html'
    
class ResturantSignUp(generic.CreateView):
    model=Branche
    form_class=resturantRegisterForm
    success_url=reverse_lazy('login')
    # template_name='registration/signup.html'
    template_name='registration/signup.html'



     
def login_success(request):
    """
    Redirects users based on whether they are in the admins group
    """
    
    if request.user.is_superuser:
        return redirect("/manager/")
    if request.user.is_staff:
        return redirect("/branche/")
    else:
        return render(request,'pages/costumer/customer_panel.html')