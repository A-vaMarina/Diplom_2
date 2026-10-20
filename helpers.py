import requests

from data import Urls
from generators import generate_user_data
from methods.auth_methods import AuthMethods


def register_new_user():
    """
    Регистрация нового уникального пользователя.
    Возвращает словарь с данными и токеном, либо None при ошибке.
    """
    payload = generate_user_data()
    response = AuthMethods.register_user(payload)
    
    if response.status_code == 200:
        payload['accessToken'] = response.json()['accessToken']
        return payload
    return None

def get_ingredient_ids(count):
    """
    Получает список _id ингредиентов.
    Возвращает заданное количество id или None.
    """
    response = requests.get(Urls.INGREDIENTS_URL)

    if response.status_code == 200:
        ingredients = response.json()['data']
        return [ingredient['_id'] for ingredient in ingredients[:count]]
    return None
