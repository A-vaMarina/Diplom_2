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
    """
    Пред- и постусловие для тестов, которым нужен уже
    зарегистрированный пользователь. Удаляет пользователя после теста.
    """
    user = register_new_user()
    cleanup_user.append(user['accessToken'])
    return user

@pytest.fixture
def authorized_user(cleanup_user):
    """
    Регистрирует пользователя, логинит его,
    возвращает accessToken, который используется
    для запросов, требующих авторизацию.
    Удаляет пользователя после теста.
    """
    user = register_new_user()
    cleanup_user.append(user['accessToken'])

    response = AuthMethods.login_user(user['email'], user['password'])
    return response.json()['accessToken']
