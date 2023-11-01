from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Taskscontroller.models import Client,Province,District,Subdistrict, Contact, RegisterClient

def checkdata(request):
    subdistrict = Subdistrict.objects.values('id', 'name_th', 'postcode')
    district = District.objects.values('id', 'name_th')
    province = Province.objects.values('id', 'name_th').order_by('name_th')
    return render(request, 'forms.html', {
        'subdistrict': subdistrict,
        'district': district,
        'province': province
    })

def test(request):
    subdistrict = Subdistrict.objects.values('id', 'name_th', 'postcode')
    district = District.objects.values('id', 'name_th')
    province = Province.objects.values('id', 'name_th').order_by('name_th')
    return render(request, 'test2.html', {
        'subdistrict': subdistrict,
        'district': district,
        'province': province
    })

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
    c_address = ""
    if address is not None:
        c_address += address
    if province is not None:
        c_address += ' ' + province
    if district is not None:
        c_address += ' ' + district
    if subdistrict is not None:
        c_address += ' ' + subdistrict
    c_channal = request.POST.get('c_channal')
    c_detail = request.POST.get('c_detail')
    contact_id = request.POST.get('contact_id')
    regisclient_id = request.POST.get('regisclient_id')

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
    ct_address1 = ""
    if address1 is not None:
        ct_address1 += address1
    if ct_subdistrict is not None:
        ct_address1 += ' ' + ct_subdistrict
    if ct_district is not None:
        ct_address1 += ' ' + ct_district
    if ct_province is not None:
        ct_address1 += ' ' + ct_province
    ct_address2 = request.POST.get('ct_address2')

    ct = Contact()
    ct.name = ct_name
    ct.position = ct_position
    ct.tel = ct_tel
    ct.email = ct_email
    ct.line = ct_line
    ct.other = ct_other
    ct.address1 = ct_address1
    ct.address2 = ct_address2
    ct.save()


    regis_vat = request.POST.get('regis_vat')
    if regis_vat == 'on':
        regis_vat = True
    else:
        regis_vat = False
    date_vat = request.POST.get('date_vat')
    regis_sbt = request.POST.get('regis_sbt')
    if regis_sbt == 'on':
        regis_sbt = True
    else:
        regis_sbt = False
    date_sbt = request.POST.get('date_sbt')
    regis_sso = request.POST.get('regis_sso')
    if regis_sso == 'on':
        regis_sso = True
    else:
        regis_sso = False
    date_sso = request.POST.get('date_sso')
    regis_e_filling = request.POST.get('regis_e_filling')
    if regis_e_filling == 'on':
        regis_e_filling = True
    else:
        regis_e_filling = False
    date_e_filling = request.POST.get('date_e_filling')
    regis_other = request.POST.get('regis_other')
    if regis_other == 'on':
        regis_other = True
    else:
        regis_other = False
    date_other = request.POST.get('date_other')

    r = RegisterClient()
    r.regis_vat = regis_vat
    r.date_vat = date_vat
    r.regis_sbt = regis_sbt
    r.date_sbt = date_sbt
    r.regis_sso = regis_sso
    r.date_sso = date_sso
    r.regis_e_filling = regis_e_filling
    r.date_e_filling = date_e_filling
    r.regis_other = regis_other
    r.date_other = date_other
    r.save()

    c = Client()
    c.code = c_code
    c.company_name = c_company_name
    c.tin_id = c_tin_id
    c.create_data = c_create_data
    c.service_fee = c_service_fee
    c.address = c_address
    c.channal = c_channal
    c.detail = c_detail
    c.register_vat = RegisterClient.objects.filter(id=regisclient_id).first()
    c.contact = Contact.objects.filter(id=contact_id).first()
    c.save()





    return render(request, 'test2.html')

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