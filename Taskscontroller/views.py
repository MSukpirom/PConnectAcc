from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Taskscontroller.models import Client,Province,District,Subdistrict
# Create your views here.
def checkdata(request):
    subdistrict = Subdistrict.objects.all().values('id','name_th','postcode')
    district = District.objects.all().values('id','name_th')
    province = Province.objects.all().values('id','name_th')[:100]

    return render(request,'tasks/test.html',
    {'subdistrict':subdistrict,
    'district':district,
    'province':province
    })

def RegisterForm(request):
    c_code = request.POST.get('c_code','')
    c_company_name = request.POST.get('c_company_name')
    c_tin_id = request.POST.get('c_tin_id')
    c_create_data = request.POST.get('c_create_data')
    c_service_fee = request.POST.get('c_service_fee')
    address = request.POST.get('address')
    province = request.POST.get('province')
    district = request.POST.get('district')
    subdistrict = request.POST.get('subdistrict')
    c_address = []
    if subdistrict and district and province :
        full_address = f"{address} {subdistrict[0].name_th} {district[0].name_th} {province[0].name_th}"
        c_address.append(full_address)
    c_channal = request.POST.get('c_channal')
    c_detail = request.POST.get('c_detail')

    c = Client()
    c.code = c_code
    c.company_name = c_company_name
    c.tin_id = c_tin_id
    c.create_data = c_create_data
    c.service_fee = c_service_fee
    c.address = c_address
    c.channal = c_channal
    c.detail = c_detail
    # c.save()

    return render(request, 'tasks/test.html')

def GetProvinces(request):
    provinces = Province.objects.all().values('id', 'name_th')[:100]
    return JsonResponse(list(provinces), safe=False)

def GetDistrict(request):
    province_id = request.GET.get('province_id')
    district = District.objects.filter(province_id=province_id).values('id', 'name_th')
    return JsonResponse(list(district), safe=False)

def GetSubdistrict(request):
    district_id = request.GET.get('districts_id')
    subdistrict = Subdistrict.objects.filter(district_id=district_id).values('id', 'name_th', 'postcode')
    return JsonResponse(list(subdistrict), safe=False)
