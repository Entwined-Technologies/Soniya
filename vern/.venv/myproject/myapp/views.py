from django.shortcuts import render
from .models import *

#register view web page
def RegisterPage(request):
    return render(request,"myapp/register.html")

#new signup data validation
def UserRegister(request):
        if request.method == "POST":
            fname = request.POST['fname']
            lname = request.POST['lname']
            email = request.POST['email']
            contact = request.POST['contact']
            password = request.POST['password']
            cpassword = request.POST['cpassword']

            # validate user already exist
            user = signup.objects.filter(Email=email)

            if user:
                message = "User already exist"
                return render(request,"myapp/register.html",{'msg':message})
            else:
                if password == cpassword:
                    newuser = signup.objects.create(Firstname=fname,Lastname=lname,Email=email
                                        ,Contact=contact,Password=password)
                    message = "User registered Successfully"
                    return render(request,"myapp/login.html",{'msg':message})
                else:
                    message = "Password and Confirm Password Doesnot Match"
                    return render(request,"myapp/register.html",{'msg':message})
                

#view login webpage
def LoginPage(request):
    return render(request, "myapp/login.html")


# Login User data validation
def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking emailid
        user = signup.objects.get(Email=email)

        if user:
            if user.Password == password:
                # We are getting user data in session
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                return render(request,"myapp/home.html")
            else:
                message = "Password does not match"
                return render(request,"myapp/login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"myapp/register.html",{'msg':message})
