import allure

from faker import Faker


fake = Faker()

def generate_user_data():
    with allure.step('Сгенерировать данные для создания пользователя'):
        return {
            "email": fake.email(),
            "password": fake.password(length=10),
            "name": fake.first_name()
        }
