from urllib import response
from wsgiref.util import request_uri
from django.shortcuts import render,redirect, HttpResponse
from . models import *
# Create your views here.

#views for registration page

def RegisterPage(request):
    return render(request,"app/register.html")

    # views for user registration
def UserRegister(request):
    if request.method =="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['cpassword']


        #first we will validate that user already exists
        user= User.objects.filter(Email=email)
        if user:
            message ="User already exists"
            return render(request,"app/register.html",{'msg':message})
        else:
            if password==cpassword:
                newuser=User.objects.create(Firstname=fname, Lastname=lname, Email=email, Contact=contact,Password=password)
                message="User register Succesfully"

                return render(request, "app/login.html")
                return response

            else:
                message="Password doesn't match"
                return render(request,"app/register.html",{'msg':message})


#for login page view
def LoginPage(request):
    return render(request,"app/login.html")



#login user
def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking the emailid with database
        user = User.objects.get(Email=email)

        if user:
            if user.Password == password:
                # We are getting user data in session
                request.session['Firstname'] = user.Firstname
                request.session['Lastname'] = user.Lastname
                request.session['Email'] = user.Email
                return render(request,"app/home.html")
            else:
                message = "Password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"app/register.html",{'msg':message})