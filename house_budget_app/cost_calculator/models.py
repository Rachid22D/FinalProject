from django.db import models

# Create your models here.

from django.db import models

class Project(models.Model):
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
    start_date = models.DateTimeField()  
    budget_category = models.CharField(max_length=50, choices=BUDGET_CATEGORIES)  
    total_cost = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)  # التكلفة الإجمالية
    def __str__(self):
        return self.name
    
