import pytest
from treasury_banking_app.models import User, Company, Administrator, Bank, Account


@pytest.mark.django_db
def test_user_create_view(client):
    """Test to create a user from information passed in the user create form"""

    name = 'Katarzyna'
    surname = 'Solska'
    internal_id = 'PKY8978'
    is_administrator = True
    is_payment_creator = True
    is_payment_approver = False
    can_delete_payment = True
    response = client.post('/user_create/', {'name': name,
                                             'surname': surname,
                                             'internal_id': internal_id,
                                             'is_administrator': is_administrator,
                                             'is_payment_creator': is_payment_creator,
                                             'is_payment_approver': is_payment_approver,
                                             'can_delete_payment': can_delete_payment})
    assert response.status_code == 302
    assert User.objects.get(name=name)


@pytest.mark.django_db
def test_user_model(user):
    """Test to create a user from information passed in user model"""

    assert User.objects.get(name='Janek') == user


@pytest.mark.django_db
def test_company_create_view(client):
    """Test to create a company from information passed in the company create form"""

    name = 'Tre Bulgaria'
    country = 'Bulgaria'
    response = client.post('/company_create/', {'name': name, 'country': country})

    assert response.status_code == 302
    assert Company.objects.get(name=name)


@pytest.mark.django_db
def test_company_model(company):
    """Test to create a company from information passed in company model"""

    assert Company.objects.get(name='Tre G.M.B.H.') == company


@pytest.mark.django_db
def test_administrator_create_view(client):
    """Test to create an administrator from information passed in the administrator create form"""

    name = 'Jacek'
    surname = 'Kruchy'
    login = 'PLIjds7'
    password = 'Password_2'
    password_repeat = 'Password_2'
    response = client.post('/admin_create/', {'name': name, 'surname': surname, 'login': login,
                                              'password': password, 'password_repeat': password_repeat})

    assert response.status_code == 302
    assert Administrator.objects.get(name=name)


@pytest.mark.django_db
def test_administrator_model(administrator):
    """Test to create an administrator from information passed in administrator model"""

    assert Administrator.objects.get(surname='Paluch') == administrator


@pytest.mark.django_db
def test_bank_model(bank):
    """Test to create a bank from information passed in bank model"""

    assert Bank.objects.get(name='Random Bank') == bank


@pytest.mark.django_db
def test_account_model(account):
    """Test to create an account from information passed in account model"""

    assert Account.objects.get(iban_number='TEEdddddddfs')
