import requests
import allure
from data import Urls


class OrderMethods:

    @staticmethod
    def create_order(payload, token=None):
        with allure.step('Отправить POST-запрос на создание заказа'):
            return requests.post(Urls.ORDERS_URL, json=payload, headers={'Authorization': token})
