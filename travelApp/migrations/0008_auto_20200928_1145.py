# Generated by Django 3.1.1 on 2020-09-28 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0007_allpackages_region'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newoffers',
            old_name='time',
            new_name='package_name',
        ),
        migrations.RemoveField(
            model_name='newoffers',
            name='image',
        ),
        migrations.RemoveField(
            model_name='newoffers',
            name='title',
        ),
    ]
