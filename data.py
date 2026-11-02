class Urls:

    BASE_URL = 'https://qa-stellarburgers.education-services.ru'

    REGISTER_USER_URL = f'{BASE_URL}/api/auth/register'   # POST   — регистрация
    LOGIN_USER_URL = f'{BASE_URL}/api/auth/login'         # POST   — авторизация
    ORDERS_URL = f'{BASE_URL}/api/orders'                 # POST — создание заказа
    INGREDIENTS_URL = f'{BASE_URL}/api/ingredients'       # GET  — список ингредиентов
    USER_URL = f'{BASE_URL}/api/auth/user'                # DELETE - удаление пользователя

class Messages:

    # POST /api/auth/register — регистрация
    REGISTER_USER_ALREADY_EXISTS = "User already exists"                     # 403
    REGISTER_USER_MISSING_FIELDS = "Email, password and name are required fields"  # 403

    # POST /api/auth/login — авторизация
    LOGIN_INVALID_CREDENTIALS = "email or password are incorrect"            # 401

    # POST /api/orders — создание заказа
    ORDER_INGREDIENTS_REQUIRED = "Ingredient ids must be provided"           # 400
    ORDERS_UNAUTHORIZED = "You should be authorised"                         # 401
    # 500 Internal Server Error возвращается при невалидном хеше
    