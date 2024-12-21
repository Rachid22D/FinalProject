from django.urls import path
from .views import home, user_register, user_login, new_project, user_logout, create_project, all_projects

app_name = 'cost_calculator'

urlpatterns = [
    path('', home, name='home'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('new-project/', new_project, name='new_project'),
    path('create_project/', create_project, name='create_project'),
    path('all-projects/', all_projects, name='all_projects'),
    path('logout/', user_logout, name='logout'),
]
