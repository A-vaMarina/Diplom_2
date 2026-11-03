import requests
import allure

from data import Urls


class OrderMethods:

    @staticmethod
    def create_order(payload, token=None):
        headers = {'Authorization': token} if token else {}
        with allure.step('Отправить POST-запрос на создание заказа'):
            return requests.post(Urls.ORDERS_URL, json=payload, headers=headers)

    @staticmethod
    def get_ingredients():
        with allure.step('Отправить GET-запрос на получение списка ингредиентов'):
            return requests.get(Urls.INGREDIENTS_URL)
        