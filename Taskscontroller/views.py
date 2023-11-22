from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from Taskscontroller.models import *
from datetime import date, datetime
from django.contrib import messages

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
    register_types = RegisterType.objects.all()

    return render(request, 'client/create.html',{
    # return render(request, 'testall.html',{
        'subdistrict': subdistrict,
        'district': district,
        'province': province,
        'register_types': register_types,
    })
    # return JsonResponse(list(subdistrict),safe=False)

# def forms_client(request):
    # if request.method == 'POST':
    #     # Extract data from the POST request
    #     c_code = request.POST.get('c_code')
    #     c_company_name = request.POST.get('c_company_name')
    #     c_tax_id = request.POST.get('c_tax_id')
    #     c_service_fee = request.POST.get('c_service_fee')
    #     c_channal = request.POST.get('c_channal')
    #     c_detail = request.POST.get('c_detail')
    #     c_status = request.POST.get('c_status')

    #     ct_name = request.POST.get('ct_name')
    #     ct_position = request.POST.get('ct_position')
    #     ct_phone = request.POST.get('ct_phone')
    #     ct_email = request.POST.get('ct_email')
    #     ct_line = request.POST.get('ct_line')
    #     ct_other = request.POST.get('ct_other')
    #     ct_address = request.POST.get('ct_address')
    #     ct_province = request.POST.get('ct_province')
    #     ct_district = request.POST.get('ct_district')
    #     ct_subdistrict = request.POST.get('ct_subdistrict')

    #     r_vat = request.POST.get('r_vat')
    #     r_vat_date = request.POST.get('r_vat_date')
    #     r_sbt = request.POST.get('r_sbt')
    #     r_sbt_date = request.POST.get('r_sbt_date')
    #     r_sso = request.POST.get('r_sso')
    #     r_sso_date = request.POST.get('r_sso_date')
    #     r_dbd_e_filling = request.POST.get('r_dbd_e_filling')
    #     r_dbd_e_filling_date = request.POST.get('r_dbd_e_filling_date')

    #     # Process date fields
    #     dateformat = "%Y-%m-%d"
    #     def parse_date(date_str):
    #         try:
    #             return datetime.strptime(date_str, dateformat)
    #         except ValueError:
    #             return None

    #     date_vat = parse_date(r_vat_date)
    #     date_sbt = parse_date(r_sbt_date)
    #     date_sso = parse_date(r_sso_date)
    #     date_dbd_e_filling = parse_date(r_dbd_e_filling_date)

    #     address = request.POST.get('address')
    #     province = request.POST.get('province')
    #     district = request.POST.get('district')
    #     subdistrict = request.POST.get('subdistrict')

    #     address0 = Address(
    #         address = address,
    #         province = Province.objects.filter(id=province).first(),
    #         district = District.objects.filter(id=district).first(),
    #         subdistrict = Subdistrict.objects.filter(id=subdistrict).first(),
    #         )
    #     address0.save()

    #     # Create and save the Contact instance
    #     contact = Contact(
    #         name=ct_name,
    #         position=ct_position,
    #         phone=ct_phone,
    #         email=ct_email,
    #         line=ct_line,
    #         other=ct_other,
    #         address=ct_address,
    #         province=Province.objects.filter(id=ct_province).first(),
    #         district=District.objects.filter(id=ct_district).first(),
    #         subdistrict=Subdistrict.objects.filter(id=ct_subdistrict).first(),
    #         same_address_company = address0
    #     )
    #     # ติดเรื่อง same_address_company ต้องให้บันทึกอย่างใดอย่างหนึ่ง
    #     contact.save()

    #     # Create and save the RegisterTax instance
    #     register_tax = RegisterTax(
    #         vat=r_vat,
    #         vat_date=date_vat,
    #         sbt=r_sbt,
    #         sbt_date=date_sbt,
    #         sso=r_sso,
    #         sso_date=date_sso,
    #         dbd_e_filling=r_dbd_e_filling,
    #         dbd_e_filling_date=date_dbd_e_filling,
    #     )
    #     register_tax.save()

    #     # Create and save the Client instance
    #     client = Client(
    #         code=c_code,
    #         company_name=c_company_name,
    #         tax_id=c_tax_id,
    #         service_fee=c_service_fee,
    #         create_client_date=datetime.today(),
    #         c_address=address0,
    #         channal=c_channal,
    #         detail=c_detail,
    #         status=c_status,
    #         contact=contact,
    #         register_tax=register_tax,
    #     )
    #     client.save()

    #     # type_password_id = request.POST.get('type_password')
    #     # username = request.POST.get('username')
    #     # password = request.POST.get('password')

    # username = request.POST.get('username')
    # password = request.POST.get('password')
    # type_password_id = request.POST.get('type_password')
    # client_id = request.POST.get('client')

    # try:
    #     type_password = RegisterType.objects.get(id=type_password_id)
    #     client = Client.objects.get(id=client_id)

    #     password_client = PasswordClient(username=username, password=password, type_password=type_password, client=client)
    #     password_client.save()

    #     # Move this line inside the try block
    #     return redirect('Taskscontroller:checkdata')

    # except (RegisterType.DoesNotExist, Client.DoesNotExist):
    #     return render(request, 'error404.html')

def create_client(request):
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
    return render(request, 'client/create.html')
    
