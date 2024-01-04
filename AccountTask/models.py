from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

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

class AddressBase(models.Model):
    address = models.CharField(max_length=255, default=None, null=True, blank=True)
    address2 = models.CharField(max_length=255, default=None, null=True, blank=True)
    province = models.ForeignKey('Province', on_delete=models.CASCADE, blank=True, null=True)
    district = models.ForeignKey('District', on_delete=models.CASCADE, blank=True, null=True)
    subdistrict = models.ForeignKey('Subdistrict', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'address_base'

class Client(models.Model):
    code = models.CharField(max_length=255, default=None, null=True, blank=True)
    company_name = models.CharField(max_length=255, default=None, null=True, blank=True)
    tax_id = models.CharField(max_length=255, default=None, null=True, blank=True)
    service_fee = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)
    create_client_date = models.DateTimeField(blank=True, null=True)
    channal = models.CharField(max_length=255, default=None, null=True, blank=True)
    detail = models.CharField(max_length=255, default=None, null=True, blank=True)
    contact = models.ForeignKey('Contact', on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('close', 'Close')])
    register_tax = models.ForeignKey('RegisterTax', on_delete=models.CASCADE, blank=True, null=True)
    company_address = models.ForeignKey(AddressBase, on_delete=models.CASCADE, blank=True, null=True, related_name='client_company_address')

    class Meta:
        db_table = 'client'

class Province(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE, blank=True, null=True, related_name='provinces')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True, related_name='provinces')

    class Meta:
        db_table = 'province'

class District(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE, blank=True, null=True, related_name='districts')

    class Meta:
        db_table = 'district'

class Subdistrict(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)
    zipcode = models.PositiveIntegerField()
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'subdistrict'

class RegisterTax(models.Model):
    vat = models.CharField(max_length=255, default=None, null=True, blank=True)
    vat_date = models.DateField(blank=True, null=True)
    sbt = models.CharField(max_length=255, default=None, null=True, blank=True)
    sbt_date = models.DateField(blank=True, null=True)
    sso = models.CharField(max_length=255, default=None, null=True, blank=True)
    sso_date = models.DateField(blank=True, null=True)
    dbd_e_filling = models.CharField(max_length=255, default=None, null=True, blank=True)
    dbd_e_filling_date = models.DateField(blank=True, null=True)

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
    name = models.CharField(max_length=255, default=None, null=True, blank=True)
    position = models.CharField(max_length=255, default=None, null=True, blank=True)
    phone = models.CharField(max_length=255, default=None, null=True, blank=True)
    email = models.EmailField(default=None, null=True, blank=True)
    line = models.CharField(max_length=255, default=None, null=True, blank=True)
    other = models.CharField(max_length=255, default=None, null=True, blank=True)
    address = models.ForeignKey(AddressBase, related_name='contact_address', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = 'contact'

class ClientPassword(models.Model):
    client = models.ForeignKey('Client', null=True, blank=True, on_delete=models.CASCADE)
    type_password = models.ForeignKey('RegisterType', null=True, blank=True, on_delete=models.CASCADE)
    username =  models.CharField(max_length=255, default=None, null=True, blank=True)
    password = models.TextField(default=None, null=True, blank=True)
    
    class Meta:
        db_table = 'client_password'

class Category(models.Model):
    name_th =  models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en =  models.CharField(max_length=255, default=None, null=True, blank=True)

    class Meta:
        db_table = 'category'

class EngagementDoc(models.Model):
    name_th = models.CharField(max_length=255, default=None, null=True, blank=True)
    name_en = models.CharField(max_length=255, default=None, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        db_table = 'engagement_doc'

class EngagementDocDetail(models.Model):
    engagement_doc = models.ForeignKey(EngagementDoc, on_delete=models.CASCADE)
    type = models.CharField(max_length=255, default=None, null=True, blank=True)
    deadline = models.DateField(blank=True, null=True)
    notification = models.CharField(max_length=255, default=None, null=True, blank=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    review_by = models.ForeignKey('BaseUser', models.DO_NOTHING, blank=True, null=True, related_name='review_by')
    review_date = models.DateField(blank=True, null=True)
    approved_by = models.ForeignKey('BaseUser', models.DO_NOTHING, blank=True, null=True, related_name='approved_by')
    approved_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'engagement_doc_detail'

class BaseUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username, password, **extra_fields)

class BaseUser(AbstractBaseUser, PermissionsMixin):
    active = models.BooleanField(default=True)
    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    image = models.ImageField(upload_to='user_images/', blank=True, null=True)
    permission = models.CharField(max_length=255)

    objects = BaseUserManager()
    USERNAME_FIELD = 'username'

    class Meta:
        db_table = 'base_user'

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

class Engagement(models.Model):
    clients = models.ManyToManyField('Client')
    job_code = models.CharField(max_length=255)
    start_date_service = models.DateTimeField()
    end_date_service = models.DateTimeField()
    start_date_period = models.DateTimeField()
    end_date_period = models.DateTimeField()
    administrator = models.ForeignKey(BaseUser, on_delete=models.DO_NOTHING, related_name='admin_engagements')
    approver = models.ForeignKey(BaseUser, on_delete=models.DO_NOTHING, related_name='approver_engagements')
    reviewer = models.ForeignKey(BaseUser, on_delete=models.DO_NOTHING, related_name='reviewer_engagements')
    categories = models.ManyToManyField('Category', related_name='engagements')
    status = models.CharField(max_length=50, choices=[('open', 'Open'), ('close', 'Close')])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'engagement'

class TaskType(models.Model):
    type_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'task_type'

class TaskControl(models.Model):
    task_name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=[('open_job', 'Open Job'), ('in_progress', 'In Progress'), ('review', 'Review'), ('pending', 'Pending'), ('completed', 'Completed')])
    assigned_to = models.ForeignKey('BaseUser', on_delete=models.CASCADE, related_name='assigned_tasks')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    task_type = models.ForeignKey('TaskType', on_delete=models.CASCADE)
    engagement = models.ForeignKey('Engagement', on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'task_control'