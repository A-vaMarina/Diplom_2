import allure
import requests

from data import Urls


class AuthMethods:

    @staticmethod
    def register_user(payload):
        with allure.step('Отправить POST-запрос на регистрацию пользователя'):
            return requests.post(Urls.REGISTER_USER_URL, json=payload)

    @staticmethod
    def login_user(payload):
        with allure.step('Отправить POST-запрос на авторизацию пользователя'):
            return requests.post(Urls.LOGIN_USER_URL, json=payload)

    @staticmethod
    def delete_user(token):
        with allure.step('Удалить пользователя'):
            return requests.delete(Urls.USER_URL, headers={'Authorization': token})
        