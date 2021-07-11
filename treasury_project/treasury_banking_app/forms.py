from django import forms
from django.forms import ModelForm
from treasury_banking_app.models import Bank, Access


class UserCreateForm(forms.Form):
    name = forms.CharField(max_length=255)
    surname = forms.CharField(max_length=255, required=True)
    internal_id = forms.CharField(max_length=7, required=True)
    is_administrator = forms.BooleanField(initial=False, required=False)
    is_payment_creator = forms.BooleanField(initial=False, required=False)
    is_payment_approver = forms.BooleanField(initial=False, required=False)
    can_delete_payment = forms.BooleanField(initial=False, required=False)


class AdministratorCreateForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    surname = forms.CharField(max_length=255, required=True)
    login = forms.CharField(max_length=7, required=True)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput, required=True)
    password_repeat = forms.CharField(max_length=64, widget=forms.PasswordInput, required=True)


class CompanyCreateForm(forms.Form):
    name = forms.CharField(max_length=255)
    country = forms.CharField(max_length=255)


class BankAddForm(ModelForm):
    class Meta:
        model = Bank
        fields = ['name']




