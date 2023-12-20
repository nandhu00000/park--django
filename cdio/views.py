# from django.shortcuts import render,redirect
import django
from django.http import HttpResponse
# # from .models import login_record,signup
from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login 
from django.contrib.auth.forms import AuthenticationForm
# from .forms import LoginForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from .models import RegUser

 

# Create your views here.

def home (request):
    #  return render (request,"index.html")
    return HttpResponse("<h1>successfully logined yuor data</h2>")

def register(request):
    if request.method == "POST":
        if request.POST.get('submit') == 'register':
            username= request.POST.get['username']
            department= request.POST.get['department']
            password= request.POST.get['password1']
            con_password= request.POST.get['password2']

            user = RegUser.objects.filter(Department = department)
            if user :
                messages = "user alresdy exists"
                return render (request,"register.html",{'msg':messages})
            else:
                if password == con_password:
                    newuser = RegUser.objects.create(username=username,department= department,password=password,con_password=con_password)
                    return redirect ("dashbord") 
                else:
                    return redirect("home")
            # data= User.objects.create_user(username=username,email=email,password=password1)
            # data.save()
            # return HttpResponse("<h1>successfully registration your data</h2>")
        print("thanks")
        # pro= request.POST['sign'] 
        # password_s= request.POST['password_s']
        
        # print("continuing on auth statement")

        # user= authenticate(request,username=pro,password=password_s)
        # if user.is_valid():
        #     user.save
        # # if user is not None:   
        # #     login(request,user)
        # #     return HttpResponse("<h1>successfully logined yuor data</h2>")
        # else:
        #      return HttpResponse("<h1>successfully logined yuor data</h2>")
    return render (request,"signup.html")
def login1(request):
    if request.method == "POST":
        print("step1")
        # if request.POST.get('submit') == 'login':
        print("step3")
        username= request.POST.get('user')
        password = request.POST.get('password')
        print("step2")
        user= authenticate(request,username=username,password=password)
        if user is not None:   
            login(request,user)
            return HttpResponse("<h1>successfully logined yuor data</h2>")
        else:
            return HttpResponse("<h1>successfully logined yuor data</h2>")
    # else:
    #     return HttpResponse("<h1>successfully logined yuor data</h2>")
    else:
        return render (request,"signup.html")

def login2(request):
    con=AuthenticationForm()
    return render ( request, 
                    template_name= "dashbord.html",
                    context={'form':con}

    )











def signup(request):
    if request.method == "POST":
        username=   request.POST['username']
        department= request.POST['department']
        password=  request.POST['password1']
        con_password=  request.POST['password2']
       
        data= User.objects.create_user(username=username,email=department,password=password)
        # user= RegUser.objects.filter(Email = department)
        data.save()
       # try:
        #     data.save()
        # except django.db.utils.IntegrityError:
        #     messages = "user alresdy exists"
        #     data.save()
        #     return render (request,"register.html",{'msg':messages})
        
        # return redirect ("login")
        # print("thanks") 
            
    #     user = User.objects.filter(username= username)
    #     if user:
    #         messages = "user alresdy exists"
    #         return render (request,"register.html",{'msg':messages})
    #     else:
    #         if password == con_password:
    #             newuser = User.objects.create(username=username,department= department,password=password,con_password=con_password)
    #             return redirect ("dashbord") 
    #         else:
    #             return redirect("home")
    return render (request,"register.html")
def check(request):
    
    try:  
       a=User.objects.create_user(username="nandha",first_name="meeeon",email="mechanical",password="pass",department="robotics") 
       a.save()
       print("thank you")
    except AttributeError:
        print("this is error method")
    return HttpResponse("<h1> thank you </h1>")
def sign_in(request):
    print("step 3 ")
    if request.method == 'POST':
        print("step 2 ")

        username =  request.POST['username']
        password =  request.POST['password']
        print("step 1")
        user = authenticate(request,username=username,password=password)
        print("thanks")
        if user is not None:   
            login(request,user)
            return redirect ('dashbord')
        else:
            return redirect ('register')
         
        # if user:
        #         login(request, user)
        #         messages.success(request,f'Hi {username.title()}, welcome back!')
        #         return redirect('posts')
    else:
        return render (request,"logpro.html")   
        
def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out.')
    return redirect('register')        
def syll(request):
    return render (request , "dashboard_pages/syllabus.html")
def dashbord(request):
    return render (request, "dashbord.html")