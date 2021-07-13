import pytest

from treasury_banking_app.models import User


@pytest.mark.django_db
def test_user_delete_view(client, user):
    id_ = user.pk
    response = client.get(f'/user_delete/{id_}')
    assert response.status_code == 301
    assert User.objects.filter(name=user.name).delete()
