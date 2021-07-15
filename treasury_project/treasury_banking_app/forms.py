from django import forms
from django.forms import ModelForm
from treasury_banking_app.models import Bank, User, Administrator, Company


class UserCreateForm(ModelForm):
    """ Class utilizes ModelForm for creating a form for a new user"""

    class Meta:
        """ Class utilizes model User for translating user model attributes into form fields"""

        model = User
        fields = ['name', 'surname', 'internal_id', 'is_administrator', 'is_payment_creator', 'is_payment_approver',
                  'can_delete_payment']

    # name = forms.CharField(max_length=255)
    # surname = forms.CharField(max_length=255, required=True)
    # internal_id = forms.CharField(max_length=7, required=True)
    # is_administrator = forms.BooleanField(initial=False, required=False)
    # is_payment_creator = forms.BooleanField(initial=False, required=False)
    # is_payment_approver = forms.BooleanField(initial=False, required=False)
    # can_delete_payment = forms.BooleanField(initial=False, required=False)


class AdministratorCreateForm(ModelForm):
    """ Class utilizes ModelForm for creating a form for a new admin"""

    class Meta:
        """ Class utilizes model User for translating user model attributes into form fields"""

        model = Administrator
        fields = ['name', 'surname', 'login', 'password', 'password_repeat']

    # name = forms.CharField(max_length=255, required=True)
    # surname = forms.CharField(max_length=255, required=True)
    # login = forms.CharField(max_length=7, required=True)
    # password = forms.CharField(max_length=64, widget=forms.PasswordInput, required=True)
    # password_repeat = forms.CharField(max_length=64, widget=forms.PasswordInput, required=True)


# class CompanyCreateForm(ModelForm):
#     """ Class utilizes ModelForm for creating a form for a new admin"""
#
#     class Meta:
#         """ Class utilizes model User for translating user model attributes into form fields"""
#
#         model = Company
#         fields = ['name', 'country']
#
#
    # name = forms.CharField(max_length=255)
    # country = forms.CharField(max_length=255)


class BankAddForm(ModelForm):
    class Meta:
        model = Bank
        fields = ['name']


class LoginForm(forms.Form):
    login = forms.CharField(max_length=64, required=True)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput, required=True)
