from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    # عنوان المشروع
    title = models.CharField(max_length=255)
    
    # نوع البناء (Full House / Part of House)
    CONSTRUCTION_TYPES = [
        ('full_house', 'Full House'),
        ('part_of_house', 'Part of House'),
    ]
    type = models.CharField(max_length=50, choices=CONSTRUCTION_TYPES)
    
    # إذا كان البناء "Full House" فسيكون لدينا مساحة المنزل
    area = models.PositiveIntegerField(null=True, blank=True)  # المساحة بالمتر المربع
    
    # إذا كان البناء "Part of House" فسيكون لدينا جزء من المنزل
    part = models.CharField(max_length=255, null=True, blank=True)  # مثال: غرفة المعيشة، المطبخ
    
    # إذا كان البناء "Part of House" فسنحتاج إلى الكمية المطلوبة (مثل كمية المواد أو عدد الغرف)
    quantity = models.PositiveIntegerField(null=True, blank=True)
    
    # تاريخ الحفظ
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ربط المشروع بالمستخدم الحالي
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Unit(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the unit (e.g., Square Meter)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Name of the category (e.g., Foundations, Structure)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=100)  # Name of the subcategory (e.g., Excavation, Walls)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class HousePart(models.Model):
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name="parts")
    name = models.CharField(max_length=100)  # Name of the part (e.g., Reinforced Concrete)
    material_cost = models.DecimalField(max_digits=10, decimal_places=2)  # Material cost per unit
    labor_cost = models.DecimalField(max_digits=10, decimal_places=2)  # Labor cost per unit
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, related_name="house_parts")
    description = models.TextField(blank=True, null=True)

    def total_cost(self):
        return self.material_cost + self.labor_cost

    def __str__(self):
        return self.name
