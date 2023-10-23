from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Taskscontroller.models import Contact,Client,Province,District,Subdistrict,RegisterClient,PasswordClient,TypeRegister

# Create your views here.
def checkdata(request):
    subdistrict = Subdistrict.objects.all().values('id','name_th','postcode')
    district = District.objects.all().values('id','name_th')
    province = Province.objects.all().values('id','name_th')[:100]
    return render(request,'tasks/index.html',
    {'subdistrict':subdistrict,
    'district':district,
    'province':province
    })
# def RegisterForm(request):
#     id = request.POST.get('id')
#     c_code = request.POST.get('c_code','')
#     c_company_name = request.POST.get('c_company_name')
#         # c_tin_id = request.POST.get('c_tin_id')
#         # c_create_data = request.POST.get('c_create_data')
#         # c_service_fee = request.POST.get('c_service_fee')
#         # address = request.POST.get('address')
#         # province = request.POST.get('province', '')
#         # district = request.POST.get('district', '')
#         # subdistrict = request.POST.get('subdistrict', '')
#         # postcode = request.POST.get('postcode', '')
#         # c_channal = request.POST.get('c_channal')
#         # c_detail = request.POST.get('c_detail')
#         # c_regis_vat = request.POST.get('c_regis_vat','')
#         # c_date_vat = request.POST.get('c_date_vat','')
#         # c_regis_sbt = request.POST.get('c_regis_sbt','')
#         # c_date_sbt = request.POST.get('c_date_sbt','')
#         # c_regis_sso = request.POST.get('c_regis_sso','')
#         # c_date_sso = request.POST.get('c_date_sso','')
#         # c_regis_e_filling = request.POST.get('c_regis_e_filling','')
#         # c_date_e_filling = request.POST.get('c_date_e_filling','')
#         # c_regis_other = request.POST.get('c_regis_other','')
#         # c_rdate_other = request.POST.get('c_rdate_other','')
#         # contact_name = request.POST.get('contact_name','')
#         # contact_position = request.POST.get('contact_position','')
#         # contact_tel = request.POST.get('contact_tel','')
#         # contact_email = request.POST.get('contact_email','')
#         # contact_line = request.POST.get('contact_line','')
#         # contact_other = request.POST.get('contact_other','')
#         # contact_address1 = request.POST.get('contact_address1','')
#         # contact_address2 = request.POST.get('contact_address2','')

#     c = Client.objects.filter(id=id.replace(',','')).first()
#     c.code = c_code
#     c.company_name = c_company_name
#     # c.tin_id = c_tin_id
#     # c.create_data = c_create_data
#     # c.service_fee = c_service_fee
#     # c.channal = c_channal
#     # c.detail = c_detail
#     # c.save()
#     return render(request, 'tasks/test.html')

def RegisterForm(request):
    id = request.POST.get('id')

    if id is not None:
        id = id.replace(',', '')
        c_code = request.POST.get('c_code', '')
        c_company_name = request.POST.get('c_company_name', '')
        
        try:
            # Attempt to convert the sanitized 'id' to an integer
            id = int(id)
        except ValueError:
            # Handle the case where 'id' cannot be converted to an integer (e.g., invalid 'id')
            return render(request, 'tasks/test.html')

        c = Client.objects.filter(id=id).first()

        if c is not None:
            c.code = c_code
            c.company_name = c_company_name
            # Continue updating other attributes
        else:
            return render(request, 'tasks/test.html')
    else:
        # Handle the case where 'id' is None
        return render(request, 'tasks/test.html')
    
    








