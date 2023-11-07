from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from Taskscontroller.models import *
import datetime

def test(request):
    subdistrict = Subdistrict.objects.values('id', 'name_th', 'zipcode')
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

    return render(request, 'client/forms_client.html', {
        'subdistrict': subdistrict,
        'district': district,
        'province': province
    })
    # return JsonResponse(list(subdistrict),safe=False)

def forms_client(request):
    # Extract contact information
    ct_name = request.POST.get('ct_name')
    ct_position = request.POST.get('ct_position')
    ct_phone = request.POST.get('ct_phone')
    ct_email = request.POST.get('ct_email')
    ct_line = request.POST.get('ct_line')
    ct_other = request.POST.get('ct_other')
    ct_address0 = request.POST.get('ct_address0')
    ct_province = request.POST.get('ct_province')
    ct_district = request.POST.get('ct_district')
    ct_subdistrict = request.POST.get('ct_subdistrict')
    ct_address_company = request.POST.get('ct_address_company')

    # Logic to handle address comparison
    if ct_address0 == ct_address0:
        ct_address0 = request.POST.get('ct_address0')
        ct_province = request.POST.get('ct_province')
        ct_district = request.POST.get('ct_district')
        ct_subdistrict = request.POST.get('ct_subdistrict')
    elif ct_address_company == ct_address_company:
        ct_address_company = request.POST.get('ct_address_company')

    # Extract client information
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

    # Extract and process registration tax information
    r_vat = request.POST.get('r_vat') == 'on'
    r_vat_date = request.POST.get('r_vat_date')
    r_sbt = request.POST.get('r_sbt') == 'on'
    r_sbt_date = request.POST.get('r_sbt_date')
    r_sso = request.POST.get('r_sso') == 'on'
    r_sso_date = request.POST.get('r_sso_date')
    r_dbd_e_filling = request.POST.get('r_dbd_e_filling') == 'on'
    r_dbd_e_filling_date = request.POST.get('r_dbd_e_filling_date')

    # Create and save the Contact instance
    ct = Contact(
        name=ct_name, 
        position=ct_position, 
        phone=ct_phone, 
        email=ct_email, 
        line=ct_line, 
        other=ct_other, 
        address0=ct_address0, 
        province=Province.objects.filter(id=ct_province).first(),
        district=District.objects.filter(id=ct_district).first(),
        subdistrict=Subdistrict.objects.filter(id=ct_subdistrict).first(),
        address_company=Client.objects.filter(id=ct_address_company).first()
        )
    ct.save()

    # Create and save the RegisterTax instance
    r = RegisterTax(
        vat=r_vat, 
        vat_date=r_vat_date, 
        sbt=r_sbt, 
        sbt_date=r_sbt_date, 
        sso=r_sso, 
        sso_date=r_sso_date, 
        dbd_e_filling=r_dbd_e_filling, 
        dbd_e_filling_date=r_dbd_e_filling_date
        )
    r.save()

    # Create and save the Client instance
    c = Client(
        code=c_code, 
        company_name=c_company_name, 
        tax_id=c_tax_id, 
        create_client_date=datetime.datetime.now(),
        service_fee=c_service_fee, address=c_address,
        province=Province.objects.filter(id=c_province).first(),
        district=District.objects.filter(id=c_district).first(),
        subdistrict=Subdistrict.objects.filter(id=c_subdistrict).first(),
        channal=c_channal, 
        detail=c_detail, 
        status=c_status, 
        contact=ct, 
        register_tax=r
        )
    c.save()

    # return render(request,'client/forms_client.html')
    return redirect('Taskscontroller:list_client')

def list_client(request):
    client = Client.objects.all()
    return render(request,'client/list_client.html',{'client':client})
    # return JsonResponse(list(client),safe=False)

def get_districts(request):
    province_id = request.GET.get('province_id')
    district = District.objects.filter(province=province_id).all().values('id','name_th')
    return JsonResponse(list(district),safe=False)

def get_subdistricts(request):
    district_id = request.GET.get('district_id')
    subdistrict = Subdistrict.objects.filter(district=district_id).all().values('id', 'name_th', 'zipcode')
    return JsonResponse(list(subdistrict),safe=False)