import pytest


@pytest.mark.django_db
def test_user_view(client, user):
    """Test to view user from information passed in the context"""
    id_ = user.pk
    response = client.get(f'/user_view/{id_}/')
    assert response.status_code == 200
    assert response.context['name'] == user.name
    assert response.context['surname'] == user.surname
    assert response.context['internal_id'] == user.internal_id
    assert response.context['is_administrator'] == user.is_administrator
    assert response.context['is_payment_approver'] == user.is_payment_approver
    assert response.context['is_payment_creator'] == user.is_payment_creator
    assert response.context['can_delete_payment'] == user.can_delete_payment

