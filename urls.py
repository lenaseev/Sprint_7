class Urls:
    BASE = 'https://qa-scooter.praktikum-services.ru/api/v1'

    # Курьер
    COURIER = f"{BASE}/courier"
    COURIER_LOGIN = f"{BASE}/courier/login"

    # Заказы
    ORDERS = f"{BASE}/orders"

    def courier_delete(self, courier_id):
        return f"{self.BASE}/courier/{courier_id}"