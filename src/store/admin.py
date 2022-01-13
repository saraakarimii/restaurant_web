from django.contrib import admin
from django.utils.html import format_html
# Register your models here.
from django.contrib import admin
from .models import *
@admin.register(Resturant)
class Restrant_admin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Branche)
class Branche_admin(admin.ModelAdmin):
    list_display = ['name','resturant',"menu"]
    list_filter=['resturant_mother__name']


    @admin.display(description="resturant ")
    def resturant(self,obj):
        return obj.resturant_mother.name
    @admin.display(description="menu ")
    def menu(self,obj):
        return" ,\n".join([f'{m.food.name}({m.price})' for m in obj.menu_item.all()])
        


@admin.register(Food)
class Food_admin(admin.ModelAdmin):
    list_display = ['name','description','meal',"category_food"]
    search_fields = ['name','food__name']
    list_filter=['food_meal__meal',"category__Category_title"]
    @admin.display(description="meal ")
    def meal(self,obj):
        return" ,".join([m.meal for m in obj.food_meal.all()])
    @admin.display(description="category ")
    def category_food(self,obj):
        return" ,".join([m.Category_title for m in obj.category.all()])

@admin.register(MenuItem)
class Menu_admin(admin.ModelAdmin):
    list_display = ['food_name','branche_name',"quantity","price"]#,'image_tag'
    list_filter=['branche__name']

    @admin.display(description="food name ")
    def food_name(self,obj):
        return str(obj.food.name)

    
    @admin.display(description="branche ")
    def branche_name(self,obj):
        return obj.branche
    
    # def image_tag(self, obj):
    #     return format_html('<img src="{}" />'.format(obj.photo.url))
    # image_tag.short_description = 'Image'

@admin.register(Address)     #ok
class Menu_admin(admin.ModelAdmin):
    list_display = ['city',"address",'postal_code']
    list_filter=["city"]

@admin.register(OrderItem)
class Order_Item_admin(admin.ModelAdmin):
    
    list_display = ["branche_ordered","customer_ordered",'food_name',"food_price","quantity","added_date"]
    search_fields = ['quantity']
    @admin.display(description="branche ")
    def branche_ordered(self,obj):
        return obj.item.branche.name

    @admin.display(description="food name")
    def food_name(self,obj):
        return obj.item.food.name
    @admin.display(description="food price")
    def food_price(self,obj):
        return obj.item.price

    @admin.display(description="customer")
    def customer_ordered(self,obj):
        return obj.bill.owner 

@admin.register(bill)  #ok
class bill_admin(admin.ModelAdmin):
    list_display = ['owner',"branche_bill","items","ordered_date"]
    search_fields=['choosen_branch__name',"owner__user__first_name","owner__user__last_name"]
    @admin.display(description="items ")
    def items(self,obj):
        return" ,\n".join([f'{m.item.food.name}({m.item.price})' for m in obj.order_item.all()])
    @admin.display(description="branche ")
    def branche_bill(self,obj):
        return  obj.choosen_branch.name

 




# admin.site.register(Branche)
# admin.site.register(bill)
admin.site.register(Category)
admin.site.register(MealCategory)

admin.site.register(Customer)
# admin.site.register(OrderItem)




