import os
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, ProjectForm
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, HousePart, Material, Work


def home(request):
    return render(request, 'cost_calculator/home.html')

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('cost_calculator:login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'cost_calculator/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('cost_calculator:home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'cost_calculator/login.html')

def new_project(request):
    return render(request, 'cost_calculator/new_project.html')



def create_project(request):
    pass
    
    
@login_required
def all_projects(request):
   
    # تمرير المشاريع إلى القالب
    return render(request, 'cost_calculator/all_projects.html')




def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('cost_calculator:home')
