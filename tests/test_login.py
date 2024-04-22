import allure
import requests
from data import ExistentUserCredentials
from urls import Urls


class TestLogin:

    @allure.title('Проверка логина под существующим пользователем')
    @allure.description('При логине передаются email и password уже созданного пользователя')
    def test_login_actual_email_and_password_success(self, create_new_user):
        user_data, response_data = create_new_user
        email, password, name = user_data
        payload = {'email': email, 'password': password}
        response = requests.post(Urls.LOGIN, data=payload)
        login_data = response.json()

        assert (
                response.status_code == 200 and
                login_data["success"] == True and
                login_data["user"]["email"] == email and
                login_data["user"]["name"] == name
        )

    @allure.title('Проверка логина с неправильным и паролем')
    @allure.description('При логине передаются правильный email и неправильный password уже созданного пользователя')
    def test_login_wrong_password_error(self):
        email = ExistentUserCredentials.email
        password = ExistentUserCredentials.wrong_password
        payload = {'email': email, 'password': password}
        response = requests.post(Urls.LOGIN, data=payload)
        login_data = response.json()

        assert response.status_code == 401 and login_data["success"] == False

    @allure.title('Проверка логина несуществующего пользователя')
    @allure.description('При логине передаются несуществующие email и password')
    def test_login_wrong_email_wrong_password_error(self):
        email = ExistentUserCredentials.wrong_email
        password = ExistentUserCredentials.wrong_password
        payload = {'email': email, 'password': password}
        response = requests.post(Urls.LOGIN, data=payload)
        login_data = response.json()

        assert response.status_code == 401 and login_data["success"] == False
