import pytest
from django.test import Client
from treasury_banking_app.models import User, Company, Administrator, Account, Bank


@pytest.fixture
def client():
    """Fixture for client object passed as an argument to the test functions"""

    client = Client()
    return client


@pytest.fixture
def user():
    """Fixture for user object passed as an argument to the user create view test function"""

    user = User.objects.create(name='Janek', surname='Kowalski',
                               internal_id='PUHgjdJ', is_administrator=True,
                               is_payment_creator=True, is_payment_approver=False,
                               can_delete_payment=True)
    return user


@pytest.fixture
def company():
    """Fixture for company object passed as an argument to the company create view test function"""

    company = Company.objects.create(name='Tre G.M.B.H.', country='Germany')
    return company


@pytest.fixture
def administrator():
    """Fixture for admin object passed as an argument to the admin create view test function"""

    administrator = Administrator.objects.create(name='Michał', surname='Paluch',
                                                 login='Udfsr43', password='Password_3',
                                                 password_repeat='Password_3')
    return administrator


@pytest.fixture
def bank():
    """Fixture for bank object passed as an argument to the admin bank view test function"""

    bank = Bank.objects.create(name='Random Bank')
    return bank


@pytest.fixture
def account():
    """Fixture for account object passed as an argument to the account create view test function"""

    bank_test = Bank.objects.create(name='R-Bank')
    company_test = Company.objects.create(name='Tre Belarus', country='Belarus')
    account = Account.objects.create(iban_number='TEEdddddddfs', swift_code='tertrefdsf',
                                     bank=bank_test, company=company_test)
    return account
