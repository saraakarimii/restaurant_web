from django.shortcuts import render

from django.views import generic
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.urls import reverse_lazy
from store.models import Food ,Branche
from django.http import JsonResponse
from django.db.models import Sum 

# def theme(req):
#     return render(req,'index.html')

def main(req):
    

        if req.method == 'POST'  and req.is_ajax():
            value = req.POST.get('value')
            if value=="food":
                foods = Food.objects.filter(menu_item__order_item__bill__customer_status='R')
                sum=foods.annotate(total=Sum('menu_item__order_item__quantity')).order_by('-total')[:10]
                print(sum)
                print("_____________________________")
            
                if sum:
                    print()
                    return JsonResponse({
                    "food":list(sum.values_list("name"))
                    #    "description":list(p.values_list('description', flat=True))
                    })
                else:
                    return JsonResponse({
                        'food': [],
                        'msg' : "doesn't match any files",
                    })
            if value=="resturan":
                branche = Branche.objects.filter(menu_item__order_item__bill__customer_status='R')
                sum=branche.annotate(total=Sum('menu_item__order_item__quantity')).order_by('-total')[:10]
                print(sum)
                print("_____________________________")
            
                if sum:
                    print()
                    return JsonResponse({
                    "food":list(sum.values_list("name"))
                    #    "description":list(p.values_list('description', flat=True))
                    })
                else:
                    return JsonResponse({
                        'food': [],
                        'msg' : "doesn't match any files",
                    })
        return render(req,'index.html')