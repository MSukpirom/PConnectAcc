from django.urls import path
from . import views

app_name = 'Taskscontroller'

urlpatterns = [
    path('index/', views.checkdata, name='Index'),
    path('regis_form/', views.RegisterForm, name='RegisterForm'),
]