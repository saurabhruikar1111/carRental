# Generated by Django 4.2.4 on 2023-08-21 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_userauthonticationmodel_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='userauthonticationmodel',
            name='datetime_employee_registered',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='userauthonticationmodel',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='userauthonticationmodel',
            name='special_token',
            field=models.CharField(default=None, max_length=150),
        ),
    ]
