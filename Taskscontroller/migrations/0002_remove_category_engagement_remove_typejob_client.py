# Generated by Django 4.2.6 on 2023-12-13 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Taskscontroller', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='engagement',
        ),
        migrations.RemoveField(
            model_name='typejob',
            name='client',
        ),
    ]