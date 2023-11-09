from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from Taskscontroller.models import *
from datetime import date, datetime

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

    return render(request, 'client/forms_client.html',{
        'subdistrict': subdistrict,
        'district': district,
        'province': province
    })
    # return JsonResponse(list(subdistrict),safe=False)

def forms_client(request):
    if request.method == 'POST':
        # Extract data from the POST request
        c_code = request.POST.get('c_code')
        c_company_name = request.POST.get('c_company_name')
        c_tax_id = request.POST.get('c_tax_id')
        c_service_fee = request.POST.get('c_service_fee')
        c_channal = request.POST.get('c_channal')
        c_detail = request.POST.get('c_detail')
        c_status = request.POST.get('c_status')

        ct_name = request.POST.get('ct_name')
        ct_position = request.POST.get('ct_position')
        ct_phone = request.POST.get('ct_phone')
        ct_email = request.POST.get('ct_email')
        ct_line = request.POST.get('ct_line')
        ct_other = request.POST.get('ct_other')
        ct_address = request.POST.get('ct_address')
        ct_province = request.POST.get('ct_province')
        ct_district = request.POST.get('ct_district')
        ct_subdistrict = request.POST.get('ct_subdistrict')

        r_vat = request.POST.get('r_vat')
        r_vat_date = request.POST.get('r_vat_date')
        r_sbt = request.POST.get('r_sbt')
        r_sbt_date = request.POST.get('r_sbt_date')
        r_sso = request.POST.get('r_sso')
        r_sso_date = request.POST.get('r_sso_date')
        r_dbd_e_filling = request.POST.get('r_dbd_e_filling')
        r_dbd_e_filling_date = request.POST.get('r_dbd_e_filling_date')

        # Process date fields
        dateformat = "%Y-%m-%d"
        def parse_date(date_str):
            try:
                return datetime.strptime(date_str, dateformat)
            except ValueError:
                return None

        date_vat = parse_date(r_vat_date)
        date_sbt = parse_date(r_sbt_date)
        date_sso = parse_date(r_sso_date)
        date_dbd_e_filling = parse_date(r_dbd_e_filling_date)

        address = request.POST.get('address')
        province = request.POST.get('province')
        district = request.POST.get('district')
        subdistrict = request.POST.get('subdistrict')

        address0 = Address(
            address = address,
            province = Province.objects.filter(id=province).first(),
            district = District.objects.filter(id=district).first(),
            subdistrict = Subdistrict.objects.filter(id=subdistrict).first(),
            )
        address0.save()

        # Create and save the Contact instance
        contact = Contact(
            name=ct_name,
            position=ct_position,
            phone=ct_phone,
            email=ct_email,
            line=ct_line,
            other=ct_other,
            address=ct_address,
            province=Province.objects.filter(id=ct_province).first(),
            district=District.objects.filter(id=ct_district).first(),
            subdistrict=Subdistrict.objects.filter(id=ct_subdistrict).first(),
            same_address_company = address0
        )
        # ติดเรื่อง same_address_company ต้องให้บันทึกอย่างใดอย่างหนึ่ง
        contact.save()

        # Create and save the RegisterTax instance
        register_tax = RegisterTax(
            vat=r_vat,
            vat_date=date_vat,
            sbt=r_sbt,
            sbt_date=date_sbt,
            sso=r_sso,
            sso_date=date_sso,
            dbd_e_filling=r_dbd_e_filling,
            dbd_e_filling_date=date_dbd_e_filling,
        )
        register_tax.save()

        # Create and save the Client instance
        client = Client(
            code=c_code,
            company_name=c_company_name,
            tax_id=c_tax_id,
            service_fee=c_service_fee,
            create_client_date=datetime.today(),
            c_address=address0,
            channal=c_channal,
            detail=c_detail,
            status=c_status,
            contact=contact,
            register_tax=register_tax,
        )
        client.save()
        
        return redirect('Taskscontroller:list_client')

def list_client(request):
    clients = Client.objects.values('id', 'code', 'company_name', 'tax_id', 'contact__name', 'register_tax', 'status')
    return render(request, 'client/list_client.html', {'clients': clients})
    # return JsonResponse(list(client),safe=False)

def get_districts(request):
    province_id = request.GET.get('province_id')
    district = District.objects.filter(province=province_id).all().values('id','name_th')
    return JsonResponse(list(district),safe=False)

def get_subdistricts(request):
    district_id = request.GET.get('district_id')
    subdistrict = Subdistrict.objects.filter(district=district_id).all().values('id', 'name_th', 'zipcode')
    return JsonResponse(list(subdistrict),safe=False)