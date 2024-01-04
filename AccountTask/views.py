from django.shortcuts import render, redirect, get_object_or_404
from AccountTask.models import *
from datetime import datetime
from django.contrib import messages
from django.db import transaction
import logging
from django.db.models import Count, F
from django.utils.dateparse import parse_date
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect, csrf_exempt

@csrf_protect
def custom_login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                messages.success(request, 'เข้าสู่ระบบเรียบร้อยแล้วค่ะ')
                return redirect('AccountTask:dashboard')
            else:
                messages.error(request, 'ชื่อผู้ใช้งานหรือรหัสผ่านไม่ถูกต้อง!')

    return render(request, 'login.html')

@login_required
def custom_logout(request):
    logout(request)
    return redirect("AccountTask:login")

def testpage(request):
    category = Category.objects.all()
    engagement_doc = EngagementDoc.objects.all()
    return render(request, 'testpage.html',{'category':category,'engagement_doc':engagement_doc})

def test(request):
    subdistrict = Subdistrict.objects.values('id', 'name_th', 'zipcode')
    district = District.objects.values('id', 'name_th')
    province = Province.objects.values('id', 'name_th').order_by('name_th')
    return render(request, 'test2.html', {
        'subdistrict': subdistrict,
        'district': district,
        'province': province
    })

def parse_date(date_string):
    if not date_string:
        return None
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        print(f"Error parsing date string: {date_string}")
        return None

def get_districts(request):
    province_id = request.GET.get('province_id')
    district = District.objects.filter(province=province_id).all().values('id','name_th')
    return JsonResponse(list(district),safe=False)

def get_subdistricts(request):
    district_id = request.GET.get('district_id')
    subdistrict = Subdistrict.objects.filter(district=district_id).all().values('id', 'name_th', 'zipcode')
    return JsonResponse(list(subdistrict),safe=False)

def get_clients(request):
    client_id = request.GET.get('client_id')
    clients = Client.objects.filter(id=client_id).values('id', 'code', 'company_name')
    return JsonResponse(list(clients), safe=False)

def get_category(request):
    category_id = request.GET.get('category_id')
    categorys = Category.objects.filter(id=category_id).values('id', 'name_th', 'name_en')
    return JsonResponse(list(categorys), safe=False)

# # engagement
# def create_engagement(request):
#     if request.method == 'POST':
#         client_id = request.POST.get('client')
#         e_job_code = request.POST.get('e_job_code')
#         e_sdate_service = request.POST.get('e_sdate_service')
#         e_edate_service = request.POST.get('e_edate_service')
#         e_sdate_period = request.POST.get('e_sdate_period')
#         e_edate_period = request.POST.get('e_edate_period')
#         document_type_id = request.POST.get('document_type_id')

#         date_format = "%Y-%m-%d"
#         def parse_date(date_str):
#             try:
#                 return datetime.strptime(date_str, date_format).date()
#             except ValueError:
#                 return None

#         sdate_service = parse_date(e_sdate_service)
#         edate_service = parse_date(e_edate_service)
#         sdate_period = parse_date(e_sdate_period)
#         edate_period = parse_date(e_edate_period)

#         try:
#             client_id = int(client_id)
#         except (ValueError, TypeError):
#             return render(request, 'engagement/create.html', {'error_message': 'Invalid Client ID'})

#         client_obj = Client.objects.filter(id=client_id).first()
#         if not client_obj:
#             return render(request, 'engagement/create.html', {'error_message': 'Client not found'})

#         document_type_obj = TypeJob.objects.filter(id=document_type_id).first()
#         if not document_type_obj:
#             return render(request, 'engagement/create.html', {'error_message': 'Document Type not found'})

#         engagement = Engagement(
#             client=client_obj,
#             job_code=e_job_code,
#             start_date_service=sdate_service,
#             end_date_service=edate_service,
#             start_date_period=sdate_period,
#             end_date_period=edate_period,
#             document_type=document_type_obj,
#         )
#         engagement.save()

#         return redirect('AccountTask:list_engagement')

#     return render(request, 'engagement/create.html', {'clients': Client.objects.all(), 'document_types': TypeJob.objects.all()})

# def list_engagement(request):
#     engagements = Engagement.objects.all().values('id', 'job_code', 'client__code', 'client__company_name', 'client__tax_id', 'client__status', 'document_type__account_category__name_th')
#     document_type_detail = TypeJobDetail.objects.all().values('id', 'type')
#     return render(request, 'engagement/list.html', {'engagements': engagements, 'document_type_details' : document_type_detail})

# def update_engagement(request, pk):
#     engagement = get_object_or_404(Engagement, id=pk)

