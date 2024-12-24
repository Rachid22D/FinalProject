import os
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .forms import CustomUserCreationForm
from django.http import JsonResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from .models import SubCategory, HousePart, Project


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

def get_subcategories(request):
    subcategories = SubCategory.objects.all()
    data = {
        'subcategories': [
            {'id': subcategory.id, 'name': subcategory.name} 
            for subcategory in subcategories
        ]
    }
    return JsonResponse(data)

def get_full_house_data(request):
    house_parts = HousePart.objects.all()
    data = {
        'house_parts': [
            {
                'name': part.name,
                'material_cost': str(part.material_cost),
                'labor_cost': str(part.labor_cost),
                'unit': part.unit.name
            }
            for part in house_parts
        ]
    }
    return JsonResponse(data)

def get_house_part_data(request, part_id):
    try:
        part = HousePart.objects.select_related('subcategory', 'subcategory__category', 'unit').get(pk=part_id)
        data = {
            'id': part.id,
            'name': part.name,
            'description': part.description,
            'material_cost': float(part.material_cost),
            'labor_cost': float(part.labor_cost),
            'total_cost': float(part.total_cost()),
            'unit': {
                'id': part.unit.id,
                'name': part.unit.name,
            },
            'subcategory': {
                'id': part.subcategory.id,
                'name': part.subcategory.name,
                'description': part.subcategory.description,
                'category': {
                    'id': part.subcategory.category.id,
                    'name': part.subcategory.category.name,
                    'description': part.subcategory.category.description,
                },
            },
        }
        return JsonResponse(data)
    except HousePart.DoesNotExist:
        return JsonResponse({'error': 'House part not found'}, status=404)




def new_project(request):

    return render(request, 'cost_calculator/new_project.html')



@login_required  # التأكد من أن المستخدم مسجل دخوله
@csrf_exempt  # يمكن إضافة csrf_exempt إذا كنت تستخدم fetch مع csrftoken
def save_project(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        type = data.get('type')
        area = data.get('area')
        part = data.get('part')
        quantity = data.get('quantity')
        if type == "Part of House":
            house_part = get_object_or_404(HousePart, id=int(part))
            project = Project.objects.create(
            title=title,
            type=type,
            area=area,
            part=house_part,
            quantity=quantity,
            user=request.user  # ربط المشروع بالمستخدم الحالي
        )
        else:  
            # ربط المشروع بالمستخدم الحالي
            project = Project.objects.create(
                title=title,
                type=type,
                area=area,
                part=part,
                quantity=quantity,
                user=request.user  # ربط المشروع بالمستخدم الحالي
            )

        return JsonResponse({'success': True})

    return JsonResponse({'success': False})

    
@login_required
def all_projects(request):
    user_projects = Project.objects.filter(user=request.user)[::-1]
    
    return render(request, 'cost_calculator/all_projects.html', {'projects': user_projects})

@login_required
def delete_project(request, project_id):
    if request.method == "POST" and request.is_ajax():
        project = get_object_or_404(Project, id=project_id, user=request.user)
        project.delete()
        return JsonResponse({'success': True, 'message': 'Project has been deleted successfully.'})
    return JsonResponse({'success': False, 'message': 'Invalid request.'}, status=400)


def user_logout(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('cost_calculator:home')
