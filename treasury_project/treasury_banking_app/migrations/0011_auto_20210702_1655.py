# Generated by Django 3.0.6 on 2021-07-02 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasury_banking_app', '0010_auto_20210702_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='access_type',
            field=models.CharField(choices=[(1, 'Create Payment'), (2, 'Delete Payment'), (3, 'Approve Payment')], max_length=64),
        ),
    ]
