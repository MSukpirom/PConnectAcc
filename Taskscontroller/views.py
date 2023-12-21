from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from Taskscontroller.models import *
from datetime import datetime
from django.contrib import messages
from django.db import transaction
import logging
from django.db.models import Count, F
from django.utils.dateparse import parse_date
from django.urls import reverse

def testpage(request):
    category = Category.objects.all()
    engagement_status = EngagementStatus.objects.filter(id=1).first()
    return render(request, 'testpage.html',{'category':category,'engagement_status':engagement_status})

def test(request):
    subdistrict = Subdistrict.objects.values('id', 'name_th', 'zipcode')
    district = District.objects.values('id', 'name_th')
    province = Province.objects.values('id', 'name_th').order_by('name_th')
    return render(request, 'test2.html', {
        'subdistrict': subdistrict,
        'district': district,
        'province': province
    })
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

def parse_date(date_string):
    if not date_string:
        return None
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        print(f"Error parsing date string: {date_string}")
        return None

# def create_client(request):
#     if request.method == 'POST':
#         c_code = request.POST.get('c_code')
#         c_company_name = request.POST.get('c_company_name')
#         c_tax_id = request.POST.get('c_tax_id')
#         c_service_fee = request.POST.get('c_service_fee')
#         c_address = request.POST.get('c_address')
#         c_address2 = request.POST.get('c_address2')
#         c_province = request.POST.get('c_province')
#         c_district = request.POST.get('c_district')
#         c_subdistrict = request.POST.get('c_subdistrict')
#         c_channal = request.POST.get('c_channal')
#         c_detail = request.POST.get('c_detail')
#         c_status = request.POST.get('c_status')

#         ct_name = request.POST.get('ct_name')
#         ct_position = request.POST.get('ct_position')
#         ct_phone = request.POST.get('ct_phone')
#         ct_email = request.POST.get('ct_email')
#         ct_line = request.POST.get('ct_line')
#         ct_other = request.POST.get('ct_other')
#         ct_address = request.POST.get('ct_address')
#         ct_address2 = request.POST.get('ct_address2')
#         ct_province = request.POST.get('ct_province')
#         ct_district = request.POST.get('ct_district')
#         ct_subdistrict = request.POST.get('ct_subdistrict')

#         r_vat = request.POST.get('r_vat')
#         r_vat_date = request.POST.get('r_vat_date')
#         r_sbt = request.POST.get('r_sbt')
#         r_sbt_date = request.POST.get('r_sbt_date')
#         r_sso = request.POST.get('r_sso')
#         r_sso_date = request.POST.get('r_sso_date')
#         r_dbd_e_filling = request.POST.get('r_dbd_e_filling')
#         r_dbd_e_filling_date = request.POST.get('r_dbd_e_filling_date')

#         date_vat = parse_date(r_vat_date)
#         date_sbt = parse_date(r_sbt_date)
#         date_sso = parse_date(r_sso_date)
#         date_dbd_e_filling = parse_date(r_dbd_e_filling_date)

#         contact = Contact(
#             name=ct_name,
#             position=ct_position,
#             phone=ct_phone,
#             email=ct_email,
#             line=ct_line,
#             other=ct_other,
#             address=ct_address,
#             address2=ct_address2,
#             province=Province.objects.filter(id=ct_province).first(),
#             district=District.objects.filter(id=ct_district).first(),
#             subdistrict=Subdistrict.objects.filter(id=ct_subdistrict).first(),
#         )
#         contact.save()

#         register_tax = RegisterTax(
#             vat=r_vat,
#             vat_date=date_vat,
#             sbt=r_sbt,
#             sbt_date=date_sbt,
#             sso=r_sso,
#             sso_date=date_sso,
#             dbd_e_filling=r_dbd_e_filling,
#             dbd_e_filling_date=date_dbd_e_filling,
#         )
#         register_tax.save()

#         client = Client(
#             code = c_code,
#             company_name = c_company_name,
#             tax_id = c_tax_id,
#             service_fee = c_service_fee,
#             create_client_date = datetime.now(),
#             address = c_address,
#             address2 = c_address2,
#             province = c_province,
#             district = c_district,
#             subdistrict = c_subdistrict,
#             channal = c_channal,
#             detail = c_detail,
#             status = c_status,
#             contact = contact,
#             register_tax = register_tax,
#         )
#         client.save()

#         contact.client = client
#         contact.save()
#     return render(request, 'client/create.html')
    
# def list_client(request):
#     clients = Client.objects.all()
#     return render(request, 'client/list_client.html', {'clients': clients})

