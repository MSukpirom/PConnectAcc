from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Taskscontroller.models import *

def test(request):
    subdistrict = Subdistrict.objects.values('id', 'name_th', 'postcode')
    district = District.objects.values('id', 'name_th')
    province = Province.objects.values('id', 'name_th').order_by('name_th')
    return render(request, 'test2.html', {
        'subdistrict': subdistrict,
        'district': district,
        'province': province
    })

def checkdata(request):
    subdistrict = Subdistrict.objects.values('id', 'name_th', 'zipcode')
    district = District.objects.values('id', 'name_th')
    province = Province.objects.values('id', 'name_th').order_by('name_th')
    contact = Contact.objects.values('id', 'name')
    register_tax = RegisterTax.objects.all()

    return render(request, 'client/forms.html', {
        'subdistrict': subdistrict,
        'district': district,
        'province': province,
        'contact': contact,
        'register_tax': register_tax,
    })
    # return JsonResponse(list(subdistrict),safe=False)

def forms_client(request):
    contact_id = request.POST.get('contact_id')
    ct_name = request.POST.get('ct_name')
    ct_position = request.POST.get('ct_name')
    ct_phone = request.POST.get('ct_name')
    ct_email = request.POST.get('ct_name')
    ct_line = request.POST.get('ct_name')
    ct_other = request.POST.get('ct_name')
    ct_address0 = request.POST.get('ct_address0')
    ct_province = request.POST.get('ct_province')
    ct_district = request.POST.get('ct_district')
    ct_subdistrict = request.POST.get('ct_subdistrict')
    ct_address_company = request.POST.get('ct_address_company')
    if ct_address0 == ct_address0:
        ct_address0 = request.POST.get('ct_name')
        ct_province = request.POST.get('ct_name')
        ct_district = request.POST.get('ct_name')
        ct_subdistrict = request.POST.get('ct_name')
    elif ct_address0 == ct_address_company:
        ct_address_company = request.POST.get('ct_address_company')

    c_code = request.POST.get('c_code')
    c_company_name = request.POST.get('c_company_name')
    c_tax_id = request.POST.get('c_tax_id')
    c_create_client_date = request.POST.get('c_create_client_date')
    c_service_fee = request.POST.get('c_service_fee')
    c_address = request.POST.get('c_address')
    c_province = request.POST.get('c_province')
    c_district = request.POST.get('c_district')
    c_subdistrict = request.POST.get('c_subdistrict')
    c_channal = request.POST.get('c_channal')
    c_detail = request.POST.get('c_detail')
    c_status = request.POST.get('c_status')

    register_tax_id = request.POST.get('register_tax_id')
    r_vat = request.POST.get('r_vat')
    if r_vat == 'on':
        r_vat = True
    else:
        r_vat = False
    r_vat_date = request.POST.get('r_vat_date')
    r_sbt = request.POST.get('r_sbt')
    if r_sbt == 'on':
        r_sbt = True
    else:
        r_sbt = False
    r_sbt_date = request.POST.get('r_sbt_date') or None
    r_sso = request.POST.get('r_sso')
    if r_sso == 'on':
        r_sso = True
    else:
        r_sso = False
    r_sso_date = request.POST.get('r_sso_date') or None
    r_dbd_e_filling = request.POST.get('r_dbd_e_filling')
    if r_dbd_e_filling == 'on':
        r_dbd_e_filling = True
    else:
        r_dbd_e_filling = False
    r_dbd_e_filling_date = request.POST.get('r_dbd_e_filling_date') or None

    ct = Contact()
    ct.name = ct_name
    ct.position = ct_position
    ct.phone = ct_phone
    ct.email = ct_email
    ct.line = ct_line
    ct.other = ct_other
    ct.address0 = ct_address0
    ct.province = Province.objects.filter(id=ct_province).first()
    ct.district = District.objects.filter(id=ct_district).first()
    ct.subdistrict = Subdistrict.objects.filter(id=ct_subdistrict).first()
    ct.address_company = Client.objects.filter(id=ct_address_company).first()
    ct.save()

    r = RegisterTax()
    r.vat = r_vat
    r.vat_date = r_vat_date
    r.sbt = r_sbt
    r.sbt_date = r_sbt_date
    r.sso = r_sso
    r.sso_date = r_sso_date
    r.dbd_e_filling = r_dbd_e_filling
    r.dbd_e_filling_date = r_dbd_e_filling_date
    r.save()

    c = Client()
    c.code = c_code
    c.company_name = c_company_name
    c.tax_id = c_tax_id
    c.create_client_date = c_create_client_date
    c.service_fee = c_service_fee
    c.address = c_address
    c.province = Province.objects.filter(id=c_province).first()
    c.district = District.objects.filter(id=c_district).first()
    c.subdistrict = Subdistrict.objects.filter(id=c_subdistrict).first()
    c.channal = c_channal
    c.detail = c_detail
    c.contact = c_code
    c.register_tax = c_code
    c.status = c_status
    c.contact = Contact.objects.filter(id=contact_id).first()
    c.register_tax = RegisterTax.objects.filter(id=register_tax_id).first()
    c.save()

    return render(request, 'client/forms.html')

def GetDistrict(request):
    province_id = request.GET.get('province_id')
    district = District.objects.filter(province=province_id).all().values('id','name_th')
    return JsonResponse(list(district),safe=False)

def GetSubdistrict(request):
    district_id = request.GET.get('district_id')
    subdistrict = Subdistrict.objects.filter(district=district_id).all().values('id', 'name_th', 'zipcode')
    return JsonResponse(list(subdistrict),safe=False)