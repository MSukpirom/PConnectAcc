from django.urls import path
from . import views

app_name = 'Taskscontroller'

urlpatterns = [
    path('index/', views.checkdata, name='Index'),
    path('', views.RegisterForm, name='RegisterForm'),
    path('GetProvinces/',views.GetProvinces,name='GetProvinces'),
    path('GetDistrict/',views.GetDistrict,name='GetDistrict'),
    path('GetSubdistrict/',views.GetSubdistrict,name='GetSubdistrict'),
]