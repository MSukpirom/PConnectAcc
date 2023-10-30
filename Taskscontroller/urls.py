from django.urls import path
from . import views

app_name = 'Taskscontroller'

urlpatterns = [
    path('test/', views.checkdata, name='test'),
    path('index/', views.checkdata, name='Index'),
    # path('cilent/', views.RegisterForm, name='RegisterForm'),
    path('get_district/', views.GetDistrict, name='GetDistrict'),
    path('get_subdistrict/', views.GetSubdistrict, name='GetSubdistrict'),
    # path('egagement/',views.RegisterEgagement,name='RegisterEgagement'),
    # path('tasks/',views.TasksControl,name='TasksControl'),

    # NEW
    path('page/',views.Dashboard,name='Dashboard'),
    path('forms/',views.Forms,name='Forms'),
    path('cards/',views.Cards,name='Cards'),
    path('charts/',views.Charts,name='Charts'),
    path('buttons/',views.Buttons,name='Buttons'),
    path('modals/',views.Modals,name='Modals'),
    path('tables/',views.Tables,name='Tables'),
    path('page404/',views.Page404,name='Page404'),
    path('blank/',views.Blank,name='Blank'),
    path('create_account/',views.Create_Account,name='Create_Account'),
    path('forgot_pass/',views.Forgot_Pass,name='Forgot_Pass'),
    path('login/',views.Login,name='Login'),
]