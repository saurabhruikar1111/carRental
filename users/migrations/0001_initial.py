# Generated by Django 4.2.4 on 2023-08-19 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAuthonticationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=80)),
                ('role', models.CharField(max_length=5)),
            ],
        ),
    ]
