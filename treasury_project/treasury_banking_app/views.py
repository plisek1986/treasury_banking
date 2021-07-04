from django.shortcuts import render, redirect
from django.views import View

from treasury_banking_app.forms import UserCreateForm, CompanyCreateForm
from treasury_banking_app.models import User, Account, ACCESS_CHOICE, Company, Bank
from django.http import HttpResponseRedirect, HttpResponse


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
                message = 'Violation of segregation of duties. User cannot create and approve payments'
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
        accounts = Account.objects.all()
        name = request.POST.get('user_name')
        surname = request.POST.get('user_surname')
        is_administrator = request.POST.get('administrator')
        # access = request.POST.get('access')
        # account = request.POST.get('account')
        internal_id = request.POST.get('internal_id')
        if len(internal_id) < 7:
            message = 'Provided internal ID is too short'
            return render(request, 'user_edit.html', {'user': user, 'accounts': accounts,
                                                      'message': message,
                                                      'access_choice': ACCESS_CHOICE})
        user.name = name
        user.surname = surname
        user.internal_id = internal_id
        user.is_administrator = is_administrator
        # user.account.set = account
        # user.access.set(access.value)
        user.save()
        return redirect('users-list')


def user_delete(request, user_id):
    if request.method == 'GET':
        user = User.objects.get(pk=user_id)
        user.delete()
        response = HttpResponseRedirect('/users_list/')
        return response


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
                message = 'Company with this name already exists in database'
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
    if request.method == 'GET':
        company = Company.objects.get(pk=company_id)
        company.delete()
        return redirect('company-list')


class CompanyAddAccountView(View):
    def get(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        banks = Bank.objects.all()
        return render(request, 'add_account.html', {'company': company, 'banks': banks})

    def post(self, request, company_id):
        company = Company.objects.get(pk=company_id)
        iban_number = request.POST.get('iban')
        swift_code = request.POST.get('swift')
        bank = request.POST.get('bank')
        bank = Bank.objects.get(name=bank)
        account = Account.objects.create(iban_number=iban_number, swift_code=swift_code, bank=bank, company=company)
        account.save()
        return redirect(f'/company_view/{company_id}/')


class AccountCreateView(View):
    def get(self, request):
        banks = Bank.objects.all()
        companies = Company.objects.all()
        return render(request, 'account_create.html', {'banks': banks, 'companies': companies})

    def post(self, request):
        iban_number = request.POST.get('iban')
        swift_code = request.POST.get('swift')
        bank = request.POST.get('bank')
        bank = Bank.objects.get(name=bank)
        company = request.POST.get('company')
        company = Company.objects.get(name=company)
        Account.objects.create(iban_number=iban_number, swift_code=swift_code,
                               bank=bank, company=company)
        return redirect('/')


class AccountListView(View):
    def get(self, request):
        accounts = Account.objects.all().order_by('-company')
        return render(request, 'account_list.html', {'accounts': accounts})


def account_delete(request, account_id):
    if request.method == 'GET':
        account = Account.objects.get(pk=account_id)
        account.delete()
        return redirect('accounts-list')