def update_client(request, pk):
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
        client.province = edit_c_province
        client.district = edit_c_district
        client.subdistrict = edit_c_subdistrict
        client.channal = edit_c_channal
        client.detail = edit_c_detail
        client.status = edit_c_status

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

        # Save the updated client
        client.save()

        return redirect("Taskscontroller:client_list")

    return render(request, 'clients/update.html', {'client': client})

def delete_client(request, pk):
    client = get_object_or_404(Client, id=pk)
    client.delete()
    return redirect("Taskscontroller:client_list")

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

def get_type_job(request):
    type_job_id = request.GET.get('type_job_id')
    type_job = TypeJob.objects.filter(id=type_job_id).all()
    return JsonResponse(list(type_job), safe=False)

def get_type_job_detail(request):
    type_job_detail_id = request.GET.get('type_job_detail_id')
    type_job_detail = TypeJobDetail.objects.filter(id=type_job_detail_id).all()
    return JsonResponse(list(type_job_detail), safe=False)

def get_registype(request):
    get_registype_id = request.GET.get('get_registype_id')
    get_registype = TypeJobDetail.objects.filter(id=get_registype_id).all()
    return JsonResponse(list(get_registype), safe=False)

# logger = logging.getLogger(__name__)
# def create_type_job(request):
#     if request.method == 'POST':
#         category_id = request.POST.get('category')
#         new_category_name = request.POST.get('new_acc_category')
#         t_name_th = request.POST.get('t_name_th')
#         t_name_en = request.POST.get('t_name_en')

#         if not category_id or (category_id == 'create_new' and not new_category_name):
#             error_message = 'Invalid form data. Please provide valid values.'
#             logger.warning(error_message)
#             return render(request, 'setting/create_type_job.html', {'error_message': error_message, 'category': Category.objects.all()})

#         try:
#             if category_id == 'create_new':
#                 category = Category(name_th=new_category_name, name_en=new_category_name)
#                 category.save()

#                 category_id = category.id

#             doc_type = TypeJob(name_th=t_name_th, name_en=t_name_en, category=category_id)
#             doc_type.save()

#             return redirect('success_page')

#         except Exception as e:
#             logger.error(f"An error occurred: {e}")
#             error_message = 'An error occurred. Please try again.'
#             return render(request, 'setting/create_type_job.html', {'error_message': error_message, 'category': Category.objects.all()})

#     return render(request, 'setting/create_type_job.html', {'category': Category.objects.all()})

# def list_type_job(request):
#     types_job = TypeJob.objects.all()
#     return render(request, 'setting/list_type_job.html', {'types_job': types_job})

# def update_type_job(request, pk):
#     type_job = get_object_or_404(TypeJob, id=pk)

#     if request.method == 'POST':
#         edit_category_name_th = request.POST.get('edit_category_name_th')
#         edit_category_name_en = request.POST.get('edit_category_name_en')

#         type_job.name_th = edit_category_name_th
#         type_job.name_en = edit_category_name_en
#         type_job.save()
#     return render(request, 'setting/update_type_job.html', {'type_job': type_job})

# def delete_type_job(request, pk):
#     type_job = TypeJob.objects.get(pk=pk)
#     type_job.delete()
#     return redirect("Taskscontroller:list_type_job")

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

#         return redirect('Taskscontroller:list_engagement')

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
#     return redirect("Taskscontroller:list_engagement")

# def create_document_detail(request):
#     if request.method == 'POST':
#         # Extract form data
#         document_type_id = request.POST.get('document_type_id')
#         c_type = request.POST.get('c_type')
#         c_deadline = request.POST.get('c_deadline')
#         c_notification = request.POST.get('c_notification')
#         c_start_date = request.POST.get('c_start_date')
#         c_end_date = request.POST.get('c_end_date')
#         # c_review_by = request.POST.get('c_review_by')
#         # c_approved_by = request.POST.get('c_approved_by')

#         # Date format and parsing function
#         date_format = "%Y-%m-%d"
#         def parse_date(date_str):
#             try:
#                 return datetime.strptime(date_str, date_format).date()
#             except ValueError:
#                 return None

#         # Parse date strings
#         start_date = parse_date(c_start_date)
#         end_date = parse_date(c_end_date)

#         # Check for valid dates
#         if start_date is None or end_date is None:
#             # Handle the error, maybe return an error response or render a specific template
#             return render(request, 'error_template.html', {'error_message': 'Invalid date format'})

#         # Create DocumentTypeDetail object and save
#         document_detail = TypeJobDetail(
#             document_type=TypeJob.objects.filter(id=document_type_id).first(),
#             type=c_type,
#             deadline=c_deadline,
#             notification=c_notification,
#             start_date=start_date,
#             end_date=end_date,
#             # review_by_id=BaseUser.objects.filter(id=c_review_by).first(),
#             # review_date=datetime.now(),
#             # approved_by_id=BaseUser.objects.filter(id=c_approved_by).first(),
#             # approved_date=datetime.now(),
#         )
#         document_detail.save()

