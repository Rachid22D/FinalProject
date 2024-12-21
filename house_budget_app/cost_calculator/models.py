from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# نموذج جزء من المنزل
class HousePart(models.Model):
    name = models.CharField(max_length=200)  # اسم الجزء (مثل الأساسات، الأسطح، إلخ)
    description = models.TextField(blank=True, null=True)  # وصف الجزء

    def __str__(self):
        return self.name

# نموذج العمل
class Work(models.Model):
    name = models.CharField(max_length=200)  # اسم العمل (مثل "بناء" أو "نجار")
    cost_per_hour = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # تكلفة الساعة

    def __str__(self):
        return self.name

# نموذج فئة المادة
class MaterialCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)  # اسم الفئة مثل "Foundations"
    description = models.TextField(blank=True, null=True)  # وصف الفئة (اختياري)

    def __str__(self):
        return self.name

# نموذج المادة
class Material(models.Model):
    house_part = models.ForeignKey(HousePart, on_delete=models.CASCADE, related_name="materials")  # ارتباط المادة بجزء من المنزل
    category = models.ForeignKey(MaterialCategory, on_delete=models.CASCADE, related_name="materials")  # ربط المادة بفئة معينة
    name = models.CharField(max_length=200)  # اسم المادة
    description = models.TextField()  # وصف المادة
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)  # سعر الوحدة (بافتراض الدولار)
    unit = models.CharField(max_length=50, choices=[('m2', 'Square Meter'), ('piece', 'Piece'), ('kg', 'Kilogram')])  # وحدة القياس
    material_type = models.CharField(max_length=100)  # نوع المادة مثل "Concrete", "Brick", إلخ
    
    def __str__(self):
        return self.name

# نموذج المشروع
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    PROJECT_TYPES = [
        ('complete', 'Complete'),
        ('partial', 'Partial'),
    ]
    
    BUDGET_CATEGORIES = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]
    
    PARTIAL_AREAS = [
        ('kitchen', 'Kitchen'),
        ('living_room', 'Living Room'),
        ('bedroom', 'Bedroom'),
        ('bathroom', 'Bathroom'),
        ('hallway', 'Hallway'),
        ('exterior', 'Exterior'),
    ]
    
    name = models.CharField(max_length=200)
    project_type = models.CharField(max_length=50, choices=PROJECT_TYPES)
    area = models.DecimalField(max_digits=10, decimal_places=2)  
    partial_area = models.CharField(max_length=50, choices=PARTIAL_AREAS, blank=True, null=True)  
    tart_date = models.DateTimeField(default=timezone.now)
    budget_category = models.CharField(max_length=50, choices=BUDGET_CATEGORIES)  
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)  # التكلفة الإجمالية
    
    def __str__(self):
        return self.name

# نموذج ربط المشروع بالعمل
class ProjectWork(models.Model):
    project = models.ForeignKey(
        'Project', 
        on_delete=models.CASCADE, 
        related_name="project_works"
    )  # المشروع
    work = models.ForeignKey(
        'Work', 
        on_delete=models.CASCADE, 
        related_name="project_assignments"
    )  # العمل المرتبط بالمشروع

    def __str__(self):
        return f"{self.project.name} - {self.work.name}"
