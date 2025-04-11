import requests
from helpers import register_new_courier_and_return_login_password
import allure
@allure.description("Тесты авторизации курьеров")
class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    def test_successful_login(self):
        # Регистрируем нового курьера
        login_pass = register_new_courier_and_return_login_password()

        # Пробуем авторизоваться
        response = requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
            data={
                "login": login_pass[0],
                "password": login_pass[1]
            }
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация без логина")
    def test_login_without_login_field(self):
        login_pass = register_new_courier_and_return_login_password()

        response = requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
            data={
                "password": login_pass[1]
            }
        )

        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json().get("message")

    @allure.title("Авторизация без пароля")
    def test_login_without_password_field(self):
        login_pass = register_new_courier_and_return_login_password()

        response = requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
            data={
                "login": login_pass[0]}
        )

        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json().get("message", "")

    @allure.title("Авторизация с несуществующим паролем")
    def test_login_with_wrong_password(self):
        login_pass = register_new_courier_and_return_login_password()

        response = requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
            data={
                "login": login_pass[0],
                "password": "password"}
        )

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message", "")

    @allure.title("Авторизация с несуществующим логином")
    def test_login_with_wrong_login(self):
        login_pass = register_new_courier_and_return_login_password()

        response = requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
            data={
                "login": "login",
                "password": login_pass[1]}
        )

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message")

    @allure.title("Авторизация несуществующего пользователя")
    def test_login_with_non_existent_user(self):
        response = requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/courier/login',
            data={
                "login": "login",
                "password": "password"}
        )

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message")