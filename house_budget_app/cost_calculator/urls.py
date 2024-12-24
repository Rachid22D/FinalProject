from django.urls import path
from . import views #home, user_register, user_login, new_project, user_logout, all_projects, get_subcategories, get_full_house_data, get_house_part_data, save_project

app_name = 'cost_calculator'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.user_register, name='register'),
    path('login/', views.user_login, name='login'),
    path('new-project/', views.new_project, name='new_project'),
    path('all-projects/', views.all_projects, name='all_projects'),
    path('logout/', views.user_logout, name='logout'),
    path('get_subcategories/', views.get_subcategories, name='get_subcategories'),
    path('get_full_house_data/', views.get_full_house_data, name='get_full_house_data'),
    path('get_house_part_data/<int:part_id>/', views.get_house_part_data, name='get_house_part_data'),
    path('save_project/', views.save_project, name='save_project'),
    path('delete-project/<int:project_id>/', views.delete_project, name='delete_project'),


]
