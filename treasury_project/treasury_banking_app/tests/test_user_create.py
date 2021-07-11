import pytest
from treasury_banking_app.models import User


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
