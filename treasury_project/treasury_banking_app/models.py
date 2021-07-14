from django.db import models


ACCESS_CHOICE = [
    ('CREATE_PAYMENT', 'Create Payment'),
    ('DELETE_PAYMENT', 'Delete Payment'),
    ('APPROVE_PAYMENT', 'Approve Payment'),
]

COUNTRY_CHOICE = [
    ('Austria', 'AT'),  # Austria
    ('Belgium', 'BE'),  # Belgium
    ('Bulgaria', 'BG'),  # Bulgaria
    ('Switzerland', 'CH'),  # Switzerland
    ('Czech Republic', 'CZ'),  # Czech Republic
    ('Germany', 'DE'),  # Germany
    ('Denmark', 'DK'),  # Denmark
    ('Estonia', 'EE'),  # Estonia
    ('Spain', 'ES'),  # Spain
    ('Finland', 'FI'),  # Finland
]


class User(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=False)
    internal_id = models.CharField(max_length=7, blank=False)
    account = models.ManyToManyField('Account')
    is_administrator = models.BooleanField(default=False)
    is_payment_creator = models.BooleanField(default=False)
    is_payment_approver = models.BooleanField(default=False)
    can_delete_payment = models.BooleanField(default=False)
    access = models.ManyToManyField('Access')


class Access(models.Model):
    access_type = models.CharField(max_length=64, choices=ACCESS_CHOICE)

    def __str__(self):
        return self.access_type


class Administrator(models.Model):
    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=255, blank=False)
    login = models.CharField(max_length=7, blank=False, unique=True)
    password = models.CharField(max_length=64, blank=False, null=False)
    password_repeat = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False)
    country = models.CharField(max_length=64, choices=COUNTRY_CHOICE)

    def __str__(self):
        return self.name


class Bank(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Account(models.Model):
    iban_number = models.CharField(max_length=64, unique=True, blank=False, null=False)
    swift_code = models.CharField(max_length=11, blank=False)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
