import requests

from data import Urls
from generators import generate_user_data


def delete_user(token):
    return requests.delete(Urls.USER_URL, headers={'Authorization': token})

def register_new_user():
    """
    Регистрация нового уникального пользователя.
    Возвращает словарь {'email', 'password', 'name', 'accessToken'} или None, если регистрация не удалась.
    """
    payload = generate_user_data()
    
    response = requests.post(Urls.REGISTER_USER_URL, json=payload)
    
    if response.status_code == 200:
        payload['accessToken'] = response.json()['accessToken']
        return payload
    return None

def login_user(email, password):
    payload = {'email': email, 'password': password}
    return requests.post(Urls.LOGIN_USER_URL, json=payload)

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