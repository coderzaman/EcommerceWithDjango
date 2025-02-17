from django.shortcuts import render, redirect
from django.http import HttpResponse

# Authentication form
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

# forms and model
from .forms import ProfileForm, SignUpForm
from .models import Profile, User

# message
from django.contrib import messages


# Create your views here.
def sign_up(request):
    form =  SignUpForm()
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully")
            return redirect('login_app:login')
   
    return render(request, 'LoginApp/signup.html', context={'form':form})
    

def login_user(request):
    form = AuthenticationForm()
    
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request,user)
                return HttpResponse("Successfully Login")
            else:
                return HttpResponse("Email and password not found")
    
    return render(request, 'LoginApp/login.html', context={'form':form})

@login_required
def logout_user(request):
    logout(request)
    messages.warning(request, "Your are logged out")
    return redirect("login_app:login")

@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    form = ProfileForm(instance=profile)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            form = ProfileForm(instance=profile)
    
    return render(request, 'LoginApp/change_profile.html', context={'form':form})