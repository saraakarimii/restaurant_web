from django.shortcuts import render

from django.views import generic
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django.urls import reverse_lazy
from store.models import Food ,Branche, MenuItem
from django.http import JsonResponse
from django.db.models import Sum 

from django.views.generic import ListView, UpdateView,DeleteView,CreateView,TemplateView
# def theme(req):
#     return render(req,'index.html')

class main(TemplateView):
    template_name='index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menuitems'] = MenuItem.objects.all()
        
        return context
    

    def post(self, request):
        if request.is_ajax():
            text = request.POST.get('text')
            res_text=request.POST.get('res_text')
            value = request.POST.get('value')
            value_r = request.POST.get('value_r')
            
            
            
            if value=="popular_food":
                foods = MenuItem.objects.filter(order_item__bill__customer_status='R')
                sum=foods.annotate(total=Sum('order_item__quantity')).order_by('-total')[:3]
                print(sum)
                print("_____________________________")
            
                if sum:
                    data=list(sum.values('food__name',"branche__name","price",'food__id',"branche__id","photo"))
                    
                    js_f=[]
                    a=[]
                    for i in data:
                            
                        a.append(i['food__name'])
                        a.append(i['branche__name'])
                        a.append(i['price'])
                        a.append(i['food__id'])
                        a.append(i['branche__id'])
                        a.append(i["photo"])
                        js_f.append(tuple(a))
                        a=[]
                    return JsonResponse({
                    "food":js_f
                    #    "description":list(p.values_list('description', flat=True))
                    })
                else:
                    return JsonResponse({
                        'food': [],
                        'msg' : "doesn't match any files",
                    })
            elif value=="all_food":
                foods = MenuItem.objects.all()
                
                if foods:
                    data=foods.values('food__name',"branche__name","price",'food__id',"branche__id","photo")
                    print(data)
                    print("""""""""""""""""""""""""")
                    js_f=[]
                    a=[]
                    for i in data:
                            
                        a.append(i['food__name'])
                        a.append(i['branche__name'])
                        a.append(i['price'])
                        a.append(i['food__id'])
                        a.append(i['branche__id'])
                        a.append(i["photo"])
                        js_f.append(tuple(a))
                        a=[]
                    return JsonResponse({
                    "food":js_f
                    #    "description":list(p.values_list('description', flat=True))
                    })
                else:
                    return JsonResponse({
                        'food': [],
                        'msg' : "doesn't match any files",
                    })
            elif value_r:
                branche = Branche.objects.filter(menu_item__order_item__bill__customer_status='R')
                sum=branche.annotate(total=Sum('menu_item__order_item__quantity')).order_by('-total')[:3]
                print(sum)
                print("_____________________________")
            
                if sum:
                    print()
                    return JsonResponse({
                    "resturan":list(sum.values_list("name","id"))
                    #    "description":list(p.values_list('description', flat=True))
                    })
                else:
                    return JsonResponse({
                        'resturan': [],
                        'msg' : "doesn't match any files",
                    })
            elif res_text:
                
                res= Branche.objects.filter(name__startswith=res_text).all()
                
                if res:
                    return JsonResponse({
                    "resturan_search":list(res.values_list("name","id"))
                    #    "description":list(p.values_list('description', flat=True))
                    })
                else:
                    return JsonResponse({
                        "resturan_search": [],
                        'msg' : "doesn't match any files",
                    })
            
            elif text:
                    Items = MenuItem.objects.filter(food__name__startswith=text)
                    
                    
                    if Items:
                        data=list(Items.values('food__name',"branche__name","price",'food__id',"branche__id","photo"))
                        print(data)
                        js=[]
                        a=[]
                        for i in data:
                            
                            a.append(i['food__name'])
                            a.append(i['branche__name'])
                            a.append(i['price'])
                            a.append(i['food__id'])
                            a.append(i['branche__id'])
                            a.append(i["photo"])
                            js.append(tuple(a))
                            a=[]
                        

                        return JsonResponse({
                            'menu':js
                        })
                    else:
                        return JsonResponse({
                            'menu': [],
                            'msg' : "doesn't match any files",
                        })
            elif not text:
                return JsonResponse({
                            'menu': [],
                            'msg' : "doesn't match any files",
                        })

        return render(request,'index.html')

class food_slider(TemplateView):
    template_name='food_slider.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menuitems'] = MenuItem.objects.all().first()