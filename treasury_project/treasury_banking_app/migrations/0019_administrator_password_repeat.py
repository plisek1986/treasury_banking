# Generated by Django 3.2.4 on 2021-07-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasury_banking_app', '0018_alter_administrator_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='administrator',
            name='password_repeat',
            field=models.CharField(default='p', max_length=64),
            preserve_default=False,
        ),
    ]
