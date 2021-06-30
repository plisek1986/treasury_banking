from django.db import models
from django import forms
from treasury_banking_app.models import Account, PERMISSION_CHOICE, Bank, User


class UserViewForm(forms.Form):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255, required=True)
    internal_id = forms.CharField(max_length=7, required=True)
    account = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple)
    is_administrator = forms.BooleanField(initial=False)
    permission = forms.MultipleChoiceField(choices=PERMISSION_CHOICE, widget=forms.CheckboxSelectMultiple)


class AdministratorViewForm(models.Model):
    name = forms.CharField(max_length=255, required=True)
    surname = forms.CharField(max_length=255, required=True)
    login = forms.CharField(max_length=255, required=True)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput)


class CompanyViewForm(models.Model):
    name = forms.CharField(max_length=255, unique=True)
    country = forms.CharField(max_length=255)
    bank = forms.MultipleChoiceField(Bank.objects.all(), widget=forms.CheckboxSelectMultiple)


class BankViewForm(models.Model):
    name = forms.CharField(max_length=255, unique=True)


class AccountViewForm(models.Model):
    class Meta:
        model = Account
        fields = ['iban_number', 'swift_code', 'bank', 'company']
