# Generated by Django 3.0.6 on 2021-07-01 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasury_banking_app', '0008_auto_20210701_0505'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministratorViewForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='BankViewForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyViewForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
