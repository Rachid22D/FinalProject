from django.urls import path
from .views import home, user_register, user_login, new_project, all_projects, user_logout, create_project, calculate_cost

app_name = 'cost_calculator'

urlpatterns = [
    path('', home, name='home'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('new-project/', new_project, name='new_project'),
    path('all-projects/', all_projects, name='all_projects'),
    path('logout/', user_logout, name='logout'),
    path('create-project/', create_project, name='create_project'),
    path('calculate-cost/', calculate_cost, name='calculate_cost'),
]
