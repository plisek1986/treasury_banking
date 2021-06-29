from django.shortcuts import render
from django.views import View
from treasury_banking_app.models import User


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
        accounts = user.account.all()
        return render(request, 'user_edit.html', {'user': user, 'accounts': accounts})
