import pytest
from treasury_banking_app.models import User


@pytest.mark.django_db
def test_user_view(client, user):
    id_ = user.pk
    response = client.get(f'/user_view/{id_}/')
    assert response.status_code == 200
    # assert response.context['user']['name'] == user.name

