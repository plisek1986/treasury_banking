# Generated by Django 3.2.4 on 2021-07-12 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasury_banking_app', '0027_auto_20210712_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='password_repeat',
            field=models.CharField(max_length=255),
        ),
    ]