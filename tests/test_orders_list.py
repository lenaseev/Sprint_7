import requests
import allure
@allure.description("Тесты на получение списка заказов")
class TestOrderList:
    @allure.suite("Тесты список заказов")
    def test_get_orders_returns_list(self):
        response = requests.get('https://qa-scooter.praktikum-services.ru/api/v1/orders')

        assert response.status_code == 200
        assert "orders" in response.json()