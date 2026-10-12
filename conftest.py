import pytest

from helpers import delete_user, register_new_user


@pytest.fixture
def cleanup_user():
    """
    Постусловие для тестов на регистрацию пользователя.
    Тест создаёт пользователя и передает фикстуре access_token.
    После теста фикстура удаляет пользователя.
    """
    tokens = []

    yield tokens

    for token in tokens:
        delete_user(token)

@pytest.fixture
def registered_user(cleanup_user):
    """
    Пред- и постусловие для тестов, которым нужен уже
    зарегистрированный пользователь. Удаляет пользователя после теста.
    """
    user = register_new_user()
    cleanup_user.append(user['accessToken'])
    return user


