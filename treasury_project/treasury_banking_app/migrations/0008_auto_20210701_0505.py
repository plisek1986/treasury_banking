# Generated by Django 3.0.6 on 2021-07-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasury_banking_app', '0007_auto_20210630_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('CREATE_PAYMENT', 'Create Payment'), ('DELETE_PAYMENT', 'Delete Payment'), ('APPROVE_PAYMENT', 'Approve Payment')], max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='permission',
        ),
        migrations.AddField(
            model_name='user',
            name='permission',
            field=models.ManyToManyField(to='treasury_banking_app.Permission'),
        ),
    ]