def list_client(request):
    clients = Client.objects.all()
    return render(request, 'client/list_client.html', {'clients': clients})

def update_client(request, pk):
    client = get_object_or_404(Client, id=pk)

    if request.method == 'POST':
        # Extract data from the POST request
        edit_c_code = request.POST.get('c_code')
        edit_c_company_name = request.POST.get('c_company_name')
        edit_c_tax_id = request.POST.get('c_tax_id')
        edit_c_service_fee = request.POST.get('c_service_fee')
        edit_c_channal = request.POST.get('c_channal')
        edit_c_detail = request.POST.get('c_detail')
        edit_c_status = request.POST.get('c_status')

        # Update the Client instance
        client.code = edit_c_code
        client.company_name = edit_c_company_name
        client.tax_id = edit_c_tax_id
        client.service_fee = edit_c_service_fee
        client.channal = edit_c_channal
        client.detail = edit_c_detail
        client.status = edit_c_status
        client.save()
        return redirect("Taskscontroller:list_client")

    return render(request, 'client/update.html', {'client': client})

def delete_client(request, pk):
    client = get_object_or_404(Client, id=pk)
    client.delete()
    return redirect("Taskscontroller:list_client")

# def password_clients(request):
#     password_clients = PasswordClient.objects.all()
#     register_types = RegisterType.objects.all()
#     clients = Client.objects.all()
#     return render(request, 'password_manager/password_clients.html', {'password_clients': password_clients, 'register_types': register_types, 'clients': clients})

# def add_password_client(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        type_password_id = request.POST.get('type_password')
        client_id = request.POST.get('client')

        try:
            type_password = RegisterType.objects.get(id=type_password_id)
            client = Client.objects.get(id=client_id)

            password_client = PasswordClient(username=username, password=password, type_password=type_password, client=client)
            password_client.save()

            return redirect('Taskscontroller:password_clients')
        except (RegisterType.DoesNotExist, Client.DoesNotExist):
            return render(request, 'error404.html')

    register_types = RegisterType.objects.all()
    clients = Client.objects.all()
    return render(request, 'password_manager/add_password_client.html', {'register_types': register_types, 'clients': clients})

# def list_client(request):
#     clients = Client.objects.values('id', 'code', 'company_name', 'tax_id', 'contact__name', 'register_tax', 'status')
#     return render(request, 'client/list_client.html', {'clients': clients})
#     # return JsonResponse(list(client),safe=False)

def get_districts(request):
    province_id = request.GET.get('province_id')
    district = District.objects.filter(province=province_id).all().values('id','name_th')
    return JsonResponse(list(district),safe=False)

def get_subdistricts(request):
    district_id = request.GET.get('district_id')
    subdistrict = Subdistrict.objects.filter(district=district_id).all().values('id', 'name_th', 'zipcode')
    return JsonResponse(list(subdistrict),safe=False)

# def create_egagement(request):
#     if request.method == 'POST':
#         e_client = request.POST.get('e_client')
#         e_job_code = request.POST.get('e_job_code')
#         sdate_service = request.POST.get('sdate_service')
#         edate_service = request.POST.get('edate_service')
#         sdate_period = request.POST.get('sdate_period')
#         edate_period = request.POST.get('edate_period')
#         admin = request.POST.get('admin')
#         approver = request.POST.get('approver')
#         reviewer = request.POST.get('reviewer')
#         document_type = request.POST.get('document_type')

#         e = Egagement(
#             client = ,
#             job_code = ,
#             start_date_service = ,
#             end_date_service = ,
#             start_date_period = ,
#             end_date_period = ,
#             administrator = ,
#             approver = ,
#             reviewer = ,
#             document_type = ,
#         )
#         return

# def list_egagement(request):
#     return

# def update_egagement(request, pk):
#     return

# def delete_egagement(request, pk):
#     return

def type_job_list(request):
    clients = Client.objects.all()
    return render(request, 'client/client_list.html', {'clients': clients})

def create_type_job(request):
    if request.method == 'POST':
        c_name_th = request.POST.get('c_name_th')
        c_name_en = request.POST.get('c_name_en')

        t_name_th = request.POST.get('t_name_th')
        t_name_en = request.POST.get('t_name_en')

        acc_category = AccountCategory(
            name_th = c_name_th,
            name_en = c_name_en
        )
        acc_category.save()

        doc_type = DocumentType(
            name_th = t_name_th,
            name_en = t_name_en,
            account_category = acc_category
        )
        doc_type.save()
    return render(request, 'setting/create_type_job.html')

def list_type_job(request):
    document_types = DocumentType.objects.all()
    return render(request, 'setting/list_type_job.html', {'document_types': document_types})

def update_type_job(request, pk):
    doc_type = get_object_or_404(DocumentType, id=pk)

    if request.method == 'POST':
        c_name_th=request.POST.get('c_name_th'),
        c_name_en=request.POST.get('c_name_en')
        acc_category = AccountCategory(
            name_th = c_name_th,
            name_en = c_name_en
        )
        acc_category.save()

        doc_type.name_th = request.POST.get('t_name_th')
        doc_type.name_en = request.POST.get('t_name_en')
        doc_type.account_category = acc_category
        doc_type.save()

        return redirect('Taskscontroller:create_type_job')

    return render(request, 'setting/update_type_job.html', {'doc_type': doc_type})

# def delete_egagement(request, pk):
#     return