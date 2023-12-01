from django.urls import path
from .views import *

app_name = 'Taskscontroller'

urlpatterns = [
    path('test2/', test, name='test'),
    path('demo/', demo, name='demo'),
    path('get_districts/', get_districts, name='GetDistrict'),
    path('get_subdistricts/', get_subdistricts, name='GetSubdistrict'),
    path('get_clients/', get_clients, name='GetClient'),
    # path('password_clients/', password_clients, name='password_clients'),
    # path('add_password_client/', add_password_client, name='add_password_client'),
    # path('client/create/', create_client, name='create_client'),
    # path('client/list/', list_client, name='list_client'),
    
    path('client/delete/<int:pk>/', delete_client, name='delete_client'),
    # path('type_job/create/', create_type_job, name='create_type_job'),
    # path('type_job/list/', list_type_job, name='list_type_job'),
    # path('type_job/update/<int:pk>/', update_type_job, name='update_type_job'),
    # path('type_job/delete/<int:pk>/', delete_type_job, name='delete_type_job'),
    # path('engagement/create/', create_engagement, name='create_engagement'),
    # path('engagement/list/', list_engagement, name='list_engagement'),
    # path('engagement/update/<int:pk>/', update_engagement, name='update_engagement'),
    # path('engagement/delete/<int:pk>/', delete_engagement, name='delete_engagement'),
    # path('document/detail/create/', create_document_detail, name='create_document_detail'),
    # path('document/detail/list/', list_document_detail, name='list_document_detail'),
    # path('document/detail/update/<int:pk>/', update_document_detail, name='update_document_detail'),
    # path('document/detail/delete/<int:pk>/', delete_document_detail, name='delete_document_detail'),
    path('dashboard/', dashboard, name='dashboard'),
    path('client_list/', client_list, name='client_list'),
    path('client_create/', client_create, name='client_create'),
    path('client/update/<int:pk>/', client_update, name='client_update'),
    path('engagement_list/', engagement_list, name='engagement_list'),
    path('engagement_create/', engagement_create, name='engagement_create'),
    path('task_list/', task_list, name='task_list'),
    path('setting/', setting, name='setting'),
]