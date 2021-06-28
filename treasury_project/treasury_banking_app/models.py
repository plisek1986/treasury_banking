from django.db import models


class User(models.Model):
    TREASURY = 'TRE'
    NON_TREASURY = 'NTRE'
    TEAM_CHOICE = [
        (TREASURY, 'TREASURY'),
        (NON_TREASURY, 'NON-TREASURY'),
    ]
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=False)
    internal_id = models.CharField(max_length=7, blank=False)
    team = models.CharField(max_length=4, choices=TEAM_CHOICE)
    account = models.ManyToManyField('Account')
    is_administrator = models.BooleanField(default=False)


class Administrator(models.Model):
    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=255, blank=False)
    login = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=64)


class Permission(models.Model):
    CREATE_PAYMENT = 'CR'
    DELETE_PAYMENT = 'DP'
    APPROVE_PAYMENT = 'AP'
    PERMISSION_CHOICE = [
        (CREATE_PAYMENT, 'Create Payment'),
        (DELETE_PAYMENT, 'Delete Payment'),
        (APPROVE_PAYMENT, 'Approve Payment'),
    ]
    permission_type = models.CharField(max_length=2, choices=PERMISSION_CHOICE)
    user = models.ManyToManyField(User)


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)
    bank = models.ManyToManyField('Bank')


class Bank(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Account(models.Model):
    iban_number = models.CharField(max_length=64, unique=True)
    swift_code = models.CharField(max_length=64)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
