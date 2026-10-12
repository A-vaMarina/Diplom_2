class Urls:

    BASE_URL = 'https://stellarburgers.education-services.ru'

    REGISTER_USER_URL = f'{BASE_URL}/api/auth/register'   # POST   — регистрация
    LOGIN_USER_URL    = f'{BASE_URL}/api/auth/login'      # POST   — авторизация
    LOGOUT_USER_URL   = f'{BASE_URL}/api/auth/logout'     # POST   — выход из системы
    REFRESH_TOKEN_URL = f'{BASE_URL}/api/auth/token'      # POST   — обновление токена
    USER_URL          = f'{BASE_URL}/api/auth/user'       # GET/PATCH/DELETE — данные пользователя

    ORDERS_URL      = f'{BASE_URL}/api/orders'            # POST — создание заказа, GET — заказы пользователя
    ALL_ORDERS_URL  = f'{BASE_URL}/api/orders/all'        # GET  — все заказы

    INGREDIENTS_URL = f'{BASE_URL}/api/ingredients'       # GET  — список ингредиентов


class Messages:

    # POST /api/auth/register — регистрация
    REGISTER_USER_ALREADY_EXISTS = "User already exists"                     # 403
    REGISTER_USER_MISSING_FIELDS = "Email, password and name are required fields"  # 403

    # POST /api/auth/login — авторизация
    LOGIN_INVALID_CREDENTIALS = "email or password are incorrect"            # 401

    # GET/PATCH/DELETE /api/auth/user — данные пользователя
    USER_UNAUTHORIZED         = "You should be authorised"                   # 401
    USER_EMAIL_ALREADY_EXISTS = "User with such email already exists"        # 403

    # POST /api/orders — создание заказа
    ORDER_INGREDIENTS_REQUIRED = "Ingredient ids must be provided"           # 400
    # 500 Internal Server Error возвращается при невалидном хеше — тела с message нет

    # GET /api/orders — заказы пользователя
    ORDERS_UNAUTHORIZED = "You should be authorised"                         # 401
