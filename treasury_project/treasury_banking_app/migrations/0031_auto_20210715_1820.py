# Generated by Django 3.0.6 on 2021-07-15 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treasury_banking_app', '0030_auto_20210713_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='access',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='administrator',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='company',
            name='country',
            field=models.CharField(choices=[('Austria', 'AT'), ('Belgium', 'BE'), ('Bulgaria', 'BG'), ('Switzerland', 'CH'), ('Czech Republic', 'CZ'), ('Germany', 'DE'), ('Denmark', 'DK'), ('Estonia', 'EE'), ('Spain', 'ES'), ('Finland', 'FI'), ('France', 'FR'), ('United Kingdom', 'GB'), ('Greece', 'GR'), ('Croatia', 'HR'), ('Hungary', 'HU'), ('Ireland', 'IE'), ('Iceland', 'IS'), ('Italy', 'IT'), ('Kazakhstan', 'KZ'), ('Lithuania', 'LT'), ('Latvia', 'LV'), ('Netherlands', 'NL'), ('Norway', 'NO'), ('Poland', 'PL'), ('Portugal', 'PT'), ('Romania', 'RO'), ('Sweden', 'SE'), ('Slovenia', 'SI'), ('Slovakia', 'SK'), ('Turkey', 'TR')], max_length=64),
        ),
        migrations.AlterField(
            model_name='company',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
