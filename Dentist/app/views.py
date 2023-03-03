from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User 
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

def Doctors(request):
    return render(request,'Doctors.html')

def Treatments(request):
    return render(request,'Treatments.html')

def Blog(request):
    return render(request,'Blog.html')

def About(request):
    return render(request,'About.html')

def Contact(request):
    return render(request,'Contact.html')

def handleLogin(request):
    return render(request,'Login.html')

def handlesignup(request):
    if request.method=="POST":
       username=request.POST.get("username")
       email=request.POST.get("email")
       password=request.POST.get("pass1")
       confirmpassword=request.POST.get("pass2") 
     # print(username,email,password,confirmpassword)
       if password!=confirmpassword:
        messages.warning(request,"Password is Incorrect ")
        return redirect('/signup')
       
       try:
          if User.objects.get(username=username):
             messages.info(request,"UserName is Taken ")
             return redirect('/signup')
       except:
           pass
       try:
           if User.objects.get(email=email):
                messages.info(request,"Email is Taken ")
                return redirect('/signup')
       except:
           pass
      
       myuser=User.objects.create_user(username,email,password)
       myuser.save()
       messages.info(request,"Signup Success Please login ")
       return redirect('/Login')
    
    return render(request,'signup.html')


