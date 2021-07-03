# Generated by Django 3.2.4 on 2021-07-03 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasury_banking_app', '0012_auto_20210702_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyCreateForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='AdministratorViewForm',
        ),
        migrations.DeleteModel(
            name='CompanyViewForm',
        ),
        migrations.AddField(
            model_name='user',
            name='can_delete_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_payment_approver',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_payment_creator',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='access',
            name='access_type',
            field=models.CharField(choices=[('CREATE_PAYMENT', 'Create Payment'), ('DELETE_PAYMENT', 'Delete Payment'), ('APPROVE_PAYMENT', 'Approve Payment')], max_length=64),
        ),
        migrations.AlterField(
            model_name='access',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bankviewform',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]