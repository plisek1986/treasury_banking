from django.shortcuts import render, redirect
from django.views import View

from treasury_banking_app.forms import UserCreateForm, CompanyCreateForm, BankAddForm
from treasury_banking_app.models import User, Account, ACCESS_CHOICE, Company, Bank


#
# IBAN_COUNTRY_CODE_LENGTH = {
#     'Austria': 20,  # Austria
#     'Belgium': 16,  # Belgium
#     'Bulgaria': 22,  # Bulgaria
#     'Switzerland': 21,  # Switzerland
#     'Czech Republic': 24,  # Czech Republic
#     'Germany': 22,  # Germany
#     'Denmark': 18,  # Denmark
#     'Estonia': 20,  # Estonia
#     'Spain': 24,  # Spain
#     'Finland': 18,  # Finland
#     'France': 27,  # France
#     'United Kingdom': 22,  # United Kingdom + Guernsey, Isle of Man, Jersey
#     'GR': 27,  # Greece
#     'HR': 21,  # Croatia
#     'HU': 28,  # Hungary
#     'IE': 22,  # Ireland
#     'IS': 26,  # Iceland
#     'IT': 27,  # Italy
#     'KZ': 20,  # Kazakhstan
#     'LT': 20,  # Lithuania
#     'LV': 21,  # Latvia
#     'NL': 18,  # Netherlands
#     'NO': 15,  # Norway
#     'PL': 28,  # Poland
#     'PT': 25,  # Portugal
#     'RO': 24,  # Romania
#     'SE': 24,  # Sweden
#     'SI': 19,  # Slovenia
#     'SK': 24,  # Slovakia
#     'TR': 26,  # Turkey
# }


class MainPageView(View):
    def get(self, request):
        return render(request, 'main_page.html')


class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')


class UserCreateView(View):
    def get(self, request):
        form = UserCreateForm()
        return render(request, 'user_create.html', {'form': form})

    def post(self, request):
        form = UserCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            internal_id = form.cleaned_data['internal_id']
            if len(internal_id) < 7:
                message = 'Provided internal ID is too short'
                return render(request, 'user_create.html', {'form': form, 'message': message})
            elif User.objects.filter(internal_id=internal_id):
                message = 'Provided internal ID already exists in the database'
                return render(request, 'user_create.html', {'form': form, 'message': message})
            is_payment_approver = form.cleaned_data['is_payment_approver']
            is_payment_creator = form.cleaned_data['is_payment_creator']
            is_administrator = form.cleaned_data['is_administrator']
            can_delete_payment = form.cleaned_data['can_delete_payment']
            if is_payment_creator is True and is_payment_approver is True:
                message = 'Violation of segregation of duties. User cannot create and approve payments.'
                return render(request, 'user_create.html', {'form': form, 'message': message})
            User.objects.create(name=name, surname=surname, internal_id=internal_id,
                                is_administrator=is_administrator, is_payment_creator=is_payment_creator,
                                is_payment_approver=is_payment_approver, can_delete_payment=can_delete_payment)
            return redirect('/users_list/')


class UsersListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'users_list.html', {'users': users})


class UserView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        accounts = user.account.all()
        return render(request, 'user_view.html', {'user': user, 'accounts': accounts})


class UserEditView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        accounts = Account.objects.all()
        return render(request, 'user_edit.html', {'user': user, 'accounts': accounts})

    def post(self, request, user_id):
        user = User.objects.get(pk=user_id)
        surname = request.POST.get('user_surname')
        is_administrator = request.POST.get('administrator')
        if is_administrator == "on":
            is_administrator = True
        else:
            is_administrator = False
        is_payment_creator = request.POST.get('creator')
        if is_payment_creator == "on":
            is_payment_creator = True
        else:
            is_payment_creator = False
        is_payment_approver = request.POST.get('approver')
        if is_payment_approver == "on":
            is_payment_approver = True
        else:
            is_payment_approver = False
        can_delete_payment = request.POST.get('delete')
        if can_delete_payment == "on":
            can_delete_payment = True
        else:
            can_delete_payment = False
        if is_payment_creator is True and is_payment_approver is True:
            message = 'Violation of segregation of duties. User cannot create and approve payments.'
            return render(request, 'user_edit.html', {'user': user, 'message': message})
        user.surname = surname
        user.is_administrator = is_administrator
        user.is_payment_creator = is_payment_creator
        user.is_payment_approver = is_payment_approver
        user.can_delete_payment = can_delete_payment
        user.save()
        return redirect(f'/user_view/{user_id}/')


