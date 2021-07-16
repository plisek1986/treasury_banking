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


class AdministratorCreateForm(ModelForm):
    """ Class utilizes ModelForm for creating a form for a new admin"""

    password = forms.CharField(widget=forms.PasswordInput)
    password_repeat = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        """ Class utilizes model User for translating user model attributes into form fields"""

        model = Administrator
        fields = ['name', 'surname', 'login', 'password', 'password_repeat']
        widgets = {
            'password': forms.PasswordInput(),
            'password_repeat': forms.PasswordInput(),
        }


class BankAddForm(ModelForm):
    class Meta:
        model = Bank
        fields = ['name']


class LoginForm(forms.Form):
    login = forms.CharField(max_length=64, required=True)
    password = forms.CharField(max_length=64, widget=forms.PasswordInput, required=True)
