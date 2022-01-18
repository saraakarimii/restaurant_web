from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model
# User = get_user_model()
from .models import *
from django import forms


class CustomerRegisterForm(forms.ModelForm):
    
    
    email=forms.EmailField(required=True)
    class Meta:
        model=CostumUser
        fields=['email','username','address','password']
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user.set_password(self.cleaned_data["password"])
    #     user.is_staff=False
        
    #     print("__________________________")
    #     if commit:
    #         user.save()
    #     return user
        
        


class resturantRegisterForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=CostumUser
        fields=['email','username','address']
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_staff=True
    
        if commit:
            user.save()
        return user



# class CustomUserChangeForm(UserChangeForm):
#     class Meta: 
#         model = CostumUser
#         # fields = UserChangeForm.Meta.fields
#         fields = ('username', 'email', 'age') 
