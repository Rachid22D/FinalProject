from django.contrib import admin
from .models import Unit, Category, SubCategory, HousePart, Project

admin.site.register(Unit)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(HousePart)
admin.site.register(Project)