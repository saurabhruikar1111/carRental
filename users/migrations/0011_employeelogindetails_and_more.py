# Generated by Django 4.2.4 on 2023-08-22 16:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_userauthonticationmodel_datetime_user_registered_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeLoginDetails',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('special_token', models.CharField(max_length=150, null=True)),
                ('datetime_employee_registered', models.DateTimeField(default=datetime.datetime(2023, 8, 22, 22, 18, 44, 162698))),
            ],
        ),
        migrations.RenameField(
            model_name='userauthonticationmodel',
            old_name='password',
            new_name='_password',
        ),
        migrations.AlterField(
            model_name='userauthonticationmodel',
            name='datetime_user_registered',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 22, 18, 44, 162698)),
        ),
        migrations.AlterField(
            model_name='userauthonticationmodel',
            name='datetime_user_updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 22, 18, 44, 162698)),
        ),
    ]
