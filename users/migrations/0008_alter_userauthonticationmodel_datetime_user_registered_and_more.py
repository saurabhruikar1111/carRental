# Generated by Django 4.2.4 on 2023-08-21 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_userauthonticationmodel_datetime_user_registered_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userauthonticationmodel',
            name='datetime_user_registered',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 4, 29, 52, 132308)),
        ),
        migrations.AlterField(
            model_name='userauthonticationmodel',
            name='datetime_user_updated',
            field=models.DateTimeField(default=datetime.datetime(2023, 8, 22, 4, 29, 52, 132308)),
        ),
    ]
