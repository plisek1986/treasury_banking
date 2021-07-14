import pytest
from django.test import Client
from treasury_banking_app.models import User, Company, Administrator, Account, Bank


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def user():
    user = User.objects.create(name='Janek', surname='Kowalski',
                               internal_id='PUHgjdJ', is_administrator=True,
                               is_payment_creator=True, is_payment_approver=False,
                               can_delete_payment=True)
    return user


@pytest.fixture
def company():
    company = Company.objects.create(name='Tre G.M.B.H.', country='Germany')
    return company


@pytest.fixture
def administrator():
    administrator = Administrator.objects.create(name='Michał', surname='Paluch',
                                                 login='Udfsr43', password='Password_3',
                                                 password_repeat='Password_3')
    return administrator


@pytest.fixture
def bank():
    bank = Bank.objects.create(name='Random Bank')
    return bank


@pytest.fixture
def account():
    bank_test = Bank.objects.create(name='R-Bank')
    company_test = Company.objects.create(name='Tre Belarus', country='Belarus')
    account = Account.objects.create(iban_number='TEEdddddddfs', swift_code='tertrefdsf',
                                     bank=bank_test, company=company_test)
    return account
