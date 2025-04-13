import allure
import requests
from helpers import register_new_courier_and_return_login_password, generate_random_string
from urls import Urls

@allure.suite("Тесты на регистрацию курьеров")
class TestCourierCreation:
    @allure.title("Успешное создание курьера возвращает ok: true")
    def test_create_courier_returns_ok_true(self):
        urls = Urls()
        payload = {
            "login": generate_random_string(10),
            "password": generate_random_string(10),
            "firstName": generate_random_string(10)
        }

        response = requests.post(urls.COURIER, data=payload)

        assert response.status_code == 201
        assert response.json() == {"ok": True}


    @allure.title("Создание дубликата курьера")
    def test_create_two_identical_couriers(self):
        login_pass = register_new_courier_and_return_login_password()
        urls = Urls()
        # Пытаемся создать второго курьера с тем же логином
        response = requests.post(
            urls.COURIER,
            data={
                "login": login_pass[0],
                "password": login_pass[1],
                "firstName": login_pass[2]
            }
        )

        assert response.status_code == 409
        assert "Этот логин уже используется. Попробуйте другой." in response.json().get("message")


    @allure.title("Создание курьера без обязательных полей")
    def test_create_courier_missing_field(self):
        urls = Urls()
        response = requests.post(
            urls.COURIER,
            data={
                "login": "testuser"
            }
        )
        assert response.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in response.json().get("message")
