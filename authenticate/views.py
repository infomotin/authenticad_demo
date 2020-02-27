from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from authenticate.forms import RegisterForm

# Create your views here.
def home(request):
    context={}
    return render(request,'authenticate/home.html',context)

def login_user(request):
    context={}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,("You Have Successfull for Log in "))
            return redirect('index')
            
        else:
            messages.success(request,("You Have UnSuccessfull for Log in "))
            return redirect('login_user')

    
    else:

        return render(request,'authenticate/login_user.html',context)

def logout_user(request):
    messages.success(request,("You Have Successfull for Log out "))
    logout(request)
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request,username=username,password=password)
            login(request,user)
            messages.success(request,("You Have Successfull Register...... "))
            return redirect('index')
        
            
    else:
        form = RegisterForm()
    context={'form':form}
    return render(request,'authenticate/register_user.html',context)
