from django.db import models
from django import forms
from django.forms import ModelForm
from treasury_banking_app.models import Account, ACCESS_CHOICE, Bank, User


class UserCreateForm(forms.Form):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255, required=True)
    internal_id = forms.CharField(max_length=7, required=True)
    # account = forms.MultipleChoiceField(choices=Account.objects.get(pk=2), widget=forms.CheckboxSelectMultiple)
    is_administrator = forms.BooleanField(initial=False, required=False)
    is_payment_creator = forms.BooleanField(initial=False, required=False)
    is_payment_approver = forms.BooleanField(initial=False, required=False)
    can_delete_payment = forms.BooleanField(initial=False, required=False)


# class AdministratorViewForm(models.Model):
#     name = forms.CharField(max_length=255, required=True)
#     surname = forms.CharField(max_length=255, required=True)
#     login = forms.CharField(max_length=255, required=True)
#     password = forms.CharField(max_length=64, widget=forms.PasswordInput)


class CompanyCreateForm(forms.Form):
    name = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)


class BankAddForm(ModelForm):
    class Meta:
        model = Bank
        fields = ['name']


# class AccountCreateForm(models.Model):
#     class Meta:
#         model = Account()
#         fields = ['iban_number', 'swift_code', 'bank', 'company']
