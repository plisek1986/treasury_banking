# Generated by Django 3.0.6 on 2021-07-11 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasury_banking_app', '0020_auto_20210711_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='swift_code',
            field=models.CharField(max_length=11),
        ),
    ]