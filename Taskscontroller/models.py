from django.db import models

# Create your models here.
class Country(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'country'

class Geography(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'geography'

class Client(models.Model):
    code =  models.CharField(max_length=255, default=None, null=True, blank=True)
    company_name =  models.CharField(max_length=255, default=None, null=True, blank=True)
    tax_id =  models.CharField(max_length=255, default=None, null=True, blank=True)
    service_fee =  models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    create_client_date =models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=255, default=None, null=True, blank=True)
    address2 = models.CharField(max_length=255, default=None, null=True, blank=True)
    province = models.ForeignKey('Province', on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey('District', on_delete=models.CASCADE, blank=True, null=True)
    subdistrict = models.ForeignKey('Subdistrict', on_delete=models.CASCADE, blank=True, null=True)
    channal =  models.CharField(max_length=255, default=None, null=True, blank=True)
    detail =  models.CharField(max_length=255, default=None, null=True, blank=True)
    contact = models.ForeignKey('Contact',on_delete=models.CASCADE, blank=True, null=True)
    status = models.ForeignKey('ClientStatus',on_delete=models.CASCADE, blank=True, null=True)
    register_tax = models.ForeignKey('RegisterTax',on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'client'

class ClientStatus(models.Model):
    name = models.CharField(max_length=255, default=None)

    class Meta:
        db_table = 'client_status'

class Province(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'province'

class District(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'district'

class Subdistrict(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)
    zipcode = models.IntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'subdistrict'

class RegisterTax(models.Model):
    vat = models.CharField(max_length=255, default=None, null=True, blank=True)
    vat_date = models.DateTimeField(blank=True, null=True)
    sbt = models.CharField(max_length=255, default=None, null=True, blank=True)
    sbt_date = models.DateTimeField(blank=True, null=True)
    sso = models.CharField(max_length=255, default=None, null=True, blank=True)
    sso_date = models.DateTimeField(blank=True, null=True)
    dbd_e_filling = models.CharField(max_length=255, default=None, null=True, blank=True)
    dbd_e_filling_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'register_tax'

class RegisterType(models.Model):
    short_name = models.CharField(max_length=255, default=None, null=True, blank=True)
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'register_type'

class Contact(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name =  models.CharField(max_length=255, default=None, null=True, blank=True)
    position =  models.CharField(max_length=255, default=None, null=True, blank=True)
    phone =  models.CharField(max_length=255, default=None, null=True, blank=True)
    email =  models.CharField(max_length=255, default=None, null=True, blank=True)
    line =  models.CharField(max_length=255, default=None, null=True, blank=True)
    other =  models.CharField(max_length=255, default=None, null=True, blank=True)
    address = models.CharField(max_length=255, default=None, null=True, blank=True)
    address2 = models.CharField(max_length=255, default=None, null=True, blank=True)
    province = models.ForeignKey('Province', on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey('District', on_delete=models.CASCADE, blank=True, null=True)
    subdistrict = models.ForeignKey('Subdistrict', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'contact'

class ClientPassword(models.Model):
    client = models.ForeignKey('Client', null=True, blank=True, on_delete=models.CASCADE)
    type_password = models.ForeignKey('RegisterType', null=True, blank=True, on_delete=models.CASCADE)
    username =  models.CharField(max_length=255, default=None, null=True, blank=True)
    password =  models.CharField(max_length=255, default=None, null=True, blank=True)
    
    class Meta:
        db_table = 'client_password'

class Category(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'category'

class TypeJob(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'type_job'

class TypeJobDetail(models.Model):
    type_job = models.ForeignKey(TypeJob, on_delete=models.CASCADE, blank=True, null=True)
    type =  models.CharField(max_length=255, default=None, null=True, blank=True)
    deadline = models.DateTimeField(max_length=255, default=None, null=True, blank=True)
    notification = models.CharField(max_length=255, default=None, null=True, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    review_by = models.ForeignKey('BaseUser', models.DO_NOTHING, blank=True, null=True, related_name='review_by')
    review_date = models.DateTimeField(blank=True, null=True)
    approved_by = models.ForeignKey('BaseUser', models.DO_NOTHING, blank=True, null=True, related_name='approved_by')
    approved_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'type_job_detail'

class BaseUser(models.Model):
    active = models.BooleanField(blank=True, null=True)
    username =  models.CharField(max_length=255, default=None, null=True, blank=True)
    password =  models.CharField(max_length=255, default=None, null=True, blank=True)
    confirm_password = models.CharField(max_length=255, default=None, null=True, blank=True)
    first_name =  models.CharField(max_length=255, default=None, null=True, blank=True)
    last_name =  models.CharField(max_length=255, default=None, null=True, blank=True)
    position =  models.CharField(max_length=255, default=None, null=True, blank=True)
    image = models.TextField(blank=True, null=True)
    permission = models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'base_user'

class Engagement(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    job_code = models.CharField(max_length=255, default=None, null=True, blank=True)
    start_date_service = models.DateTimeField(blank=True, null=True)
    end_date_service = models.DateTimeField(blank=True, null=True)
    start_date_period = models.DateTimeField(blank=True, null=True)
    end_date_period = models.DateTimeField(blank=True, null=True)
    administrator = models.ForeignKey(BaseUser, models.DO_NOTHING, blank=True, null=True, related_name='admin')
    approver = models.ForeignKey(BaseUser, models.DO_NOTHING, blank=True, null=True, related_name='approver')
    reviewer =models.ForeignKey(BaseUser, models.DO_NOTHING, blank=True, null=True, related_name='reviewer')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.ForeignKey('EngagementStatus', null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        db_table = 'engagement'

class EngagementStatus(models.Model):
    status = models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'engagement_status'

class TaskType(models.Model):
    type_name = models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'task_type'

class Task(models.Model):
    engagement = models.ForeignKey(Engagement, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=255, default=None, null=True, blank=True)
    description = models.TextField()
    status = models.ForeignKey('TaskStatus', on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType, on_delete=models.CASCADE)
    type_job = models.ForeignKey(TypeJob, on_delete=models.CASCADE)

    class Meta:
        db_table = 'task'

class TaskStatus(models.Model):
    status = models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'task_status'