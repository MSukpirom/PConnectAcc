from django.urls import path
from . import views

app_name = 'Taskscontroller'

urlpatterns = [
    path('checkdata/', views.checkdata, name='Checkdata'),
    path('forms_client/', views.forms_client, name='FormsClient'),
    path('get_district/', views.GetDistrict, name='GetDistrict'),
    path('get_subdistrict/', views.GetSubdistrict, name='GetSubdistrict'),
]