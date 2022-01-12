
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE

class CostumUser(AbstractUser):
    username = models.CharField(max_length=150,unique=False)
    age=models.PositiveBigIntegerField(null=True,blank=True)
    email=models.EmailField()#unique=True
    device=models.CharField(max_length=200,null=True,blank=True)
    address=models.CharField(max_length=50,null=True)
class Customer(CostumUser):
    def save(self, *args, **kwargs):
            self.is_staff = False

    class Meta:
        proxy=True
        verbose_name='customer'
        verbose_name_plural ='customers'

class Staff(CostumUser):
    def save(self, *args, **kwargs):
            self.is_staff = True

    class Meta:
        proxy = True
        verbose_name: 'branche'
        verbose_name_plural = 'branches'

class Admin(CostumUser):
    def save(self, *args, **kwargs):
            self.is_superuser = True

    class Meta:
        proxy = True
        verbose_name: 'manager'
        verbose_name_plural = 'managers'


