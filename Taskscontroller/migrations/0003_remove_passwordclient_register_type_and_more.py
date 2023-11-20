# Generated by Django 4.2.6 on 2023-11-10 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Taskscontroller', '0002_alter_contact_same_address_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passwordclient',
            name='register_type',
        ),
        migrations.AddField(
            model_name='registertype',
            name='password',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Taskscontroller.passwordclient'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='same_address_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='same_address_company', to='Taskscontroller.address'),
        ),
    ]