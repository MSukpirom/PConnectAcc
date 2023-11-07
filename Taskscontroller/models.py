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
    service_fee =  models.CharField(max_length=255, default=None, null=True, blank=True)
    create_client_date = models.DateTimeField(auto_now_add=True)
    address = models.CharField(max_length=255, default=None, null=True, blank=True)
    province = models.ForeignKey('Province', on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey('District', on_delete=models.CASCADE, blank=True, null=True)
    subdistrict = models.ForeignKey('Subdistrict', on_delete=models.CASCADE, blank=True, null=True)
    channal =  models.CharField(max_length=255, default=None, null=True, blank=True)
    detail =  models.CharField(max_length=255, default=None, null=True, blank=True)
    contact = models.ForeignKey('Contact',on_delete=models.CASCADE, blank=True, null=True)
    status = models.BooleanField(default=False, null=True)
    register_tax = models.ForeignKey('RegisterTax',on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'client'

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
    vat = models.BooleanField(null=True, blank=True, default=None)
    vat_date = models.DateField(blank=True, null=True)
    sbt = models.BooleanField(null=True, blank=True, default=None)
    sbt_date = models.DateField(blank=True, null=True)
    sso = models.BooleanField(null=True, blank=True, default=None)
    sso_date = models.DateField(blank=True, null=True)
    dbd_e_filling = models.BooleanField(null=True, blank=True, default=None)
    dbd_e_filling_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'register_tax'

class RegisterType(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'register_type'

class Contact(models.Model):
    name =  models.CharField(max_length=255, default=None, null=True, blank=True)
    position =  models.CharField(max_length=255, default=None, null=True, blank=True)
    phone =  models.CharField(max_length=255, default=None, null=True, blank=True)
    email =  models.CharField(max_length=255, default=None, null=True, blank=True)
    line =  models.CharField(max_length=255, default=None, null=True, blank=True)
    other =  models.CharField(max_length=255, default=None, null=True, blank=True)
    address0 = models.CharField(max_length=255, default=None, null=True, blank=True)
    province = models.ForeignKey('Province', on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey('District', on_delete=models.CASCADE, blank=True, null=True)
    subdistrict = models.ForeignKey('Subdistrict', on_delete=models.CASCADE, blank=True, null=True)
    address_company = models.ForeignKey('Client', on_delete=models.CASCADE, blank=True, null=True, related_name='address_company')

    class Meta:
        db_table = 'contact'

class PasswordClient(models.Model):
    register_type = models.ForeignKey('RegisterType', on_delete=models.CASCADE, blank=True, null=True)
    username =  models.CharField(max_length=255, default=None, null=True, blank=True)
    password =  models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'password_client'

# class DocumentType(models.Model):
#     name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
#     name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)

#     class Meta:
#         db_table = 'document_type'

# class DocumentTypeDetail(models.Model):
#     document_type = models.ForeignKey('DocumentType', on_delete=models.CASCADE, blank=True, null=True)
#     type =  models.CharField(max_length=255, default=None, null=True, blank=True)
#     deadline = models.IntegerField(max_length=255, blank=True, null=True)
#     notification = models.IntegerField(max_length=255, blank=True, null=True)
#     start_date = models.DateField(blank=True, null=True)
#     end_date = models.DateField(blank=True, null=True)
#     review_by = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
#     review_date = models.DateTimeField(auto_now_add=True)
#     approved_by = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
#     approved_date = models.DateTimeField(auto_now_add=True)
#     create_by = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
#     create_date = models.DateTimeField(auto_now_add=True)
#     update_by = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
#     update_date = models.DateTimeField(auto_now_add=True)
#     delete_by = models.ForeignKey('User', on_delete=models.CASCADE, blank=True, null=True)
#     delete_date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         db_table = 'document_type_detail'

# class User(models.Model):
#     username =  models.CharField(max_length=255, default=None, null=True, blank=True)
#     password =  models.CharField(max_length=255, default=None, null=True, blank=True)
#     confirm_password = models.CharField(max_length=255, default=None, null=True, blank=True)
#     permission = models.CharField(max_length=255, default=None, null=True, blank=True)
#     fname =  models.CharField(max_length=255, default=None, null=True, blank=True)
#     lname =  models.CharField(max_length=255, default=None, null=True, blank=True)
#     position =  models.CharField(max_length=255, default=None, null=True, blank=True)
#     image = models.TextField()

#     class Meta:
#         db_table = 'user'