from django.shortcuts import render, redirect
from django.views import View

from treasury_banking_app.forms import UserCreateForm
from treasury_banking_app.models import User, Account, ACCESS_CHOICE


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
            is_administrator = form.cleaned_data['is_administrator']
            # access = form.cleaned_data['access']
            # if access == 'Create Payment' and access == 'Approve Payment':
            #     message = 'Violation of segregation of duties. User cannot create and approve payments'
            #     return render(request, 'user_create.html', {'form': form, 'message': message})
            User.objects.create(name=name, surname=surname, internal_id=internal_id,
                                is_administrator=is_administrator)
            # user.access.set(access)
            # user.save()
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
        is_administrator = request.POST.get('administrator') == 'on'
        access = request.POST.get('access')
        account = request.POST.get('account')
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
