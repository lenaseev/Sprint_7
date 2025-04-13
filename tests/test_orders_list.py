import requests
import allure
from urls import Urls


@allure.suite("Тесты на получение списка заказов")
class TestOrderList:
    @allure.suite("Тесты список заказов")
    def test_get_orders_returns_list(self):
        urls = Urls()
        response = requests.get(urls.ORDERS)

        assert response.status_code == 200
        assert "orders" in response.json()