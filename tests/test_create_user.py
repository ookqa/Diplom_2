import allure
import requests
from data import GenerateUserCredentials, ExistentUserCredentials
import pytest
from urls import Urls


class TestCreateUser:
    data_empty_field = [
        {'email': '',
         'password': GenerateUserCredentials.password,
         'name': GenerateUserCredentials.name
         },
        {'email': GenerateUserCredentials.email,
         'password': '',
         'name': GenerateUserCredentials.name
         },
        {'email': GenerateUserCredentials.email,
         'password': GenerateUserCredentials.password,
         'name': ''
         }
    ]

    @allure.title('Проверка успешного создания пользователя')
    @allure.description('При создании курьера передаются все три поля: email, password, name')
    def test_create_user_all_fields_success_create(self):
        email = GenerateUserCredentials.email
        password = GenerateUserCredentials.password
        name = GenerateUserCredentials.name
        payload = {'email': email, 'password': password, 'name': name}
        response = requests.post(Urls.REGISTER_USER, data=payload)
        data = response.json()

        assert response.status_code == 200 and data["success"] == True

        # удалим созданного пользователя
        access_token = data.get("accessToken")
        requests.delete(f"{Urls.DELETE_USER}", headers={'Authorization': f'{access_token}'})

    @allure.title('Проверка невозможности создания двух одинаковых пользователей')
    @allure.description('При создании, используются все креды уже созданного пользователя')
    def test_create_user_existent_user_error(self):
        email = ExistentUserCredentials.email
        password = ExistentUserCredentials.password
        name = ExistentUserCredentials.name
        payload = {'email': email, 'password': password, 'name': name}
        response = requests.post(Urls.REGISTER_USER, data=payload)
        data = response.json()

        assert response.status_code == 403 and data["success"] == False

    @allure.title('Проверка невозможности создания пользователя, если передаются не все поля')
    @allure.description('При создании не передается каждое из полей email, password, name')
    @pytest.mark.parametrize("user_data", data_empty_field)
    def test_create_user_empty_email_pass_name_field_error(self, user_data):

        response = requests.post(Urls.REGISTER_USER, data=user_data)
        response_data = response.json()
        assert response.status_code == 403 and response_data["success"] == False

