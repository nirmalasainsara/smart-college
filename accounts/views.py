from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)
from django.shortcuts import render, redirect
from .forms import UserLoginForm,UserRegisterForm, AdminLoginForm
from django.urls import reverse
from django.template.context_processors import csrf

def login_view(request):
    form = UserLoginForm(request.POST or None) 
    if form.is_valid():  
        username = form.cleaned_data.get('username') 
        password = form.cleaned_data.get('password') 
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect(reverse("college:course_list"))
    return render(request, "accounts/form.html", {"form":form})

def register_view(request):
    form = UserRegisterForm(request.POST or None) 
    if form.is_valid():  
        user = form.save(commit=False)
        password = form.cleaned_data.get('password') 
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        return redirect("/")
        
    context = {
        "form":form
    }
    return render(request, "accounts/form.html", context)

def logout_view(request):
    logout(request)
    return redirect(reverse("accounts:login"))

def admin_login_view(request):
    adminform = AdminLoginForm(request.POST or None) 
    if adminform.is_valid():  
        adminname = adminform.cleaned_data.get('adminname') 
        password = adminform.cleaned_data.get('password') 
        admin = authenticate(username=adminname, password=password)
        login(request, admin)
        return redirect("college:paper_list")
    context = {
        "adminform":adminform
    }
    context.update(csrf(request))
    return render(request, "accounts/adminform.html", context)
