from django.urls import path
from .views import *

app_name = 'AccountTask'

urlpatterns = [
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),

    path('testpage/', testpage, name='testpage'),
    path('test2/', test, name='test'),

    path('get_districts/', get_districts, name='GetDistrict'),
    path('get_subdistricts/', get_subdistricts, name='GetSubdistrict'),
    path('get_clients/', get_clients, name='GetClient'),



    path('dashboard/', dashboard, name='dashboard'),

    path('client_list/', client_list, name='client_list'),
    path('client_create/', client_create, name='client_create'),
    path('client/update/<int:pk>/', client_update, name='client_update'),
    path('client/delete/<int:pk>/', delete_client, name='delete_client'),

    path('client/<int:client_id>/', client_detail, name='client_detail'),

    path('passwords/<int:client_id>/', password_list, name='password_list'),
    path('create_password/<int:client_id>/', create_password, name='create_password'),
    path('update_password/<int:password_id>/', update_password, name='update_password'),
    path('delete_password/<int:password_id>/', delete_password, name='delete_password'),


    path('engagement_list/', engagement_list, name='engagement_list'),
    path('engagement_create/', engagement_create, name='engagement_create'),

    path('task_list/', task_list, name='task_list'),

    path('setting/', setting, name='setting'),
]