import allure
from unittest.mock import patch
import requests
from helpers import register_new_courier_and_return_login_password
@allure.description("Тесты на регистрацию курьеров")
class TestCourierCreation:
    @allure.title("Успешное создание курьера возвращает ok: true")
    @patch('requests.post')
    def test_create_courier_returns_ok_true(self, mock_post):
        # Настраиваем мок
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {'ok': True}

        result = register_new_courier_and_return_login_password()

        assert result  # Проверяем что вернулись данные курьера
        assert mock_post.return_value.json() == {"ok": True}


    @allure.title("Создание дубликата курьера")
    def test_create_two_identical_couriers(self):
        login_pass = register_new_courier_and_return_login_password()

        # Пытаемся создать второго курьера с тем же логином
        response = requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/courier',
            data={
                "login": login_pass[0],
                "password": login_pass[1],
                "firstName": login_pass[2]
            }
        )

        assert response.status_code == 409
        assert response.json().get("message")


    @allure.title("Создание курьера без обязательных полей")
    def test_create_courier_missing_field(self):
        response = requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/courier',
            data={
                "login": "testuser"
            }
        )
        assert response.status_code == 400
        assert response.json().get("message")