#     if request.method == 'POST':
#         client_id = request.POST.get('client_id')
#         edit_job_code = request.POST.get('edit_job_code')
#         edit_sdate_service = request.POST.get('edit_sdate_service')
#         edit_edate_service = request.POST.get('edit_edate_service')
#         edit_sdate_period = request.POST.get('edit_sdate_period')
#         edit_edate_period = request.POST.get('edit_edate_period')
#         edit_administrator_id = request.POST.get('edit_administrator_id')
#         edit_approver_id = request.POST.get('edit_approver_id')
#         edit_reviewer_id = request.POST.get('edit_reviewer_id')
#         document_type_id = request.POST.get('document_type_id')

#         dateformat = "%Y-%m-%d"
#         def parse_date(date_str):
#             try:
#                 return datetime.strptime(date_str, dateformat)
#             except ValueError:
#                 return None

#         sdate_service = parse_date(edit_sdate_service)
#         edate_service = parse_date(edit_edate_service)
#         sdate_period = parse_date(edit_sdate_period)
#         edate_period = parse_date(edit_edate_period)

#         engagement.job_code = edit_job_code
#         engagement.start_date_service = sdate_service
#         engagement.end_date_service = edate_service
#         engagement.start_date_period = sdate_period
#         engagement.end_date_period = edate_period
#         engagement.save()

#     return render(request, 'engagement/update.html', {'engagement': engagement})

# def delete_engagement(request, pk):
#     type_job = Engagement.objects.get(pk=pk)
#     type_job.delete()
#     return redirect("AccountTask:list_engagement")

def dashboard(request):
    return render(request,'dashboard.html')

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_create(request):
    register_tax = None

    subdistrict = Subdistrict.objects.values('id', 'name_th', 'zipcode')
    district = District.objects.values('id', 'name_th')
    province = Province.objects.values('id', 'name_th').order_by('name_th')
    register_types = RegisterType.objects.values('id','short_name','name_th','name_en')
    category = Category.objects.values('id', 'name_th', 'name_en')
    engagement_doc = EngagementDoc.objects.all()
    engagement_doc_detail = EngagementDocDetail.objects.all()

    if request.method == 'POST':
        c_code = request.POST.get('c_code', '')
        c_company_name = request.POST.get('c_company_name', '')
        c_tax_id = request.POST.get('c_tax_id', '')
        c_service_fee = request.POST.get('c_service_fee')
        c_address = request.POST.get('c_address')
        c_address2 = request.POST.get('c_address2')
        c_province = request.POST.get('c_province')
        c_district = request.POST.get('c_district')
        c_subdistrict = request.POST.get('c_subdistrict')
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
        ct_address2 = request.POST.get('ct_address2')
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

        date_vat = parse_date(r_vat_date)
        date_sbt = parse_date(r_sbt_date)
        date_sso = parse_date(r_sso_date)
        date_dbd_e_filling = parse_date(r_dbd_e_filling_date)

        company_address = AddressBase(
            address = c_address,
            address2 = c_address2,
            province=Province.objects.filter(id=c_province).first(),
            district=District.objects.filter(id=c_district).first(),
            subdistrict=Subdistrict.objects.filter(id=c_subdistrict).first(),
        )
        company_address.save()

        client = Client(
            code=c_code,
            company_name=c_company_name,
            tax_id=c_tax_id,
            service_fee=c_service_fee,
            create_client_date=datetime.now(),
            channal=c_channal,
            detail=c_detail,
            status=c_status,
            register_tax=register_tax,
            company_address = company_address
        )
        client.save()

        contact_address = AddressBase(
            address=ct_address,
            address2=ct_address2,
            province=Province.objects.filter(id=ct_province).first(),
            district=District.objects.filter(id=ct_district).first(),
            subdistrict=Subdistrict.objects.filter(id=ct_subdistrict).first(),
        )
        contact_address.save()

        contact = Contact(
            client=client,
            name=ct_name,
            position=ct_position,
            phone=ct_phone,
            email=ct_email,
            line=ct_line,
            other=ct_other,
            address=contact_address
        )
        contact.save()

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

        contact.client = client
        contact.save()

        client.contact = contact
        client.register_tax = register_tax
        client.save()

        return redirect("AccountTask:client_detail", client_id=client.id)
    return render(request, 'clients/create.html', {
        'subdistrict': subdistrict,
        'district': district,
        'province': province,
        'register_types': register_types,
        'category': category,
        'engagement_doc': engagement_doc,
        'engagement_doc_detail': engagement_doc_detail,
    })

