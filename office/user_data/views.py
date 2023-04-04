from django.shortcuts import render,redirect
from .models import Emp
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages

# Create your views here.



def index(request):
       return render(request,"index.html")
    
def user_login(request):
    if request.method == "POST":
        login_username = request.POST['name']
        user_password = request.POST['password']
        
        user = authenticate(username=login_username,password=user_password)
        if user is not None:
            login(request , user)
            messages.success(request,"you are login Successfully")
            return redirect("user")
        else: 
            messages.error(request,"Invalid credential")
            return redirect('login')
     
     
    return render(request,"login.html")   



    

def sign_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST['email']
        password = request.POST["password"]
        
         
        if  len(username) > 10:
            messages.error(request,"name must be 10 character only ")
            return redirect("sign_in")
        if len(password) < 8:
            messages.error(request,"passwrod must 8 digits long ")
            return redirect("sign_in")
            
        
        user = User.objects.create_user(username,email,password )
        user.name = username
        user.passwd = password;
        user.save()
        messages.success(request, "your acount has been created Successfully...")
        
    return render(request,'sign_in.html')
        
    

def log_out(request):    
    
    logout(request) 
    messages.success(request, "Successfully Logged Out")
    return redirect("login")
       




def user(request):
    emp = Emp.objects.all()
    con = {"emp":emp}
    return render(request,"user.html",con)
    
    
    
def update(request, id):
      emp = Emp.objects.get(id=id)
      return redirect("update")
  
  

def destroy(request, id):
      emp = Emp.objects.get(id = id)
      emp.delete()
      return redirect("/user")
  
    
      
    