#         # Redirect to a success page or another view
#         return redirect('Taskscontroller:list_document_detail')

#     # Render the form page for GET requests
#     return render(request, 'document/create_doc_detail.html')

# def list_document_detail(request):
#     # doc_detail = DocumentTypeDetail.objects.all().values('id', 'type', 'document_type__client__code', 'document_type__client__company_name', 'document_type__client__tax_id', 'document_type__client__status', 'document_type__account_category__name_th', 'document_type__engagement__job_code')
#     doc_detail = TypeJobDetail.objects.values('id', 'type', 'document_type__client__code', 'document_type__client__company_name','document_type__client__tax_id', 'document_type__client__status','document_type__account_category__name_th', 'document_type__engagement__job_code').annotate(client_code=F('document_type__client__code')).order_by('-client_code')
    
#     count_type_acc = TypeJobDetail.objects.filter(document_type__account_category__name_th='บัญชี').count()
#     count_type_tax = TypeJobDetail.objects.filter(document_type__account_category__name_th='ภาษี').count()
#     count_type_payroll = TypeJobDetail.objects.filter(document_type__account_category__name_th='เงินเดือน').count()
#     count_type_report = TypeJobDetail.objects.filter(document_type__account_category__name_th='รายงาน').count()
#     count_type_acc = TypeJobDetail.objects.filter(document_type__account_category__name_th='บัญชี').count()
    
#     return render(request, 'document/list_doc_detail.html', {
#         'doc_details': doc_detail,
#         'count_type_acc': count_type_acc,
#         'count_type_tax': count_type_tax,
#         'count_type_payroll': count_type_payroll,
#         'count_type_report': count_type_report,
#     })

# def update_document_detail(request):
#     return redirect('Taskscontroller:list_document_detail')

# def delete_document_detail(request):
#     return redirect('Taskscontroller:list_document_detail')

def demo(request):
    return render(request, 'DEMO.html')

def dashboard(request):
    return render(request,'dashboard.html')

