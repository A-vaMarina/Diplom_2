import requests
import allure
import pytest

from data import Urls, Messages


@allure.feature('Авторизация пользователя')
class TestLoginUser:

    @allure.title('Успешная авторизация существующего пользователя')
    def test_login_existing_user_success(self, registered_user):
        with allure.step('Получить email и пароль зарегистрированного пользователя'):
            payload = {
                'email': registered_user['email'],
                'password': registered_user['password']
            }
        with allure.step('Отправить POST-запрос на авторизацию'):
            response = requests.post(Urls.LOGIN_USER_URL, json=payload)
            body = response.json()

        assert response.status_code == 200
        assert body['success'] is True
        assert 'accessToken' in body
        assert 'refreshToken' in body
        assert body['user']['email'] == registered_user['email'], (
            f'Получен email={body["user"]["email"]}, '
            f'ожидался {registered_user["email"]}')
        assert body['user']['name'] == registered_user['name'], (
            f'Получен name={body["user"]["name"]}, '
            f'ожидался {registered_user["name"]}')

    @allure.title('Получение ошибки при входе с неверными учётными данными: {wrong_field}')
    @pytest.mark.parametrize(
        'wrong_field',
        ['email', 'password'],
        ids=['wrong_email', 'wrong_password'],
    )
    def test_login_invalid_credentials_error(self, registered_user, wrong_field):
        with allure.step(f'Сформировать данные с неверным полем "{wrong_field}"'):
            payload = {
                'email': registered_user['email'],
                'password': registered_user['password'],
            }
            payload[wrong_field] = f'wrong_{payload[wrong_field]}'

        with allure.step('Отправить POST-запрос на авторизацию с неверными данными'):
            response = requests.post(Urls.LOGIN_USER_URL, json=payload)
            body = response.json()

        assert response.status_code == 401, (
            f'Получен статус-код {response.status_code}, ожидался 401')
        assert body['success'] is False
        assert body['message'] == Messages.LOGIN_INVALID_CREDENTIALS, (
            f'Получено сообщение "{body["message"]}", '
            f'ожидалось "{Messages.LOGIN_INVALID_CREDENTIALS}"')
        