def user_delete(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('users-list')
    return render(request, 'user_delete.html', {'user': user})


def user_view_delete(request, user_id):
    user = User.objects.get(pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('users-list')
    return render(request, 'user_view_delete.html', {'user': user})


class UserAddAccountsView(View):
    def get(self, request, user_id):
        user = User.objects.get(pk=user_id)
        accounts = Account.objects.all()
        user_accounts = user.account.all()
        available_accounts = []
        for account in accounts:
            if account not in user_accounts:
                available_accounts.append(account)
        return render(request, 'user_add_accounts.html', {'user': user, 'available_accounts': available_accounts})

    def post(self, request, user_id):
        user = User.objects.get(pk=user_id)
        accounts = request.POST.getlist('accounts')
        for account in accounts:
            user_account = Account.objects.get(iban_number=account)
            user.account.add(user_account)
        user.save()
        return redirect(f'/user_view/{user_id}/')


def user_remove_accounts(request, user_id, account_id):
    if request.method == "GET":
        user = User.objects.get(pk=user_id)
        account = Account.objects.get(pk=account_id)
        user.account.remove(account)
        user.save()
        return redirect(f'/user_view/{user_id}/')


class CompanyCreateView(View):
    def get(self, request):
        form = CompanyCreateForm()
        return render(request, 'company_create.html', {'form': form})

    def post(self, request):
        form = CompanyCreateForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            country = form.cleaned_data['country']
            if Company.objects.filter(name=name):
                message = 'Company with this name already exists in database.'
                return render(request, 'company_create.html', {'form': form, 'message': message})
            Company.objects.create(name=name, country=country)
            return redirect('company-list')


class CompanyListView(View):
    def get(self, request):
        companies = Company.objects.all()
        return render(request, 'company_list.html', {'companies': companies})


class CompanyView(View):
    def get(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        accounts = company.account_set.all()
        return render(request, 'company_view.html', {'company': company, 'accounts': accounts})


def company_delete(request, company_id):
    company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        company.delete()
        return redirect('company-list')
    return render(request, 'company_delete.html', {'company': company})


def company_view_delete(request, company_id):
    company = Company.objects.get(pk=company_id)
    if request.method == 'POST':
        company.delete()
        return redirect('company-list')
    return render(request, 'company_view_delete.html', {'company': company})


class CompanyAddAccountView(View):
    def get(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        banks = Bank.objects.all()
        return render(request, 'company_add_account.html', {'company': company, 'banks': banks})

    def post(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        iban_number = request.POST.get('iban')
        swift_code = request.POST.get('swift')
        bank = request.POST.get('bank')
        bank = Bank.objects.get(name=bank)
        account = Account.objects.create(iban_number=iban_number, swift_code=swift_code, bank=bank, company=company)
        account.save()
        return redirect(f'/company_view/{company_id}/')


def company_delete_accounts(request, account_id, company_id):
    company = Company.objects.get(pk=company_id)
    account = Account.objects.get(pk=account_id)
    if request.method == 'POST':
        account.delete()
        return redirect(f'/company_view/{company_id}/')
    return render(request, 'company_account_delete.html', {'company': company, 'account': account})


class CompanyEditView(View):
    def get(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        return render(request, 'company_edit.html', {'company': company})

    def post(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        name = request.POST.get('name')
        if Company.objects.filter(name=name):
            message = 'Company with this name already exists in database.'
            return render(request, 'company_edit.html', {'company': company, 'message': message})
        country = request.POST.get('country')
        company.name = name
        company.country = country
        company.save()
        return redirect('company-list')


class AccountCreateView(View):
    def get(self, request):
        banks = Bank.objects.all()
        companies = Company.objects.all()
        return render(request, 'account_create.html', {'banks': banks, 'companies': companies})

    def post(self, request):
        banks = Bank.objects.all()
        companies = Company.objects.all()
        iban_number = request.POST.get('iban')
        if not iban_number:
            message = 'Please provide iban number.'
            return render(request, 'account_create.html', {'banks': banks, 'companies': companies, 'message': message})
        swift_code = request.POST.get('swift')
        bank = request.POST.get('bank')
        bank = Bank.objects.get(name=bank)
        company = request.POST.get('company')
        company = Company.objects.get(name=company)
        Account.objects.create(iban_number=iban_number, swift_code=swift_code,
                               bank=bank, company=company)
        return redirect('accounts-list')


class AccountListView(View):
    def get(self, request):
        accounts = Account.objects.all().order_by('-company')
        return render(request, 'account_list.html', {'accounts': accounts})


def account_delete(request, account_id):
    account = Account.objects.get(pk=account_id)
    if request.method == 'POST':
        account.delete()
        return redirect('accounts-list')
    return render(request, 'account_delete.html', {'account': account})


def bank_account_delete(request, account_id, bank_id):
    account = Account.objects.get(pk=account_id)
    bank = Bank.objects.get(pk=bank_id)
    if request.method == 'POST':
        account.delete()
        return redirect(f'/bank_view/{bank_id}/')
    return render(request, 'bank_account_delete.html', {'account': account, 'bank': bank})


class BankAddView(View):
    def get(self, request):
        form = BankAddForm()
        return render(request, 'bank_add.html', {'form': form})

    def post(self, request):
        form = BankAddForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            if Bank.objects.filter(name=name):
                message = 'This bank already exists in database'
                return render(request, 'bank_add.html', {'form': form, 'message': message})
            Bank.objects.create(name=name)
            return redirect('banks-list')


class BankListView(View):
    def get(self, request):
        banks = Bank.objects.all()
        return render(request, 'banks_list.html', {'banks': banks})


class BankViewView(View):
    def get(self, request, bank_id):
        bank = Bank.objects.get(pk=bank_id)
        accounts = bank.account_set.all()
        return render(request, 'bank_view.html', {'bank': bank, 'accounts': accounts})


def bank_delete(request, bank_id):
    bank = Bank.objects.get(pk=bank_id)
    if request.method == 'POST':
        bank.delete()
        return redirect('banks-list')
    return render(request, 'bank_delete.html', {'bank': bank})


def bank_view_delete(request, bank_id):
    bank = Bank.objects.get(pk=bank_id)
    if request.method == 'POST':
        bank.delete()
        return redirect('banks-list')
    return render(request, 'bank_view_delete.html', {'bank': bank})
