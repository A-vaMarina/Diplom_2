from faker import Faker


fake = Faker()

def generate_user_data():
    # генерация данных для создания пользователя
    return {
        "email": fake.email(),
        "password": fake.password(length=10),
        "name": fake.first_name()
    }
