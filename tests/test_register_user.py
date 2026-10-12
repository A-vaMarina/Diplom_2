import requests
import allure
import pytest

from data import Urls, Messages
from generators import generate_user_data


@allure.feature('Регистрация пользователя')
class TestRegisterUser:

    @allure.title('Успешная регистрация уникального пользователя')
    def test_register_unique_user_success(self, cleanup_user):
        with allure.step('Сгенерировать данные для пользователя'):
            payload = generate_user_data()

        with allure.step('Отправить POST-запрос на регистрацию пользователя'):
            response = requests.post(Urls.REGISTER_USER_URL, json=payload)
            body = response.json()

        # Передаём accessToken фикстуре, чтобы она удалила пользователя после теста
        cleanup_user.append(body["accessToken"])

        assert response.status_code == 200
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

        with allure.step('Отправить POST-запрос на регистрацию уже созданного пользователя'):
            response = requests.post(Urls.REGISTER_USER_URL, json=payload)

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
        with allure.step('Сгенерировать данные и удалить одно обязательное поле'):
            payload = generate_user_data()
            payload.pop(missing_field)

        with allure.step(f'Отправить POST-запрос на регистрацию без поля "{missing_field}"'):
            response = requests.post(Urls.REGISTER_USER_URL, json=payload)

        assert response.status_code == 403
        assert response.json()['message'] == Messages.REGISTER_USER_MISSING_FIELDS, (
            f'Получено сообщение "{response.json()["message"]}", '
            f'ожидалось "{Messages.REGISTER_USER_MISSING_FIELDS}"')
            