def client_update(request, pk):
    subdistrict = Subdistrict.objects.values('id', 'name_th', 'zipcode')
    district = District.objects.values('id', 'name_th')
    province = Province.objects.values('id', 'name_th').order_by('name_th')
    register_types = RegisterType.objects.values('id','short_name','name_th','name_en')
    category = Category.objects.values('id', 'name_th', 'name_en')
    engagement_doc = EngagementDoc.objects.all()
    engagement_doc_detail = EngagementDocDetail.objects.all()

    client = get_object_or_404(Client, id=pk)

    if request.method == 'POST':
        edit_c_code = request.POST.get('c_code')
        edit_c_company_name = request.POST.get('c_company_name')
        edit_c_tax_id = request.POST.get('c_tax_id')
        edit_c_service_fee = request.POST.get('c_service_fee')
        edit_c_address = request.POST.get('c_address')
        edit_c_address2 = request.POST.get('c_address2')
        edit_c_province = request.POST.get('c_province')
        edit_c_district = request.POST.get('c_district')
        edit_c_subdistrict = request.POST.get('c_subdistrict')
        edit_c_channal = request.POST.get('c_channal')
        edit_c_detail = request.POST.get('c_detail')
        edit_c_status = request.POST.get('c_status')

        edit_ct_name = request.POST.get('ct_name')
        edit_ct_position = request.POST.get('ct_position')
        edit_ct_phone = request.POST.get('ct_phone')
        edit_ct_email = request.POST.get('ct_email')
        edit_ct_line = request.POST.get('ct_line')
        edit_ct_other = request.POST.get('ct_other')
        edit_ct_address = request.POST.get('ct_address')
        edit_ct_address2 = request.POST.get('ct_address2')
        edit_ct_province = request.POST.get('ct_province')
        edit_ct_district = request.POST.get('ct_district')
        edit_ct_subdistrict = request.POST.get('ct_subdistrict')

        edit_r_vat = request.POST.get('r_vat')
        edit_r_vat_date = request.POST.get('r_vat_date')
        edit_r_sbt = request.POST.get('r_sbt')
        edit_r_sbt_date = request.POST.get('r_sbt_date')
        edit_r_sso = request.POST.get('r_sso')
        edit_r_sso_date = request.POST.get('r_sso_date')
        edit_r_dbd_e_filling = request.POST.get('r_dbd_e_filling')
        edit_r_dbd_e_filling_date = request.POST.get('r_dbd_e_filling_date')

        date_vat = parse_date(edit_r_vat_date)
        date_sbt = parse_date(edit_r_sbt_date)
        date_sso = parse_date(edit_r_sso_date)
        date_dbd_e_filling = parse_date(edit_r_dbd_e_filling_date)

        client.code = edit_c_code
        client.company_name = edit_c_company_name
        client.tax_id = edit_c_tax_id
        client.service_fee = edit_c_service_fee
        client.create_client_date = datetime.now()
        client.address = edit_c_address
        client.address2 = edit_c_address2
        client.province = Province.objects.get(id=edit_c_province)
        client.district = District.objects.get(id=edit_c_district)
        client.subdistrict = Subdistrict.objects.get(id=edit_c_subdistrict)
        client.channal = edit_c_channal
        client.detail = edit_c_detail

        # Update contact fields
        client.contact.name = edit_ct_name
        client.contact.position = edit_ct_position
        client.contact.phone = edit_ct_phone
        client.contact.email = edit_ct_email
        client.contact.line = edit_ct_line
        client.contact.other = edit_ct_other
        client.contact.address = edit_ct_address
        client.contact.address2 = edit_ct_address2
        client.contact.province = Province.objects.filter(id=edit_ct_province).first()
        client.contact.district = District.objects.filter(id=edit_ct_district).first()
        client.contact.subdistrict = Subdistrict.objects.filter(id=edit_ct_subdistrict).first()
        client.contact.save()

        # Update register_tax fields
        client.register_tax.vat = edit_r_vat
        client.register_tax.vat_date = date_vat
        client.register_tax.sbt = edit_r_sbt
        client.register_tax.sbt_date = date_sbt
        client.register_tax.sso = edit_r_sso
        client.register_tax.sso_date = date_sso
        client.register_tax.dbd_e_filling = edit_r_dbd_e_filling
        client.register_tax.dbd_e_filling_date = date_dbd_e_filling
        client.register_tax.save()

        client.save()

        return redirect("AccountTask:client_list")

    return render(request, 'clients/update.html', {
        'client':client,
        'subdistrict': subdistrict,
        'district': district,
        'province': province,
        'register_types': register_types,
        'category': category,
        'engagement_doc': engagement_doc,
        'engagement_doc_detail': engagement_doc_detail,
    })

def delete_client(request, pk):
    client = get_object_or_404(Client, id=pk)
    client.delete()
    return redirect("AccountTask:client_list")

def update_password(request):
    pw_id = request.POST.get('update_id')
    updated_pw = get_object_or_404(ClientPassword, id=pw_id)
    updated_pw.type_password = get_object_or_404(RegisterType, id=request.POST.get('update_type_password_id'))
    updated_pw.username = request.POST.get('update_username')
    updated_pw.password = request.POST.get('update_password')
    updated_pw.save()

