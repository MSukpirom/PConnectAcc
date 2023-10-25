from django.urls import path
from . import views

app_name = 'Taskscontroller'

urlpatterns = [
    path('index/', views.checkdata, name='Index'),
    path('cilent/', views.RegisterForm, name='RegisterForm'),
    path('GetProvinces/',views.GetProvinces,name='GetProvinces'),
    path('GetDistrict/',views.GetDistrict,name='GetDistrict'),
    path('GetSubdistrict/',views.GetSubdistrict,name='GetSubdistrict'),
    path('egagement/',views.RegisterEgagement,name='RegisterEgagement'),
    path('taskscontrol/',views.TasksControl,name='TasksControl'),
]