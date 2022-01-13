from django.db import models
import os
import jdatetime

from django.db.models.fields import TextField



class Address(models.Model):
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=2000)
    postal_code=models.CharField(max_length=10)
    

BREAKFAST = 'B'
LUNCH = 'L'
DINNER = 'D'
MEAL_CATEGORIES = [
        (BREAKFAST, 'breakfast'),
        (LUNCH, 'lunch'),
        (DINNER, 'dinner')
    ]

class MealCategory(models.Model):
    meal=models.CharField(max_length=1,choices=MEAL_CATEGORIES)
    def __str__(self):
        return self.meal

class Category(models.Model):
    Category_title=models.CharField(max_length=50)
    def __str__(self):
        return self.Category_title

class Resturant(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Branche(models.Model):
    resturant_mother=models.ForeignKey(Resturant,on_delete=models.CASCADE,null=True)
    user=models.OneToOneField("accounts.CostumUser",on_delete=models.CASCADE,null=True,related_name='branche')
    name=models.CharField(max_length=20)
    category=models.ManyToManyField(Category,related_name="branche",null=True)
    created_at=models.DateTimeField(auto_now_add=True,null=True)
    is_main=models.BooleanField(null=True)
    description=models.TextField(max_length=3000,null=True)

    def __str__(self):
        return self.name

def get_uploade_path(self,filename):
    ext=filename.split('.')[-1]
    filename='{}.{}'.format(self.food.name,ext)
    path=f'{self.branche.name}/food/'
    return os.path.join(path,filename)

class Food(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    description=models.TextField(max_length=2000,null=True)
    food_meal=models.ManyToManyField(MealCategory,related_name="food",null=True)
    category=models.ManyToManyField(Category,related_name="food",null=True)
    def __str__(self):
        return self.name

class MenuItem(models.Model):
    branche=models.ForeignKey("Branche", on_delete=models.CASCADE,related_name="menu_item",null=True)
    price=models.IntegerField()
    food=models.ForeignKey(Food,on_delete=models.CASCADE,related_name="menu_item",null=True)
    photo=models.ImageField(upload_to=get_uploade_path,blank=True,null=True)
    quantity=models.PositiveIntegerField()
    
    
    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

class OrderItem(models.Model):
    item=models.ForeignKey(MenuItem,on_delete=models.CASCADE,null=True,related_name="order_item")
    quantity=models.PositiveIntegerField(null=True,blank=True)
    added_date=models.DateTimeField(auto_now_add=True)

    bill=models.ForeignKey("bill", on_delete=models.CASCADE,related_name="order_item",null=True)
    
    def __str__(self):
        return str(self.id)

    @property
    def get_total(self):
        total=int(self.item.price) * int(self.quantity)
        return total
    



class Customer(models.Model):
    address=models.ManyToManyField(Address,related_name="customer",null=True,blank=True)
    device=models.CharField(max_length=200,null=True,blank=True)
    user=models.OneToOneField("accounts.CostumUser", on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self):
        if str(self.user)=='None' :
            return self.device
        else:
            return str(self.user)
 
ORDERED = 'O'
RECORDED = 'R'
SENT = 'S'
DELIVERED = 'D'
ORDER_STATUS = [
        (ORDERED, 'ordered'),
        (RECORDED, 'recorded'),
        (SENT, 'sent'),
        (DELIVERED, 'delivered')
    ]
class bill(models.Model):
    owner=models.ForeignKey("Customer", on_delete=models.CASCADE,related_name="bill")
    choosen_branch=models.ForeignKey(Branche,on_delete=models.CASCADE,null=True)
    customer_status=models.CharField(max_length=1,choices=ORDER_STATUS,null=True,blank=True,default='O')
    branche_status=models.CharField(choices=ORDER_STATUS,max_length=1,null=True,blank=True)
    ordered_date=models.DateTimeField(auto_now_add=True)
    address=models.ForeignKey(Address,on_delete=models.CASCADE,null=True,blank=True)
    total_price=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return str(self.owner)

    @property
    def jalali_ordered_date(self):
        return jdatetime.datetime.fromgregorian(datetime=self.ordered_date)
    @property
    def card_total(self):
        orderitems=self.order_item.all()
        total=sum([item.get_total for item in orderitems])
        return total

