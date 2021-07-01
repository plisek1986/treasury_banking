from django.db import models

PERMISSION_CHOICE = (
    ('CREATE_PAYMENT', 'Create Payment'),
    ('DELETE_PAYMENT', 'Delete Payment'),
    ('APPROVE_PAYMENT', 'Approve Payment'),
)


class User(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    surname = models.CharField(max_length=255, blank=False)
    internal_id = models.CharField(max_length=7, blank=False)
    account = models.ManyToManyField('Account')
    is_administrator = models.BooleanField(default=False)
    permission = models.ManyToManyField('Permission')


class Permission(models.Model):
    type = models.CharField(max_length=64, choices=PERMISSION_CHOICE)

    def __str__(self):
        return self.type


class Administrator(models.Model):
    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=255, blank=False)
    login = models.CharField(max_length=255, blank=False)
    password = models.CharField(max_length=64)


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)
    bank = models.ManyToManyField('Bank')

    def __str__(self):
        return self.name


class Bank(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Account(models.Model):
    iban_number = models.CharField(max_length=64, unique=True)
    swift_code = models.CharField(max_length=64)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
