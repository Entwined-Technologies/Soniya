from django.urls import path
from . import views

urlpatterns = [
    path("", views.RegisterPage,name='registerpage'),
    path("register/",views.UserRegister,name='userregister'),
    path('login/',views.LoginPage,name='loginpage'),
    path("loginuser/",views.LoginUser,name="login"),
]