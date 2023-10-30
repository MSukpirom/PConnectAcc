from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Taskscontroller.models import Client,Province,District,Subdistrict, Contact

def checkdata(request):
    subdistrict = Subdistrict.objects.values('id', 'name_th', 'postcode')
    district = District.objects.values('id', 'name_th')
    province = Province.objects.values('id', 'name_th').order_by('name_th')
    return render(request, 'tasks/forms.html', {
    # return render(request, 'test.html', {
        'subdistrict': subdistrict,
        'district': district,
        'province': province
    })

    # return JsonResponse(list(province), safe=False)

# NEW
def Dashboard(request):
    return render(request, 'tasks/index.html')

def Forms(request):
    c_code = request.POST.get('c_code')
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
        full_address = f"{address} {subdistrict[0].name_th} {subdistrict[0].postcode} {district[0].name_th} {province[0].name_th}"
        c_address.append(full_address)
    c_channal = request.POST.get('c_channal')
    c_detail = request.POST.get('c_detail')

    ct_name = request.POST.get('ct_name')
    ct_position = request.POST.get('ct_position')
    ct_tel = request.POST.get('ct_tel')
    ct_email = request.POST.get('ct_email')
    ct_line = request.POST.get('ct_line')
    ct_other = request.POST.get('ct_other')
    address1 = request.POST.get('address1')
    ct_province = request.POST.get('ct_province')
    ct_district = request.POST.get('ct_district')
    ct_subdistrict = request.POST.get('ct_subdistrict')
    ct_address1 = []
    if ct_subdistrict and ct_district and ct_province :
        full_address = f"{address1} {ct_subdistrict[0].name_th} {ct_subdistrict[0].postcode} {ct_district[0].name_th} {ct_province[0].name_th}"
        ct_address1.append(full_address)
    ct_address2 = request.POST.get('ct_address2')

    c = Client()
    c.code = c_code
    c.company_name = c_company_name
    c.tin_id = c_tin_id
    c.create_data = c_create_data
    c.service_fee = c_service_fee
    c.address = c_address
    c.channal = c_channal
    c.detail = c_detail
    # c.register_vat = 
    c.contact = Contact.objects.filter(id=ct_name).first()
    # c.save()

    ct = Contact
    ct.name = ct_name
    ct.position = ct_position
    ct.tel = ct_tel
    ct.email = ct_email
    ct.line = ct_line
    ct.other = ct_other
    ct.address1 = ct_address1
    ct.address2 = ct_address2
    # ct.save()

    return render(request, 'tasks/forms.html')

def Cards(request):
    return render(request, 'tasks/cards.html')

def Charts(request):
    return render(request, 'tasks/charts.html')

def Buttons(request):
    return render(request, 'tasks/buttons.html')

def Modals(request):
    return render(request, 'tasks/modals.html')

def Tables(request):
    return render(request, 'tasks/tables.html')

def Page404(request):
    return render(request, 'pages/404.html')

def Blank(request):
    return render(request, 'pages/blank.html')

def Create_Account(request):
    return render(request, 'pages/create-account.html')

def Forgot_Pass(request):
    return render(request, 'pages/forgot-password.html')

def Login(request):
    return render(request, 'pages/login.html')

def GetDistrict(request):
    province_id = request.GET.get('province_id')
    district = District.objects.filter(province=province_id).all().values('id','name_th')
    return JsonResponse(list(district),safe=False)

def GetSubdistrict(request):
    district_id = request.GET.get('district_id')
    subdistrict = Subdistrict.objects.filter(district=district_id).all().values('id', 'name_th', 'postcode')
    return JsonResponse(list(subdistrict),safe=False)