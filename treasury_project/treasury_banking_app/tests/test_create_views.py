import pytest
from treasury_banking_app.models import User, Company, Administrator

# test to pass with all details correctly provided
@pytest.mark.django_db
def test_user_create_view(client):
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

# test to fail with all missing name
@pytest.mark.django_db
def test_user_create_view(client):
    name = ''
    surname = 'Wolska'
    internal_id = 'PKY8966'
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
def test_company_create_view(client):
    name = 'Tre Bulgaria'
    country = 'Bulgaria'
    response = client.post('/company_create/', {'name': name, 'country': country})

    assert response.status_code == 302
    assert Company.objects.get(name=name)


# test to fail as the login is too long
@pytest.mark.django_db
def test_administrator_create_view(client):
    name = 'Bogdan'
    surname = 'Suchy'
    login = 'PLIjds70'
    password = 'Password_1'
    password_repeat = 'Password_1'
    response = client.post('/admin_create/', {'name': name, 'surname': surname, 'login': login,
                                              'password': password, 'password_repeat': password_repeat})

    assert response.status_code == 302
    assert Administrator.objects.get(name=name)
