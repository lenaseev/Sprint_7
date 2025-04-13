import requests
import allure
from urls import Urls

@allure.suite("Тесты авторизации курьеров")
class TestLoginCourier:
    @allure.title("Успешная авторизация курьера")
    def test_successful_login(self, create_courier):
        urls = Urls()
        login, password, _ = create_courier

        response = requests.post(
            urls.COURIER_LOGIN,
            data={"login": login,
                  "password": password}
        )

        assert response.status_code == 200
        assert "id" in response.json()

    @allure.title("Авторизация без логина")
    def test_login_without_login_field(self, create_courier):
        urls = Urls()
        _, password, _ = create_courier

        response = requests.post(
            urls.COURIER_LOGIN,
            data={
                "password": password}
        )

        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json().get("message")

    @allure.title("Авторизация без пароля")
    def test_login_without_password_field(self, create_courier):
        urls = Urls()
        login, _, _ = create_courier

        response = requests.post(
            urls.COURIER_LOGIN,
            data={
                "login": login}
        )

        assert response.status_code == 400
        assert "Недостаточно данных для входа" in response.json().get("message")

    @allure.title("Авторизация с несуществующим паролем")
    def test_login_with_wrong_password(self, create_courier):
        urls = Urls()
        login, _, _ = create_courier

        response = requests.post(
            urls.COURIER_LOGIN,
            data={
                "login": login,
                "password": "password"}
        )

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message")

    @allure.title("Авторизация с несуществующим логином")
    def test_login_with_wrong_login(self, create_courier):
        urls = Urls()
        _, password, _ = create_courier

        response = requests.post(
            urls.COURIER_LOGIN,
            data={
                "login": "login",
                "password": password}
        )

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message")

    @allure.title("Авторизация несуществующего пользователя")
    def test_login_with_non_existent_user(self):
        urls = Urls()
        response = requests.post(
            urls.COURIER_LOGIN,
            data={
                "login": "login",
                "password": "password"}
        )

        assert response.status_code == 404
        assert "Учетная запись не найдена" in response.json().get("message")