from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    email = models.CharField(unique=True)
    line = models.CharField(max_length=255)
    other = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    company_address = models.ForeignKey('Client', on_delete=models.CASCADE)

class Client(models.Model):
    code = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    tax_id = models.CharField(max_length=13)
    create_data = models.DateField()
    service_fee = models.DecimalField(max_digits=6, decimal_places=2)
    address = models.CharField(max_length=255)
    province = models.ForeignKey()
    district = models.ForeignKey()
    subdistrict = models.ForeignKey()
    postcode = models.ForeignKey()
    channal = models.CharField(max_length=255)
    detail = models.TextField()
    regis_vat = models.ForeignKey()
    regis_sbt = models.ForeignKey()
    regis_sso = models.ForeignKey()
    regis_e_filling = models.ForeignKey()
    regis_other = models.ForeignKey()
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

class Country(models.Model):
    name_th = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

class Geography(models.Model):
    name_th = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)

class Province(models.Model):
    name_th = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class District(models.Model):
    name_th = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

class Subdistrict(models.Model):
    name_th = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    postcode = models.IntegerField(max_length=5)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

class Register(models.Model):
    client = models.ForeignKey('Client', on_delete=models.CASCADE)
    regis_vat = models.BooleanField(default=False)
    date_vat = models.DateField()
    regis_sbt = models.BooleanField(default=False)
    date_sbt = models.DateField()
    regis_sso = models.BooleanField(default=False)
    date_sso = models.DateField()
    regis_e_filling = models.BooleanField(default=False)
    date_e_filling = models.DateField()
    regis_other = models.BooleanField(default=False)
    date_other = models.DateField()

class PasswordClient(models.Model):
    regis_type = models.OneToOneField('Register', on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=128)

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