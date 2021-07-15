import pytest


@pytest.mark.django_db
def test_user_list_view(client):
    """Test to view the list of user objects sorted by name"""

    response = client.get('/users_list/')
    users_from_context = response.context['users']
    li1 = list(users_from_context.values_list('name', flat=True))
    li2 = list(users_from_context.values_list('name', flat=True))
    li1.sort()
    assert response.status_code == 200
    assert li1 == li2


@pytest.mark.django_db
def test_company_list_view(client):
    """Test to view the list of company objects sorted by name"""

    response = client.get('/company_list/')
    companies_from_context = response.context['companies']
    li1 = list(companies_from_context.values_list('name', flat=True))
    li2 = list(companies_from_context.values_list('name', flat=True))
    li1.sort()
    assert response.status_code == 200
    assert li1 == li2


@pytest.mark.django_db
def test_account_list_view(client):
    """Test to view the list of account objects sorted by company owning the account"""

    response = client.get('/accounts_list/')
    accounts_from_context = response.context['accounts']
    li1 = list(accounts_from_context.values_list('company', flat=True))
    li2 = list(accounts_from_context.values_list('company', flat=True))
    li1.sort()
    assert response.status_code == 200
    assert li1 == li2


@pytest.mark.django_db
def test_bank_list_view(client):
    """Test to view the list of bank objects sorted by name"""

    response = client.get('/bank_list/')
    banks_from_context = response.context['banks']
    li1 = list(banks_from_context.values_list('name', flat=True))
    li2 = list(banks_from_context.values_list('name', flat=True))
    li1.sort()
    assert response.status_code == 200
    assert li1 == li2


@pytest.mark.django_db
def test_access_types_list_view(client):
    """Test to view the list of access types objects sorted by access type"""

    response = client.get('/access_types_list/')
    access_types_from_context = response.context['access_types']
    li1 = list(access_types_from_context)
    li2 = list(access_types_from_context)
    li1.sort()
    assert response.status_code == 200
    assert li1 == li2


@pytest.mark.django_db
def admin_list_view(client):
    """Test to view the list of admin objects sorted by name"""

    response = client.get('/admin_list/')
    admins_types_from_context = response.context['access_types']
    li1 = list(admins_types_from_context.values_list('name', flat=True))
    li2 = list(admins_types_from_context.values_list('name', flat=True))
    li1.sort()
    assert response.status_code == 200
    assert li1 == li2
