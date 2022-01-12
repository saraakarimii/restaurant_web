from .models import CostumUser
from store.models import Customer ,Branche
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=CostumUser)
def create_profile(sender, instance, created, **kwargs):
    
   
    if created :
        if instance.is_staff:

           Branche.objects.create(user=instance)
           
        else:
            Customer.objects.create(user=instance)