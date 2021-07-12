import pytest
from django.test import Client
from treasury_banking_app.models import User, Company, Administrator


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
