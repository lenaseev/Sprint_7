import pytest
import requests
from data import BASE_ORDER_DATA
import allure

@allure.description("Тесты на создание заказов")
class TestCreateOrder:
    @allure.title("Создание заказа с цветом: {color}")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None
    ])
    def test_create_order_with_different_colors(self, color):
        order_data = BASE_ORDER_DATA.copy()
        if color is not None:
            order_data["color"] = color

        response = requests.post(
            'https://qa-scooter.praktikum-services.ru/api/v1/orders',
            json=order_data
        )

        assert response.status_code == 201
        assert "track" in response.json()