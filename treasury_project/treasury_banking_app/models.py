from django.db import models

TEAM_CHOICE = (
    ('treasury', 'TREASURY'),
    ('non-treasury', 'NON-TREASURY'),
)

PERMISSION_CHOICE = (
    ('create payment', 'CREATE PAYMENT'),
    ('approve payment', 'APPROVE PAYMENT'),
    ('safety administrator', 'SAFETY ADMINISTRATOR'),
)


class User(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=False)
    internal_id = models.CharField(max_length=7, blank=False)
    team = models.CharField(max_length=255, choices=TEAM_CHOICE)
    account = models.ManyToManyField('Account')


class Permission(models.Model):
    permission_type = models.CharField(max_length=255, choices=PERMISSION_CHOICE)
    aml_required = models.BooleanField(default=False)
    user = models.ManyToManyField(User)


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255, unique=True)
    bank = models.ManyToManyField('Bank')


class Bank(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Account(models.Model):
    iban_number = models.CharField(max_length=64, unique=True)
    swift_code = models.CharField(max_length=64)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
