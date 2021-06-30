from django.shortcuts import render, redirect
from django.views import View
from treasury_banking_app.models import User, Account, PERMISSION_CHOICE


class MainPageView(View):
    def get(self, request):
        return render(request, 'main_page.html')


class DashboardView(View):
    def get(self, request):
        return render(request, 'dashboard.html')


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
        permission = request.POST.get('permission')
        account = request.POST.get('account')
        internal_id = request.POST.get('internal_id')
        if len(internal_id) < 7:
            message = 'Provided internal ID is too short'
            return render(request, 'user_edit.html', {'user': user, 'accounts': accounts,
                                                      'message': message,
                                                      'permission_choice': PERMISSION_CHOICE})
        else:
            pass
        user.name = name
        user.surname = surname
        user.internal_id = internal_id
        user.is_administrator = is_administrator
        # user.account.set = account
        user.permission = permission
        user.save()
        return redirect('users-list')
