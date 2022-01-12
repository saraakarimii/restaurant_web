from django.urls import path,include
from .views import *
urlpatterns = [
    path(r'login_success/$', login_success, name='login_success'),
    path('signup/',SignUp,name='signup'),
    path('signup/costumer',CostumerSignUp.as_view(),name="csignup"),
    path('signup/resturant',ResturantSignUp.as_view(),name="rsignup")
    
]