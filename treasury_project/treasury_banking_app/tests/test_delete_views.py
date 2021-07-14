import pytest

from treasury_banking_app.models import User, Company


@pytest.mark.django_db
def test_user_delete_view(client, user):
    id_ = user.pk
    response = client.get(f'/user_delete/{id_}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_company_delete_view(client, company):
    id_ = company.pk
    response = client.get(f'/company_delete/{id_}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_account_delete_view(client, account):
    id_ = account.pk
    response = client.get(f'/account_delete/{id_}/')
    assert response.status_code == 200
