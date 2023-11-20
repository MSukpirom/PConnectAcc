# Generated by Django 4.2.6 on 2023-11-10 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Taskscontroller', '0003_remove_passwordclient_register_type_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registertype',
            name='password',
        ),
        migrations.AddField(
            model_name='passwordclient',
            name='type_password',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Taskscontroller.registertype'),
        ),
    ]