from generators import generate_user_data
from methods.auth_methods import AuthMethods
from methods.order_methods import OrderMethods


def register_new_user():
    """
    Регистрация нового уникального пользователя.
    Возвращает словарь с данными и токеном.
    """
    payload = generate_user_data()
    response = AuthMethods.register_user(payload)
    
    if response.status_code != 200:
        raise Exception(f"Не удалось зарегистрировать пользователя: {response.status_code} {response.text}")
        
    payload['accessToken'] = response.json()['accessToken']
    return payload


def get_ingredient_ids(count):
    """
    Получает список _id ингредиентов.
    Возвращает заданное количество id.
    """
    response = OrderMethods.get_ingredients()

    if response.status_code != 200:
        raise Exception(f"Не удалось получить ингредиенты: {response.status_code} {response.text}")
        
    ingredients = response.json()['data']
    return [ingredient['_id'] for ingredient in ingredients[:count]]
