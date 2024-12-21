from django.contrib import admin
from .models import Project, HousePart, Work, Material, MaterialCategory

admin.site.register(Project)
admin.site.register(HousePart)
admin.site.register(Work)
admin.site.register(Material)
admin.site.register(MaterialCategory)