def delete_password(request):
    pw_id = request.POST.get('delete_id')
    pw_to_delete = get_object_or_404(ClientPassword, id=pw_id)
    pw_to_delete.delete()

def engagement_list(request):
    engagement = Engagement.objects.all()
    engagement_doc_detail = EngagementDocDetail.objects.all()
    return render(request,'engagement/list.html',{'engagement':engagement})

def engagement_create(request):
    client = Client.objects.values('id', 'code', 'company_name')
    category = Category.objects.values('id', 'name_th')
    engagement_doc = EngagementDoc.objects.all()

    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        job_code = request.POST.get('job_code')
        start_date_service = request.POST.get('start_date_service')
        end_date_service = request.POST.get('end_date_service')
        start_date_period = request.POST.get('start_date_period')
        end_date_period = request.POST.get('end_date_period')
        category_id = request.POST.get('category_id')
        status = request.POST.get('status')

        sdate_service = parse_date(start_date_service)
        edate_service = parse_date(end_date_service)
        sdate_period = parse_date(start_date_period)
        edate_period = parse_date(end_date_period)

        engagement_doc_ids = request.POST.getlist('engagement_doc_id')
        category_instance = get_object_or_404(Category, id=category_id)

        if Engagement.objects.filter(job_code=job_code).exists():
            messages.error(request, f'Job Code "{job_code}" รหัส Job นี้มีอยู่แล้ว')

        else:
            with transaction.atomic():
                # สร้าง Engagement
                engagement = Engagement(
                    client=get_object_or_404(Client, id=client_id),
                    job_code=job_code,
                    start_date_service=sdate_service,
                    end_date_service=edate_service,
                    start_date_period=sdate_period,
                    end_date_period=edate_period,
                    category=category_instance,
                    status = status
                )
                engagement.save()

                # สร้าง TypeJobDetail สำหรับแต่ละ engagement_doc
                for engagement_doc_id in engagement_doc_ids:
                    engagement_doc = get_object_or_404(EngagementDoc, id=engagement_doc_id)
                    type_detail = request.POST.get('type_detail')
                    deadline = request.POST.get('deadline')
                    notification = request.POST.get('notification')
                    start_date = request.POST.get('start_date')
                    end_date = request.POST.get('end_date')

                    t_deadline = parse_date(deadline)
                    t_start_date = parse_date(start_date)
                    t_end_date = parse_date(end_date)

                    engagement_doc_detail = EngagementDocDetail(
                        type=type_detail,
                        deadline=t_deadline,
                        notification=notification,
                        start_date=t_start_date,
                        end_date=t_end_date,
                        engagement_doc=engagement_doc,
                    )
                    engagement_doc_detail.save()

                messages.success(request, 'Engagement successfully created.')

            return redirect('AccountTask:engagement_list')
    return render(request, 'engagement/create.html', {'client': client, 'category': category, 'engagement_doc': engagement_doc})

def task_list(request):
    return render(request,'task_list.html')

def setting(request):
    return render(request,'setting.html')

def client_detail(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    return render(request, 'client_detail.html', {'client': client})

def password_list(request,client_id):
    client = get_object_or_404(Client, id=client_id)
    passwords = ClientPassword.objects.all()
    return render(request, 'test/password_list.html', {'passwords': passwords,'client':client})

# รหัสผ่าน
def create_password(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    register_types = RegisterType.objects.all()
    passwords = ClientPassword.objects.filter(client=client)

    if request.method == 'POST':
        type_password_id = request.POST.get('type_password')
        username = request.POST.get('username')
        password_value = request.POST.get('password')

        password = ClientPassword(
            type_password=RegisterType.objects.filter(id=type_password_id).first(),
            username=username,
            password=password_value,
            client=client
        )
        password.save()

        return redirect('AccountTask:password_list', client_id=client.id)

    return render(request, 'test/password_list.html', {'register_types': register_types, 'client': client, 'passwords': passwords})

def update_password(request, password_id):
    register_types = RegisterType.objects.all()
    password_instance = get_object_or_404(ClientPassword, id=password_id)

    if request.method == 'POST':
        type_password_id = request.POST.get('type_password_id')
        username = request.POST.get('username')
        new_password = request.POST.get('password')

        password_instance.type_password = RegisterType.objects.filter(id=type_password_id).first()
        password_instance.username = username
        password_instance.password = new_password
        password_instance.save()

        return redirect('AccountTask:password_list', client_id=password_instance.client.id)

    return render(request, 'test/password_list.html', {'register_types': register_types, 'password': password_instance})

def delete_password(request, password_id):
    password_instance = get_object_or_404(ClientPassword, id=password_id)

    if request.method == 'POST':
        password_instance.delete()
        return redirect('AccountTask:password_list', client_id=password_instance.client.id)

    return render(request, 'test/password_list.html', {'password': password_instance})