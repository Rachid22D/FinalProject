from django.urls import path
from .views import home, register, login


app_name = 'cost_calculator'

urlpatterns = [
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
