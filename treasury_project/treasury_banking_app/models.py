from django.db import models


# array used as choice attribute in access model
ACCESS_CHOICE = [
    ('CREATE_PAYMENT', 'Create Payment'),
    ('DELETE_PAYMENT', 'Delete Payment'),
    ('APPROVE_PAYMENT', 'Approve Payment'),
]


# array used as choice attribute in account model
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
    ('France',  'FR'),  # France
    ('United Kingdom', 'GB'),  # United Kingdom
    ('Greece', 'GR'),  # Greece
    ('Croatia','HR'),  # Croatia
    ('Hungary', 'HU'),  # Hungary
    ('Ireland', 'IE'),  # Ireland
    ('Iceland', 'IS'),  # Iceland
    ('Italy', 'IT'),  # Italy
    ('Kazakhstan', 'KZ'),  # Kazakhstan
    ('Lithuania', 'LT'),  # Lithuania
    ('Latvia', 'LV'),  # Latvia
    ('Netherlands', 'NL'),  # Netherlands
    ('Norway', 'NO'),  # Norway
    ('Poland', 'PL'),  # Poland
    ('Portugal', 'PT'),  # Portugal
    ('Romania', 'RO'),  # Romania
    ('Sweden', 'SE'),  # Sweden
    ('Slovenia', 'SI'),  # Slovenia
    ('Slovakia', 'SK'),  # Slovakia
    ('Turkey', 'TR'),  # Turkey
]


class User(models.Model):
    """ Class defines attributes for each user object"""

    name = models.CharField(max_length=255, blank=False, null=False)
    surname = models.CharField(max_length=255, blank=False, null=False)
    internal_id = models.CharField(max_length=7, blank=False, null=False)
    account = models.ManyToManyField('Account')
    is_administrator = models.BooleanField(default=False)
    is_payment_creator = models.BooleanField(default=False)
    is_payment_approver = models.BooleanField(default=False)
    can_delete_payment = models.BooleanField(default=False)
    access = models.ManyToManyField('Access')


class Access(models.Model):
    """ Class defines attributes for each access object"""

    access_type = models.CharField(max_length=64, choices=ACCESS_CHOICE)

    def __str__(self):
        """
        Functions returns access object in a form of a string
        :return: string
        """

        return self.access_type


class Administrator(models.Model):
    """ Class defines attributes for each administrator object"""

    name = models.CharField(max_length=255, blank=False)
    surname = models.CharField(max_length=255, blank=False)
    login = models.CharField(max_length=7, blank=False)
    password = models.CharField(max_length=64, blank=False, null=False)
    password_repeat = models.CharField(max_length=64, blank=False, null=False)

    def __str__(self):
        """
        Functions returns administrator object in a form of a string
        :return: string
        """

        return self.name


class Company(models.Model):
    """ Class defines attributes for each company object"""

    name = models.CharField(max_length=255, unique=True, blank=False)
    country = models.CharField(max_length=64, choices=COUNTRY_CHOICE)

    def __str__(self):
        """
        Functions returns administrator object in a form of a string
        :return: string
        """

        return self.name


class Bank(models.Model):
    """ Class defines attributes for each bank object"""

    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        """
        Functions returns administrator object in a form of a string
        :return: string
        """

        return self.name


class Account(models.Model):
    """ Class defines attributes for each account object"""

    iban_number = models.CharField(max_length=64, unique=True, blank=False, null=False)
    swift_code = models.CharField(max_length=11, blank=False)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
