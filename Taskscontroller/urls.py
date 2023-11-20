from django.urls import path
from .views import *

app_name = 'Taskscontroller'

urlpatterns = [
    path('test2/', test, name='test'),
    path('checkdata/', checkdata, name='checkdata'),
    # path('forms_client/', forms_client, name='forms_client'),
    # path('list_client/' ,list_client, name='list_client'),
    # path('list_client/<int:id>/' ,list_client, name='list_client'),
    path('get_districts/', get_districts, name='GetDistrict'),
    path('get_subdistricts/', get_subdistricts, name='GetSubdistrict'),
    path('password_clients/', password_clients, name='password_clients'),
    path('add_password_client/', add_password_client, name='add_password_client'),
    path('create/',  create_client, name='create_client'),
    path('list/',  list_client, name='list_client'),
    path('update/<int:pk>/', update_client, name='update_client'),
    path('delete/<int:pk>/', delete_client, name='delete_client'),
]