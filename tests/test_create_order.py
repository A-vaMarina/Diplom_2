import requests
import allure
import pytest

from data import Urls, Messages
from helpers import get_ingredient_ids


@allure.feature('Создание заказа')
class TestCreateOrder:

    @allure.title('Успешное создание заказа с авторизацией и с ингредиентами')
    def test_create_order_with_auth_with_ingredients_success(self, authorized_user):
        with allure.step('Получить хеши 3-х ингредиентов'):
            ingredients = get_ingredient_ids(count=3)

        with allure.step('Отправить POST-запрос на создание заказа с авторизацией'):
            payload = {'ingredients': ingredients}
            response = requests.post(Urls.ORDERS_URL, json=payload, headers={'Authorization': authorized_user})
        
        assert response.status_code == 200
        assert response.json()['success'] is True

    @allure.title('Ошибка при создании заказа с ингредиентами без авторизации')
    def test_create_order_with_ingredients_unauthorized_error(self):
        with allure.step('Получить id двух ингредиентов'):
            ingredients = get_ingredient_ids(count=2)

        with allure.step('Отправить POST-запрос на создание заказа без авторизации'):
            payload = {'ingredients': ingredients}
            response = requests.post(Urls.ORDERS_URL, json=payload)
            body = response.json()

        assert response.status_code == 401
        assert body['message'] == Messages.ORDERS_UNAUTHORIZED, (
            f'Получено сообщение "{body["message"]}", '
            f'ожидалось "{Messages.ORDERS_UNAUTHORIZED}"')

    