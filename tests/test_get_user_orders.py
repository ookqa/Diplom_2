import allure
import requests
from urls import Urls


class TestGetUserOrder:

    @allure.title('Проверка получения списка заказов авторизованного пользователя')
    @allure.description('При запросе передается токен пользователя и отображаются его последние заказы')
    def test_get_user_orders_authorized_user_actual_order_success(self, create_new_user, create_new_order):
        access_token = create_new_user[1]["accessToken"]
        headers = {"Authorization": f"{access_token}"}
        response = requests.get(f'{Urls.GET_USER_ORDERS}', headers=headers)
        data = response.json()

        assert response.status_code == 200 and data["success"] == True and 'orders' in data

    @allure.title('Проверка получения списка заказов неавторизованного пользователя')
    @allure.description('При запросе передается токен пользователя')
    def test_get_user_orders_unauthorized_user_error(self):
        response = requests.get(f'{Urls.GET_USER_ORDERS}')
        data = response.json()

        assert response.status_code == 401 and data["success"] == False


