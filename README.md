## Задание 2: Автотесты для API сервиса Stellar Burgers

Сервис Stellar Burgers: https://stellarburgers.education-services.ru/

Документация API: https://code.s3.yandex.net/qa-automation-engineer/python-full/diploma/Api-Stellar_Burgers.pdf

## Что покрыто тестами

**1. Создание пользователя (`POST /api/auth/register`)**
- создать уникального пользователя;
- создать пользователя, который уже зарегистрирован;
- создать пользователя и не заполнить одно из обязательных полей.

**2. Логин пользователя (`POST /api/auth/login`)**
- вход под существующим пользователем;
- вход с неверным логином и паролем.

**3. Создание заказа (`POST /api/orders`)**
- с авторизацией;
- без авторизации;
- с ингредиентами;
- без ингредиентов;
- с неверным хешем ингредиентов.


**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов**

Запуск всех автотестов с одновременным сбором данных для Allure:

> `$ pytest -v --alluredir=allure_results`

Запуск тестов конкретной ручки, например, создание пользователя:

> `$ pytest tests/test_create_user.py -v --alluredir=allure_results`

**Посмотреть отчет Allur**

> `$ allure serve allure_results`
