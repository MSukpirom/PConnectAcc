# Generated by Django 4.2.6 on 2023-11-21 16:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Taskscontroller', '0008_remove_client_password_passwordclient_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_th', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('name_en', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            options={
                'db_table': 'account_category',
            },
        ),
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(blank=True, null=True)),
                ('username', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('password', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('confirm_password', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('nick_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('position', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('image', models.TextField(blank=True, null=True)),
                ('permission', models.CharField(blank=True, default=None, max_length=255, null=True)),
            ],
            options={
                'db_table': 'base_user',
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_th', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('name_en', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('account_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Taskscontroller.accountcategory')),
            ],
            options={
                'db_table': 'document_type',
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='create_client_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Egagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_code', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('start_date_service', models.DateTimeField(blank=True, null=True)),
                ('end_date_service', models.DateTimeField(blank=True, null=True)),
                ('start_date_period', models.DateTimeField(blank=True, null=True)),
                ('end_date_period', models.DateTimeField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('update_date', models.DateTimeField(blank=True, null=True)),
                ('delete_date', models.DateTimeField(blank=True, null=True)),
                ('administrator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='admin', to='Taskscontroller.baseuser')),
                ('approver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='approver', to='Taskscontroller.baseuser')),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Taskscontroller.client')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='create_by', to='Taskscontroller.baseuser')),
                ('delete_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='delete_by', to='Taskscontroller.baseuser')),
                ('document_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Taskscontroller.documenttype')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='reviewer', to='Taskscontroller.baseuser')),
                ('update_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='update_by', to='Taskscontroller.baseuser')),
            ],
            options={
                'db_table': 'egagement',
            },
        ),
        migrations.CreateModel(
            name='DocumentTypeDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('deadline', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('notification', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('review_date', models.DateTimeField(blank=True, null=True)),
                ('approved_date', models.DateTimeField(blank=True, null=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='approved_by', to='Taskscontroller.baseuser')),
                ('document_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Taskscontroller.documenttype')),
                ('review_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='review_by', to='Taskscontroller.baseuser')),
            ],
            options={
                'db_table': 'document_type_detail',
            },
        ),
    ]