class DebugData:
    example_client = {"id": 1,
                      "login": "kdanil01",
                      "password": "begemot",
                      "account_type": "admin",
                      "name": "Даниил",
                      "surname": "Капитанов",
                      "last_name": "Сергеевич",
                      "address": "[Засекречено]",
                      "email": "kdanil01@mail.ru",
                      "phone_number": "89052482424",
                      "date_of_birth": "09.02.2001",
                      "date_of_registration": "02.12.2022"
                      }
    example_cosmetologist = {"id": 1,
                      "name": "Даниил",
                      "surname": "Капитанов",
                      "last_name": "Сергеевич",
                      "address": "[Засекречено]",
                      "email": "kdanil01@mail.ru",
                      "phone_number": "89052482424",
                      "date_of_birth": "09.02.2001",
                      "date_of_hire": "02.12.2022"
                      }
    example_login = "kdanil01"
    example_password = "begemot"


class UISettings:
    title = 'Салон Красоты'
    login_window_resolution = '400x220'
    registration_window_resolution = '560x420'
    profile_window_resolution = '720x380'
    appointment_window_resolution = '360x180'
    font_big = ("League Gothic", 24)
    font_medium = ("League Gothic", 16)


class DatabaseSettings:
    database_type = "postgresql+psycopg2"
    user = "postgres"
    password = "sosiska12"
    host = "localhost"
    database_name = "beauty_saloon"


class LoggingText:
    user_created_log = "User added successfully!"
    login_failed_log = "Неверный логин или пароль"


class LoginWindowText:
    title_label = "Салон Красоты"
    login_label = "Логин:"
    password_label = "Пароль:"
    login_button = "Войти"
    registration_button = "Зарегистрироваться"


class RegistrationWindowText:
    title_label = "Регистрация"
    name_label = "Имя"
    surname_label = "Фамилия"
    last_name_label = "Отчество"
    address_label = "Адрес"
    email_label = "Эл. Почта"
    phone_number_label = "Телефон"
    date_of_birth_label = "Дата рождения"
    login_label = "Логин"
    password_label = "Пароль"
    password_confirmation_label = "Подтвердите пароль"
    registration_button = "Зарегистрироваться"
    back_button = "Назад"


class ProfileWindowText:
    title_label = "Текущий пользователь: {}"
    current_user_label = "Текущий пользователь: {}"
    name_label = "Имя: {}"
    surname_label = "Фамилия: {}"
    last_name_label = "Отчество: {}"
    address_label = "Адрес: {}"
    email_label = "Электронная почта: {}"
    phone_number_label = "Телефон: {}"
    date_of_birth_label = "Дата рождения: {}"
    logout_button = "Выйти из аккаунта"
    create_appointment_button = "Записаться"


class AppointmentWindowText:
    title_label = "Запись на приём"
    back_button = "Отмена"
    apply_button = "Записаться"
    date_label = "Введите дату записи"
    available_cosmetologists_dropdown = "Выберите косметолога"
    create_appointment_button = "Записаться"
