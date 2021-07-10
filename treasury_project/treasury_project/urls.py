"""treasury_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from treasury_banking_app import views as all_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', all_views.MainPageView.as_view(), name='main'),
    path('dashboard/', all_views.DashboardView.as_view(), name='dashboard'),
    path('users_list/', all_views.UsersListView.as_view(), name='users-list'),
    path('user_view/<int:user_id>/', all_views.UserView.as_view(), name='user-view'),
    path('user_edit/<int:user_id>/', all_views.UserEditView.as_view(), name='user-edit'),
    path('user_create/', all_views.UserCreateView.as_view(), name='user-create'),
    path('user_delete/<int:user_id>/', all_views.user_delete, name='user-delete'),
    path('user_view_delete/<int:user_id>/', all_views.user_view_delete, name='user-view-delete'),
    path('user_add_accounts/<int:user_id>/', all_views.UserAddAccountsView.as_view(), name='user-add-accounts'),
    path('company_create/', all_views.CompanyCreateView.as_view(), name='company-create'),
    path('company_edit/<int:company_id>/', all_views.CompanyEditView.as_view(), name='company-edit'),
    path('company_list/', all_views.CompanyListView.as_view(), name='company-list'),
    path('company_view/<int:company_id>/', all_views.CompanyView.as_view(), name='company-view'),
    path('company_delete/<int:company_id>/', all_views.company_delete, name='company-delete'),
    path('company_view_delete/<int:company_id>/', all_views.company_view_delete, name='company-view-delete'),
    path('company_add_account/<int:company_id>/', all_views.CompanyAddAccountView.as_view(), name='add-account'),
    path('account_create/', all_views.AccountCreateView.as_view(), name='account-create'),
    path('accounts_list/', all_views.AccountListView.as_view(), name='accounts-list'),
    path('account_delete/<int:account_id>/', all_views.account_delete, name='account-delete'),
    path('account_edit/<int:account_id>/', all_views.AccountEditView.as_view(), name='account-edit'),
    path('bank_add/', all_views.BankAddView.as_view(), name='bank-add'),
    path('bank_list/', all_views.BankListView.as_view(), name='banks-list'),
    path('user_remove_accounts/<int:user_id>/<int:account_id>/', all_views.user_remove_accounts,
         name='user-remove-accounts'),
    path('company_delete_accounts/<int:company_id>/<int:account_id>/', all_views.company_delete_accounts,
         name='company-delete-accounts'),
    path('bank_view/<int:bank_id>/', all_views.BankViewView.as_view(), name='bank-view'),
    path('bank_account_delete/<int:bank_id>/<int:account_id>/', all_views.bank_account_delete,
         name='bank-account-delete'),
    path('bank_delete/<int:bank_id>/', all_views.bank_delete, name='bank-delete'),
    path('bank_view_delete/<int:bank_id>/', all_views.bank_view_delete, name='bank-view-delete'),
    path('bank_edit/<int:bank_id>/', all_views.BankEditView.as_view(), name='bank-edit'),
    path('access_types_list/', all_views.AccessTypesListView.as_view(), name='accesses-list'),
    path('admin_create/', all_views.AdministratorCreateView.as_view(), name='admin-create'),
    path('admin_list/', all_views.AdministratorListView.as_view(), name='admins-list')
]
