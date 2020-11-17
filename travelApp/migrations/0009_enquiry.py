# Generated by Django 3.1.1 on 2020-09-28 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0008_auto_20200928_1145'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('contect', models.IntegerField()),
                ('country', models.CharField(max_length=255)),
                ('arrivalDate', models.DateField()),
                ('departureDate', models.DateField()),
                ('adult', models.IntegerField()),
                ('child', models.IntegerField()),
                ('accomodation', models.CharField(max_length=255)),
                ('remark', models.TextField(null=True)),
            ],
            options={
                'db_table': 'Enquiry',
            },
        ),
    ]