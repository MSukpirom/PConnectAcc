# Generated by Django 4.2.6 on 2023-11-10 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Taskscontroller', '0005_registertype_short_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='passwordclient',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Taskscontroller.client'),
        ),
    ]