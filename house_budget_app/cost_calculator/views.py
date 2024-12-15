from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
# Create your views here.

def home(request):
    return render(request, 'cost_calculator/home.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful. You can now log in.")
            return redirect('login')  
    else:
        form = CustomUserCreationForm()

    return render(request, 'cost_calculator/register.html', {'form': form})
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect('home')  # Redirect to home after login
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'cost_calculator/login.html')
