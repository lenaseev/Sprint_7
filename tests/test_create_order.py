import pytest
import requests
from data import BASE_ORDER_DATA
import allure
from urls import Urls

@allure.suite("Тесты на создание заказов")
class TestCreateOrder:
    @allure.title("Создание заказа с цветом: {color}")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_create_order_with_different_colors(self, color):
        urls = Urls()
        order_data = BASE_ORDER_DATA.copy()
        order_data["color"] = color

        response = requests.post(
            urls.ORDERS,
            json=order_data
        )

        assert response.status_code == 201
        assert "track" in response.json()