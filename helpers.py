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
