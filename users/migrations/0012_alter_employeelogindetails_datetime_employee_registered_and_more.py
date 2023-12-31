# Generated by Django 4.2.4 on 2023-08-22 16:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_employeelogindetails_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeelogindetails',
            name='datetime_employee_registered',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 22, 29, 9, 475659)),
        ),
        migrations.AlterField(
            model_name='userauthonticationmodel',
            name='datetime_user_registered',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 22, 29, 9, 475659)),
        ),
        migrations.AlterField(
            model_name='userauthonticationmodel',
            name='datetime_user_updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 22, 29, 9, 475659)),
        ),
        migrations.AlterField(
            model_name='userauthonticationmodel',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
