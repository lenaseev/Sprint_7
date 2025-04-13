import pytest
from helpers import register_new_courier_and_return_login_password, delete_courier


@pytest.fixture
def create_courier():
    # Регистрируем нового курьера
    login_pass = register_new_courier_and_return_login_password()
    yield login_pass  # передаем данные тестам

    # Удаляем курьера после выполнения теста
    if login_pass:  # если регистрация прошла успешно
        delete_courier(login_pass[0], login_pass[1])