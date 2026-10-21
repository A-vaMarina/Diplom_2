import allure
import pytest

from methods.auth_methods import AuthMethods
from data import Messages
from generators import generate_user_data


@allure.feature('Регистрация пользователя')
class TestRegisterUser:

    @allure.title('Успешная регистрация уникального пользователя')
    def test_register_unique_user_success(self, cleanup_user):
        payload = generate_user_data()
        response = AuthMethods.register_user(payload)
        
        assert response.status_code == 200
        body = response.json()
        # Передаём accessToken фикстуре, чтобы она удалила пользователя после теста
        cleanup_user.append(body["accessToken"])

        assert body['success'] is True
        assert body['user']['name'] == payload['name']
        assert body['user']['email'] == payload['email']
        assert 'accessToken' in body
        assert 'refreshToken' in body

    @allure.title('Сообщение об ошибке при повторной регистрации пользователя')
    def test_register_duplicate_user_error(self, registered_user):
        with allure.step('Получить данные зарегистрированного пользователя'):
            payload = {
                'email': registered_user['email'],
                'password': registered_user['password'],
                'name': registered_user['name']
            }
        response = AuthMethods.register_user(payload)

        assert response.status_code == 403
        assert response.json()['message'] == Messages.REGISTER_USER_ALREADY_EXISTS, (
            f'Получено сообщение "{response.json()["message"]}", '
            f'ожидалось "{Messages.REGISTER_USER_ALREADY_EXISTS}"')

    @allure.title('Ошибка при регистрации без обязательного поля: {missing_field}')
    @pytest.mark.parametrize(
        'missing_field',
        ['email', 'password', 'name'],
        ids=['without_email', 'without_password', 'without_name'],
    )
    def test_register_missing_required_field_error(self, missing_field):
        payload = generate_user_data()
        with allure.step(f'Удалить обязательное поле {missing_field}'):
            payload.pop(missing_field)
        response = AuthMethods.register_user(payload)

        assert response.status_code == 403
        assert response.json()['message'] == Messages.REGISTER_USER_MISSING_FIELDS, (
            f'Получено сообщение "{response.json()["message"]}", '
            f'ожидалось "{Messages.REGISTER_USER_MISSING_FIELDS}"')
            