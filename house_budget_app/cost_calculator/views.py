from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, ProjectForm
import json
from django.http import JsonResponse

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


def all_projects(request):
    return render(request, 'cost_calculator/all_projects.html')


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save()
            selected_works = request.POST.getlist('works')
            budget_category = form.cleaned_data['budget_category']
            
            with open('path/to/construction_data.json') as f:
                data = json.load(f)
            
            total_cost = 0
            for work in selected_works:
                for material in data['materials']:
                    total_cost += material['average_price']
            
            labor_multiplier = 1.0
            if budget_category == 'high':
                labor_multiplier = 1.5
            elif budget_category == 'medium':
                labor_multiplier = 1.0
            else:
                labor_multiplier = 0.8
            
            total_cost *= labor_multiplier
            project.total_cost = total_cost
            project.save()

            return JsonResponse({'status': 'success', 'total_cost': total_cost})
    else:
        form = ProjectForm()
    return render(request, 'cost_calculator/new_project.html', {'form': form})

def calculate_cost(request):
    if request.method == 'POST':
        selected_works = request.POST.getlist('works')
        budget_category = request.POST.get('budget_category')
        
        with open('path/to/construction_data.json') as f:
            data = json.load(f)

        total_cost = 0
        for work in selected_works:
            for material in data['materials']:
                total_cost += material['average_price']

        labor_multiplier = 1.0
        if budget_category == 'high':
            labor_multiplier = 1.5
        elif budget_category == 'medium':
            labor_multiplier = 1.0
        else:
            labor_multiplier = 0.8
        
        total_cost *= labor_multiplier
        return JsonResponse({'status': 'success', 'total_cost': total_cost})

def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('cost_calculator:home')
