from django.urls import path
from . import views

app_name = 'Taskscontroller'

urlpatterns = [
    path('test2/', views.test, name='test'),
    path('checkdata/', views.checkdata, name='checkdata'),
    path('forms_client/', views.forms_client, name='forms_client'),
    path('list_client/' ,views.list_client, name='list_client'),
    path('list_client/<int:id>/' ,views.list_client, name='list_client'),
    path('get_districts/', views.get_districts, name='GetDistrict'),
    path('get_subdistricts/', views.get_subdistricts, name='GetSubdistrict'),
]