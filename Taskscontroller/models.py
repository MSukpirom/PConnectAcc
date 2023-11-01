from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    line = models.CharField(max_length=255, blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.ForeignKey('Client', on_delete=models.CASCADE, blank=True, null=True, related_name='company_address')

    class Meta:
        db_table = 'contact'

class Client(models.Model):
    code = models.CharField(max_length=255, blank=True, null=True)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    tin_id = models.CharField(max_length=13, blank=True, null=True)
    create_data = models.DateField(blank=True, null=True)
    service_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    channal = models.CharField(max_length=255, blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    register_vat = models.ForeignKey('RegisterClient', on_delete=models.CASCADE, blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'client'

class Country(models.Model):
    name_th = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'country'

class Geography(models.Model):
    name_th = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'geography'

class Province(models.Model):
    name_th = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'province'

class District(models.Model):
    name_th = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'district'

class Subdistrict(models.Model):
    name_th = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    postcode = models.IntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'subdistrict'

class RegisterClient(models.Model):
    regis_vat = models.BooleanField(default=False, null=True)
    date_vat = models.DateField(blank=True, null=True)
    regis_sbt = models.BooleanField(default=False, null=True)
    date_sbt = models.DateField(blank=True, null=True)
    regis_sso = models.BooleanField(default=False, null=True)
    date_sso = models.DateField(blank=True, null=True)
    regis_e_filling = models.BooleanField(default=False, null=True)
    date_e_filling = models.DateField(blank=True, null=True)
    regis_other = models.BooleanField(default=False, null=True)
    date_other = models.DateField(blank=True, null=True)
    password_client = models.ForeignKey('PasswordClient', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'register_client'

class PasswordClient(models.Model):
    regis_type = models.ForeignKey('TypeRegister', on_delete=models.CASCADE, blank=True, null=True)
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'password_client'

class TypeRegister(models.Model):
    name_th = models.CharField(max_length=255, blank=True, null=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'type_register'

# class User(models.Model):
#     username = models.CharField(max_length=30, unique=True)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=128)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     date_joined = models.DateTimeField(auto_now_add=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.username