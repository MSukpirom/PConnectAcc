# Generated by Django 4.2.6 on 2023-11-06 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Taskscontroller', '0003_remove_contact_address_contact_address1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='create_client_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='registertax',
            name='dbd_e_filling_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='registertax',
            name='sbt_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='registertax',
            name='sso_date',
            field=models.DateField(default=None),
        ),
        migrations.AlterField(
            model_name='registertax',
            name='vat_date',
            field=models.DateField(default=None),
        ),
    ]
