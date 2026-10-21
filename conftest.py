import pytest

from helpers import register_new_user
from methods.auth_methods import AuthMethods


@pytest.fixture
def cleanup_user():
    tokens = []
    yield tokens
    for token in tokens:
        AuthMethods.delete_user(token)

@pytest.fixture
def registered_user(cleanup_user):
    user = register_new_user()
    cleanup_user.append(user['accessToken'])
    return user

@pytest.fixture
def authorized_user(registered_user):
    payload = {'email': registered_user['email'], 'password': registered_user['password']}
    response = AuthMethods.login_user(payload)
    assert response.status_code == 200, f'Не удалось авторизовать пользователя: {response.status_code} {response.text}'
    return response.json()['accessToken']
