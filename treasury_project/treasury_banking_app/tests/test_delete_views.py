import pytest


@pytest.mark.django_db
def test_user_delete_view(client, user):
    """Test to delete a user - this test tests only opening the view for deletion confirmation"""

    id_ = user.pk
    response = client.get(f'/user_delete/{id_}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_company_delete_view(client, company):
    """Test to delete a company - this test tests only opening the view for deletion confirmation"""

    id_ = company.pk
    response = client.get(f'/company_delete/{id_}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_account_delete_view(client, account):
    """Test to delete an account - this test tests only opening the view for deletion confirmation"""

    id_ = account.pk
    response = client.get(f'/account_delete/{id_}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_bank_delete_view(client, bank):
    """Test to delete a bank - this test tests only opening the view for deletion confirmation"""

    id_ = bank.pk
    response = client.get(f'/bank_delete/{id_}/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_admin_delete_view(client, administrator):
    """Test to delete an admin - this test tests only opening the view for deletion confirmation"""

    id_ = administrator.pk
    response = client.get(f'/admin_delete/{id_}/')
    assert response.status_code == 200