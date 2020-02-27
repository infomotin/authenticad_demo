from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
# import form in django 
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from authenticate.forms import RegisterForm,EditForm,PasswordChangF

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
def edit_profile(request):
    if request.method == "POST":
        form = EditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(request,username=username,password=password)
            # login(request,user)
            messages.success(request,("You Have Successfull Edit Your Profile ...... "))
            return redirect('index')
        
            
    else:
        form = EditForm(instance=request.user)
    context={'form':form}
    return render(request,'authenticate/edit_user.html',context)

def change_password(request):
    if request.method == "POST":
        form = PasswordChangF(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            # for update Session
            update_session_auth_hash(request,form.user)
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(request,username=username,password=password)
            # login(request,user)
            messages.success(request,("You Have Successfull Edit Your Profile ...... "))
            return redirect('index')
        
            
    else:
        form = PasswordChangF(user=request.user)
    context={'form':form}
    return render(request,'authenticate/change_user_password.html',context)