def client_list(request):
    clients = Client.objects.all().distinct()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_create(request):
    subdistrict = Subdistrict.objects.values('id', 'name_th', 'zipcode')
    district = District.objects.values('id', 'name_th')
    province = Province.objects.values('id', 'name_th').order_by('name_th')
    register_types = RegisterType.objects.values('id','short_name','name_th','name_en')
    category = Category.objects.values('id', 'name_th', 'name_en')
    type_job = TypeJob.objects.all()
    type_job_detail = TypeJobDetail.objects.all()
    client_status = ClientStatus.objects.values('id','name')
    client_pws = ClientPassword.objects.all()

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
        c_register_tax = request.POST.get('c_register_tax')

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

        username = request.POST.get('username')
        password = request.POST.get('password')
        type_password_id = request.POST.get('type_password_id')

        client = Client(
            code=c_code,
            company_name=c_company_name,
            tax_id=c_tax_id,
            service_fee=c_service_fee,
            create_client_date=datetime.now(),
            address=c_address,
            address2=c_address2,
            province=Province.objects.filter(id=c_province).first(),
            district=District.objects.filter(id=c_district).first(),
            subdistrict=Subdistrict.objects.filter(id=c_subdistrict).first(),
            channal=c_channal,
            detail=c_detail,
            status=ClientStatus.objects.filter(id=c_status).first(),
        )
        client.save()

        contact = Contact(
            name=ct_name,
            position=ct_position,
            phone=ct_phone,
            email=ct_email,
            line=ct_line,
            other=ct_other,
            address=ct_address,
            address2=ct_address2,
            province=Province.objects.filter(id=ct_province).first(),
            district=District.objects.filter(id=ct_district).first(),
            subdistrict=Subdistrict.objects.filter(id=ct_subdistrict).first(),
            client=client,
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

        client_pws = ClientPassword(
            username = username,
            password = password,
            client = client,
            type_password = RegisterType.objects.filter(id=type_password_id).first(),
        )
        client_pws.save()

        contact.client = client
        contact.save()

        client.contact = contact
        client.register_tax = register_tax
        client.save()
    return render(request, 'clients/create.html', {
        'subdistrict': subdistrict,
        'district': district,
        'province': province,
        'register_types': register_types,
        'category': category,
        'type_job': type_job,
        'type_job_detail': type_job_detail,
        'client_status': client_status,
        'client_pws':client_pws
    })

def client_update(request, pk):
    subdistrict = Subdistrict.objects.values('id', 'name_th', 'zipcode')
    district = District.objects.values('id', 'name_th')
    province = Province.objects.values('id', 'name_th').order_by('name_th')
    register_types = RegisterType.objects.values('id','short_name','name_th','name_en')
    category = Category.objects.values('id', 'name_th', 'name_en')
    type_job = TypeJob.objects.all()
    type_job_detail = TypeJobDetail.objects.all()
    client_status = ClientStatus.objects.all()

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
        client.status = ClientStatus.objects.get(id=edit_c_status)

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

        return redirect("Taskscontroller:client_list")

    return render(request, 'clients/update.html', {
        'client':client,
        'subdistrict': subdistrict,
        'district': district,
        'province': province,
        'register_types': register_types,
        'category': category,
        'type_job': type_job,
        'type_job_detail': type_job_detail,
        'client_status': client_status,
    })

# def client_password(request, client_id):
#     client = get_object_or_404(Client, pk=client_id)
#     register_types = RegisterType.objects.values('id', 'short_name', 'name_th')
#     client_pws = ClientPassword.objects.filter(client=client)

#     if request.method == 'POST':
#         action = request.POST.get('action')

#         if action == 'create':
#             type_password_id = request.POST.get('type_password_id')
#             username = request.POST.get('username')
#             password = request.POST.get('password')

#             if type_password_id:
#                 type_password = get_object_or_404(RegisterType, id=type_password_id)

#                 new_client_pw = ClientPassword(
#                     type_password=type_password,
#                     username=username,
#                     password=password,
#                     client=client
#                 )
#                 new_client_pw.save()

#         elif action == 'update':
#             pw_id = request.POST.get('update_id')
#             updated_pw = get_object_or_404(ClientPassword, id=pw_id)
#             updated_pw.type_password = get_object_or_404(RegisterType, id=request.POST.get('update_type_password_id'))
#             updated_pw.username = request.POST.get('update_username')
#             updated_pw.password = request.POST.get('update_password')
#             updated_pw.save()

#         elif action == 'delete':
#             pw_id = request.POST.get('delete_id')
#             pw_to_delete = get_object_or_404(ClientPassword, id=pw_id)
#             pw_to_delete.delete()

#         return redirect("Taskscontroller:client_password", client_id=client_id)

#     context = {
#         'client': client,
#         'register_types': register_types,
#         'client_pws': client_pws,
#     }

#     return render(request, 'clients/create.html', context)

def engagement_list(request):
    engagement = Engagement.objects.all()
    type_job_detail = TypeJobDetail.objects.all()
    return render(request,'engagement/list.html',{'engagement':engagement})

def engagement_create(request):
    client = Client.objects.values('id', 'code', 'company_name')
    category = Category.objects.values('id', 'name_th')
    engagement_status = EngagementStatus.objects.filter(id=1).first()
    type_job = TypeJob.objects.all()

    if request.method == 'POST':
        client_id = request.POST.get('client_id')
        job_code = request.POST.get('job_code')
        start_date_service = request.POST.get('start_date_service')
        end_date_service = request.POST.get('end_date_service')
        start_date_period = request.POST.get('start_date_period')
        end_date_period = request.POST.get('end_date_period')
        category_id = request.POST.get('category_id')

        sdate_service = parse_date(start_date_service)
        edate_service = parse_date(end_date_service)
        sdate_period = parse_date(start_date_period)
        edate_period = parse_date(end_date_period)

        type_job_ids = request.POST.getlist('type_job_id')
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
                    status = engagement_status
                )
                engagement.save()

                # สร้าง TypeJobDetail สำหรับแต่ละ type_job
                for type_job_id in type_job_ids:
                    type_job = get_object_or_404(TypeJob, id=type_job_id)
                    type_detail = request.POST.get('type_detail')
                    deadline = request.POST.get('deadline')
                    notification = request.POST.get('notification')
                    start_date = request.POST.get('start_date')
                    end_date = request.POST.get('end_date')

                    t_deadline = parse_date(deadline)
                    t_start_date = parse_date(start_date)
                    t_end_date = parse_date(end_date)

                    type_job_detail = TypeJobDetail(
                        type=type_detail,
                        deadline=t_deadline,
                        notification=notification,
                        start_date=t_start_date,
                        end_date=t_end_date,
                        type_job=type_job,
                    )
                    type_job_detail.save()

                messages.success(request, 'Engagement successfully created.')

            return redirect('Taskscontroller:engagement_list')
    return render(request, 'engagement/create.html', {'client': client, 'category': category, 'engagement_status': engagement_status, 'type_job': type_job})

def task_list(request):
    return render(request,'task_list.html')

def setting(request):
    return render(request,'setting.html')